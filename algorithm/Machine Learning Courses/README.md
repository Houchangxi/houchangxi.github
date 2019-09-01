Install env
I have a python3 system, so if you hope to operate GraphLab and SFrame，We need to intall python2.7 that could be build a new env in Anaconda.

1.# Create a new conda environment with Python 2.7.x
conda create -n gl-env python=2.7 anaconda=4.0.0

2.# Activate the conda environment
source activate gl-env

3.# Make sure pip is up to date
conda update pip

4.# Install your licensed copy of GraphLab Create. Need to register on GraphLab.
pip install --upgrade --no-cache-dir https://get.graphlab.com/GraphLab-Create/2.1/your registered email address here/your product key here/GraphLab-Create-License.tar.gz

5.# Install or update IPython and IPython Notebook
conda install ipython-notebook

When you setup your ipython-notebook or jupter notebook, there is a problem that "'ascii' codec can't decode byte 0xe5 in position 4: ordinal not in range(128)"
We need to fix this by 

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 -m pip install jupyter
Please make sure setup jupyter notebook by
LANG=zn jupyter notebook  or  LANG=zn ipython notebook
# 这段用中文解释一下 切记要加 LANG=zn 不然无法启动浏览器

Download the data and sample code and familiarize yourself with the notebooks
Before doing the assignments in this course, familiarize yourself with the two notebooks we covered in the videos:

Download the notebook that covers getting started with Python: Getting started with iPython Notebook.ipynb
Download the notebook that covers getting started with SFrames: Getting Started with SFrames.ipynb
Download the simple people dataset: people-example.csv

After running SFrames.ipynb, you will find out lots of error. Such as:
"AttributeError: 'NoneType' object has no attribute 'add_variable'"
1, pip install tornado==4.5.3
and make sure to resetup jupyter notebook. This is key!  Don't reinstall Anaconda 2.
