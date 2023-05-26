## Running the notebooks

### Running on cloud resources
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ome/EMBL-EBI-imaging-course-05-2023/)


### Running locally

Finally, if you would like to install the necessary requirements locally,
we suggest using Mamba:

* If you do not have any pre-existing conda installation, [install Mamba](https://mamba.readthedocs.io/en/latest/installation.html#installation) and use [mambaforge](https://github.com/conda-forge/miniforge#mambaforge). 
* In case you have a pre-existing conda installation, you can install Mamba by either:
  - Using the recommended way to install Mamba from [mambaforge](https://github.com/conda-forge/miniforge#mambaforge). This will not invalidate your conda installation, but possibly your pre-existing conda envs will be in a different location (e.g. ``/Users/USER_NAME/opt/anaconda3/envs/``) then the new mamba envs (e.g. ``/Users/USER_NAME/mambaforge/envs/``). You can verify this by running ``conda env list``. The addition of ``export CONDA_ENVS_PATH=/Users/user/opt/anaconda3/envs/`` into your ``.bashprofile`` or ``.zprofile`` file will fix this. 
  - Use the [Existing conda install](https://mamba.readthedocs.io/en/latest/installation.html#existing-conda-install) way, i.e. run ``conda install mamba -n base -c conda-forge`` whilst in the base environment. This way can take much longer time than the recommended way described above, and might not lead to a successful installation, especially if run on arm64 (Apple Silicon) OS X.

To avoid conflict with used packages, we have prepared several environments:
``Day_5/environment.yml``, ``Day_5/environment_conversion.yml``, ``Day_5/environment_minio.yml`` and ``Day_5/environment_cp.yml``.

Create the environments. For this, first run the commands below as written, then replace ``Day_5/environment_conversion.yml`` motives with ``Day_5/environment.yml``, ``Day_5/environment_cp.yml`` or ``Day_5/environment_minio.yml``  and run again to create the other envs. Note that unlike on Day_4, the Cellpose on Day_5 is included in the ``Day_5/environment.yml``:

For Windows, OS X x86_64 (NOT arm64 Apple Silicon), Linux:

    $ git clone https://github.com/ome/EMBL-EBI-imaging-course-05-2023
    
    $ cd EMBL-EBI-imaging-course-05-2023

    $ mamba env create -f Day_5/environment_conversion.yml

For OS X arm64 Apple Silicon

    $ git clone https://github.com/ome/EMBL-EBI-imaging-course-05-2023   
    
    $ cd EMBL-EBI-imaging-course-05-2023
    
    $ CONDA_SUBDIR=osx-64 mamba env create -f Day_5/environment_conversion.yml

and activate the newly created environment:

    $ conda activate imaging_course_conversion_day5_2023

Before creating a new environment, remember to deactivate the current one:

    $ conda deactivate

See also [Conda command reference](https://docs.conda.io/projects/conda/en/latest/commands.html).

The following steps are only required if you want to run the notebooks.

* If you have Anaconda installed:
  * Start Jupyter from the Anaconda-navigator
  * In the conda environment, run ``mamba install ipykernel``  (for OS X Apple Silicon ``CONDA_SUBDIR=osx-64 mamba install ipykernel``)
  * To register the environment, run ``python -m ipykernel install --user --name imaging_course_conversion_day5_2023``
  * Select the notebook you wish to run and select the ``Kernel>Change kernel>Python [conda env:imaging_course_conversion_day5_2023]`` or ``Kernel>Change kernel>imaging_course_conversion_day5_2023``
* If Anaconda is not installed:
  * In the environment, install ``jupyter`` e.g. ``pip install jupyter``
  * Add the virtualenv as a jupyter kernel i.e. ``ipython kernel install --name "imaging_course_conversion_day5_2023" --user``
  * Open jupyter notebook i.e. ``jupyter notebook`` and select the ``imaging_course_conversion_day5_2023`` kernel or ``[conda env:imaging_course_conversion_day5_2023]`` according to what is available.

To stop the notebook server, in the terminal where te server is running, press ``Ctrl C``. The following question will be asked in the terminal ``Shutdown this notebook server (y/[n])?``. Enter the desired choice.
  