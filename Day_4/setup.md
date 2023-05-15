### Running locally

Finally, if you would like to install the necessary requirements locally,
we suggest using mamba:

* Install Anaconda https://www.anaconda.com/products/individual#Downloads
* In the base environment, run ``conda install -n base conda-forge::mamba``

Then, create the environment:

    $ git clone https://github.com/ome/EMBL-EBI-imaging-course-05-2023
    $ cd EMBL-EBI-imaging-course-05-2023
    $ mamba env create -n imaging_course_day_4_2023 -f Day_4/environment.yml

and activate the newly created environment:

    $ conda activate imaging_course_day_4_2023

The following steps are only required if you want to run the notebooks

* If you have Anaconda installed:
  * Start Jupyter from the Anaconda-navigator
  * In the conda environment, run ``mamba install ipykernel``
  * To register the environment, run ``python -m ipykernel install --user --name imaging_course_day_4_2023``
  * Select the notebook you wish to run and select the ``Kernel>Change kernel>Python [conda env:imaging_course_day_4_2023]`` or ``Kernel>Change kernel>imaging_course_day_4_2023``
* If Anaconda is not installed:
  * In the environment, install ``jupyter`` e.g. ``pip install jupyter``
  * Add the virtualenv as a jupyter kernel i.e. ``ipython kernel install --name "imaging_course_day_4_2023" --user``
  * Open jupyter notebook i.e. ``jupyter notebook`` and select the ``imaging_course_day_4_2023`` kernel or ``[conda env:imaging_course_day_4_2023]`` according to what is available.
