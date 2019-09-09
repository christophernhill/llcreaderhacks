FROM centos:latest

USER root

RUN ( cd /tmp; curl -O https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh )
RUN ( yum -y install bzip2 )
RUN ( mkdir /root/anaconda3 )
RUN ( cd /tmp; bash  Anaconda3-2019.07-Linux-x86_64.sh -b -u )
RUN /root/anaconda3/bin/conda init
RUN cat /root/.bashrc
RUN ["/bin/bash", "-c", ". /root/.bashrc && conda install xarray dask"]
RUN ["/bin/bash", "-c", ". /root/.bashrc && conda install -c conda-forge xmitgcm"]
RUN ["/bin/bash", "-c", ". /root/.bashrc && conda install fsspec"]
RUN ["/bin/bash", "-c", ". /root/.bashrc && conda install zarr"]

COPY example1.py /root

CMD ["/bin/bash"]
