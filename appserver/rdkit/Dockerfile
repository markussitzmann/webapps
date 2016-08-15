FROM appserver_conda_image

USER appserver
WORKDIR /opt/appserver/

RUN git clone https://github.com/rdkit/conda-rdkit.git
WORKDIR /opt/appserver/conda-rdkit

#RUN git checkout development

RUN CONDA_PY=35 conda build boost --quiet --no-anaconda-upload && \
    CONDA_PY=35 conda build cairocffi --quiet --no-anaconda-upload && \
    CONDA_PY=35 conda build rdkit --quiet --no-anaconda-upload && \
    CONDA_PY=35 conda build ncurses --quiet --no-anaconda-upload && \
    CONDA_PY=35 conda build postgresql --quiet --no-anaconda-upload && \
    CONDA_PY=35 conda build rdkit-postgresql --quiet --no-anaconda-upload && \
    CONDA_PY=35 conda build postgresql95 --quiet --no-anaconda-upload && \
    CONDA_PY=35 conda build rdkit-postgresql95 --quiet --no-anaconda-upload && \

    CONDA_NPY=110 conda build rdkit --quiet --no-anaconda-upload &&\
    CONDA_PY=35 CONDA_NPY=110 conda build rdkit --quiet --no-anaconda-upload

COPY docker-entrypoint.sh / 
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]












