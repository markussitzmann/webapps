FROM debian:jessie
ARG appserver_gid
ARG appserver_uid

RUN (echo "deb http://httpredir.debian.org/debian/ jessie main contrib non-free" > /etc/apt/sources.list && \ 
    echo "deb http://httpredir.debian.org/debian/ jessie-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb http://security.debian.org/ jessie/updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src http://httpredir.debian.org/debian jessie main contrib non-free" >> /etc/apt/sources.list)

RUN apt-get update --fix-missing && apt-get install -y \
    tar \
    wget \
    git \
    bzip2 \
    ca-certificates \
    build-essential \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    libcairo2-dev \
	nginx \
	supervisor \
	postgresql-client \
	libjpeg-dev \
	libpng-dev \
	libpq-dev \
	unzip \
	flex \
	bison \
    libfreetype6 \
    libfreetype6-dev \
    libtiff5-dev \
    libjpeg62-turbo-dev \
    libxml2-dev \
    libxslt1-dev
    
# grab gosu for easy step-down from root
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
	&& wget --no-check-certificate -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
	&& wget --no-check-certificate -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
	&& gpg --verify /usr/local/bin/gosu.asc \
	&& rm /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu

# make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by default
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8


RUN apt-get update -y

# explicitly set user/group IDs
RUN groupadd postgres --gid=999 && \
    groupadd appserver --gid=${appserver_gid} && \
    useradd -g postgres --uid=999 postgres && \
    useradd -g appserver --uid=${appserver_uid} appserver && \
    usermod -G postgres appserver