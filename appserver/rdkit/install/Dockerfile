FROM markussitzmann/appserver_conda:1

USER appserver
WORKDIR /opt/appserver/

#RUN git clone https://github.com/markussitzmann/conda-rdkit.git
RUN git clone https://github.com/rdkit/conda-rdkit.git
WORKDIR /opt/appserver/conda-rdkit

#RUN git checkout origin/development

RUN CONDA_PY=35 conda install -c rdkit rdkit-postgresql95 postgresql95
RUN CONDA_PY=35 conda create -c rdkit --name appserver python rdkit rdkit-postgresql95 postgresql95

#RUN CONDA_PY=35 conda create -c rdkit --yes --name appserver python rdkit rdkit-postgresql95 postgresql95


COPY docker-entrypoint.sh / 
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]












