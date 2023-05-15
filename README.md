# EMBL-EBI-imaging-course-05-2023

This repository contains materials for the May 2023 virtual course [Microscopy data analysis: machine learning and the BioImage Archive](https://www.ebi.ac.uk/training/events/microscopy-data-analysis-0/).

Day 4 *Image data resource practical* contains a collection of notebooks with code and text. It also contains the presentation [Image Data Resource: Data Submission and Curation].

Day 5 *Distributed/Cloud computing practical* contains a collection of notebooks with code and text.



## Running the notebooks

### Running on cloud resources

* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ome/EMBL-EBI-imaging-course-05-2023/main)
* [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ome/EMBL-EBI-imaging-course-05-2023/)

### Running in Docker


Alternatively, if you have Docker installed, you can use the [repo2docker](https://repo2docker.readthedocs.io/en/latest/)
tool to run this repository as a local Docker instance:

    $ git clone https://github.com/ome/EMBL-EBI-imaging-course-05-2023
    $ cd EMBL-EBI-imaging-course-05-2023
    $ repo2docker .

Then follow the instructions that are printed after the Docker image is built.


### Running locally

Finally, if you would like to install the necessary requirements locally,
we suggest using conda:

Install Anaconda https://www.anaconda.com/products/individual#Downloads

Then, create the environment:

    $ git clone https://github.com/ome/EMBL-EBI-imaging-course-05-2023
    $ cd EMBL-EBI-imaging-course-05-2023
    $ conda env create -n imaging_course_2023 -f binder/environment.yml

and activate the newly created environment:

    $ conda activate imaging_course_2023

The following steps are only required if you want to run the notebooks

* If you have Anaconda installed:
  * Start Jupyter from the Anaconda-navigator
  * In the conda environment, run ``conda install ipykernel``
  * To register the environment, run ``python -m ipykernel install --user --name imaging_course_2023``
  * Select the notebook you wish to run and select the ``Kernel>Change kernel>Python [conda env:imaging_course_2023]``
  or ``Kernel>Change kernel>imaging_course_2023``
* If Anaconda is not installed:
  * In the environment, install ``jupyter`` e.g. ``pip install jupyter``
  * Add the virtualenv as a jupyter kernel i.e. ``ipython kernel install --name "imaging_course_2023" --user``
  * Open jupyter notebook i.e. ``jupyter notebook`` and select the ``imaging_course_2023`` kernel or ``[conda env:imaging_course_2023]`` according to what is available


An additional benefit of installing the requirements locally is that you
can then use the tools without needing to launch Jupyter itself.
