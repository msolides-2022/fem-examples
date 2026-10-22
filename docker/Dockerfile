# Execute from root of repo as: docker buildx build --platform=linux/arm64,linux/amd64 -f docker/Dockerfile ./docker/ --progress=plain

FROM ghcr.io/fenics/dolfinx/lab:v0.11.0
ARG TARGETPLATFORM


ENV DEB_PYTHON_INSTALL_LAYOUT=deb_system
ENV HDF5_MPI="ON"
ENV HDF5_DIR="/usr/local"
ENV PYVISTA_JUPYTER_BACKEND="static"
ENV LIBGL_ALWAYS_SOFTWARE=1

WORKDIR /tmp/
# Requirements for pyvista off-screen rendering (vtk and pyvista come with the base image)
RUN apt-get update && apt-get install -y libgl1-mesa-dev libxrender1 mesa-utils curl

# Upgrade setuptools and pip
RUN python3 -m pip install -U setuptools pip pkgconfig

ADD pyproject.toml /tmp/pyproject.toml
RUN python3 -m pip install --no-cache-dir --no-binary=h5py --no-build-isolation -v .
RUN python3 -m pip cache purge
ENTRYPOINT ["jupyter", "lab", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]
