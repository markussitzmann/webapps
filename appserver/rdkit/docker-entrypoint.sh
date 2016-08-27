#!/bin/bash
#set -e



set_listen_addresses() {
	sedEscapedValue="$(echo "$1" | sed 's/[\/&]/\\&/g')"
	sed -ri "s/^#?(listen_addresses\s*=\s*)\S+/\1'$sedEscapedValue'/" "$PGDATA/postgresql.conf"
}



if [ "$1" = 'postgres' ]; then

    conda create --use-local --yes --quiet --name appserver python rdkit rdkit-postgresql95 postgresql95
    source activate appserver

	mkdir -p "$PGDATA"
	initdb

    echo "-----"
    echo $PGDATA
    echo $POSTGRES_PASSWORD
    echo $POSTGRES_USER
    echo "-----"

	# check password first so we can output the warning before postgres
	# messes it up
	if [ "$POSTGRES_PASSWORD" ]; then
		pass="PASSWORD '$POSTGRES_PASSWORD'"
		authMethod=md5
	else
		# The - option suppresses leading tabs but *not* spaces. :)
		cat >&2 <<-'EOWARN'
			****************************************************
			WARNING: No password has been set for the database.
			         This will allow anyone with access to the
			         Postgres port to access your database. In
			         Docker's default configuration, this is
			         effectively any other container on the same
			         system.
			         Use "-e POSTGRES_PASSWORD=password" to set
			         it in "docker run".
				****************************************************
		EOWARN
		pass=
		authMethod=trust
	fi

	{ echo; echo "host all all 0.0.0.0/0 $authMethod"; } >> "$PGDATA/pg_hba.conf"

	# internal start of server in order to allow set-up using psql-client		
	# does not listen on TCP/IP and waits until start finishes
	pg_ctl -D "$PGDATA" \
		-o "-c listen_addresses=''" \
		-w start

	: ${POSTGRES_USER:=postgres}
	: ${POSTGRES_DB:=$POSTGRES_USER}
	export POSTGRES_USER POSTGRES_DB

	if [ "$POSTGRES_DB" != 'postgres' ]; then
		createdb ${POSTGRES_DB}
	fi

	psql --username "$POSTGRES_USER" <<-EOSQL
		AlTER USER "$POSTGRES_USER" WITH SUPERUSER $pass ;
	
	EOSQL
	echo
	
	echo
	for f in /docker-entrypoint-initdb.d/*; do
		case "$f" in
			*.sh)  echo "$0: running $f"; . "$f" ;;
			*.sql) echo "$0: running $f"; psql --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" < "$f" && echo ;;
			*)     echo "$0: ignoring $f" ;;
		esac
		echo
	done

	pg_ctl -D "$PGDATA" -m fast -w stop
	set_listen_addresses '*'

	echo
	echo 'PostgreSQL init process complete; ready for start up.'
	echo
	
fi

if [ "$1" = 'python' ]; then

    conda create --use-local --yes --quiet --name appserver python rdkit
    source activate appserver

fi


exec "$@"

