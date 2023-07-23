#
# Virtualenv ('venv') is a very useful python feature. A
# 'virtual environment' is an isolated environment for pip.
# Installing (or removing) packages in the virtual
# environment does not affect installed packages in the
# parent (non-virtual) environment.
#

#
# To Install virtualenv for your python distribution on
# linux, type: sudo apt-get install python3.10-venv.
# On Windows using IDLE, type: py -m pip install --user
# virtualenv.
#

#
# To create and enter a virtual environment on Linux, use
# venv as follows:
#

$ python3 -m venv ./virtual_environment/

$ source ./virtual_environment/bin/activate

#
# On Windows, using Powershell:
#

.\virtual_environment\Scripts\Activate.ps1

#
# Installing packages in the virtual environment does not
# affect installed packages in the parent (non-virtual)
# environment. Use pip in the virtual environment as
# follows:
#

$ pip install (package_name)

#
# Typing 'which python' will show that the python
# interpreter for the virtual environment is a member of
# ./virtual_environment, not the system directories:
#

$ which python

#
# To exit the virtual environment, type 'deactivate':
#

$ deactivate

#
# To create a requirements file from python scripts in the
# current directory, install and use pipreqs as follows:
#

$ pip install pipreqs

$ pipreqs .

#
# To load the requirements file (install the packages it
# contains):
#

$ pip install -r ./requirements.txt

#
# A virtual environment for python can also be created using
# conda (https://docs.conda.io/en/latest/).
#
