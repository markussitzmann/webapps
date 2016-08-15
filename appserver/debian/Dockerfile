FROM debian:jessie

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
    
