FROM markussitzmann/appserver_rdkit:1

#USER root
#WORKDIR /

COPY requirements.txt /

#RUN conda install --use-local --yes --quiet python rdkit
RUN CONDA_PY=35 pip install -r /requirements.txt












