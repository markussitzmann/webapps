FROM appserver_debian_image

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.0.5-Linux-x86_64.sh && \
    /bin/bash /Miniconda2-4.0.5-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda2-4.0.5-Linux-x86_64.sh

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

RUN apt-get update -y

ENV PATH /opt/conda/bin:$PATH

RUN conda update conda --yes --quiet && \
    conda install jinja2 conda-build --yes --quiet && \
    conda install anaconda-client --yes --quiet && \
    conda install patchelf --yes --quiet && \
    conda install python=3.5 --yes --quiet

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# explicitly set user/group IDs
RUN groupadd -r appserver --gid=1000 && useradd -r -g appserver --uid=1000 appserver

RUN mkdir -p /opt/appserver && \
    chown -R appserver.appserver /opt/appserver && \
    chown -R appserver.appserver /opt/conda
USER appserver














