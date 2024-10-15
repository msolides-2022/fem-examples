# Solid Mechanics: numerical examples

This repository collects example of finite element solvers used in Solid Mechanics Master of [Sorbonne Université](http://master.spi.sorbonne-universite.fr/fr/mecanique-des-solides-et-des-structures.html),

* Teachers:
    * Corrado Maurini (corrado.maurini@sorbonne-universite.fr) 

* We will use for this numerical tutorials the python finite element package `FEniCS/dolfinx` (version `0.9.0`). 

* You can find some links to online resources in the file [LINKS.md](LINKS.md)

You can run interactively the notebooks of this tutorial on Binder, by clicking here:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/msolides-2022/fem-examples/HEAD
)

## Local installation 

### Docker

1. First, install docker for your operating system. You can find instructions here: https://docs.docker.com/get-docker/

2. Download and unzip the present repository. If you have git installed, you can clone the repository with `git clone 
https://github.com/msolides-2022/fem-examples.git`.  
Otherwise download and unzip the file  `https://github.com/msolides-2022/fem-examples.git/archive/refs/heads/main.zip`. 

3. To build a docker image for this documentation, you can run from the root of the downloaded repository (use the `PowerShell` if you are on Windows)

```
docker build -t fenicsx-mmc -f docker/Dockerfile .
```

4. To create a one-time usage container you can call:

```
docker run --rm -ti -v $(pwd):/root/shared -w /root/shared  --init -p 8888:8888 fenicsx-mmc
```

*Note:* On Windows, you may need to replace `$(pwd)$` with `${PWD}` or `%cd%` in the line above, depending on the type of your terminal.

You can then access the jupyter lab notebook opening in your browser one of the links starting with `http://...` indicated in the terminal.

Steps 1-3 need to be done only the first time. After, you can then start the container with the command in step 4 directly.

### Conda

To run the notebooks locally, we recommend to use the conda environment provided in this repository. To install conda, please follow the instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).

To create the conda environment and activate it

```bash
conda env create -f fenicsx-mmc.yml
conda activate fenicsx-fracture
```