#!/bin/bash

if [ -d "venv" ]; then
    echo "Create virtualenv with python3.4"
    rm -rf venv
fi

pyvenv-3.4 --without-pip venv 
source ./venv/bin/activate 
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-3.4.4.tar.gz 
tar -vzxf setuptools-3.4.4.tar.gz 
cd setuptools-3.4.4 
python setup.py install 
cd .. 
wget https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz 
tar -vzxf pip-1.5.6.tar.gz 
cd pip-1.5.6 
python setup.py install 
cd .. 

echo "Install pip requirements"
pip install -r requirements.txt

deactivate

rm -rf pip-1.5.6.tar.gz
rm -rf pip-1.5.6
rm -rf setuptools-3.4.4
rm -rf setuptools-3.4.4.tar.gz


