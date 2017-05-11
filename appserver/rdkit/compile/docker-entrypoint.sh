#!/bin/bash
#set -e



set_listen_addresses() {
	sedEscapedValue="$(echo "$1" | sed 's/[\/&]/\\&/g')"
	sed -ri "s/^#?(listen_addresses\s*=\s*)\S+/\1'$sedEscapedValue'/" "$PGDATA/postgresql.conf"
}


if [ "$1" = 'postgres' ]; then

    source activate appserver

	mkdir -p "$PGDATA"

	# look specifically for PG_VERSION, as it is expected in the DB dir
	if [ ! -s "$PGDATA/PG_VERSION" ]; then

	    initdb --username postgres

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
			-w start \
			-U postgres

		: ${POSTGRES_USER:=appserver}
		: ${POSTGRES_DB:=$POSTGRES_USER}
		export POSTGRES_USER POSTGRES_DB

		psql --username postgres <<-EOSQL
			CREATE USER appserver WITH SUPERUSER $pass ;
		EOSQL
		echo

		echo

        createdb


        psql --username postgres <<-EOSQL
			CREATE EXTENSION rdkit ;
		EOSQL

		# we don't support this currently:
		#for f in /docker-entrypoint-initdb.d/*; do
		#	case "$f" in
		#		*.sh)  echo "$0: running $f"; . "$f" ;;
		#		*.sql) echo "$0: running $f"; psql --username appserver --dbname appserver < "$f" && echo ;;
		#		*)     echo "$0: ignoring $f" ;;
		#	esac
		#	echo
		#done

		pg_ctl -D "$PGDATA" -m fast -w stop -U postgres
		set_listen_addresses '*'

		echo
		echo 'PostgreSQL init process complete; ready for start up.'
		echo
	fi
fi

if [ "$1" = 'python' ]; then

    source activate appserver

fi


exec "$@"

