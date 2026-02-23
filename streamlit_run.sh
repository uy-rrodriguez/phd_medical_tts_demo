#!/bin/bash
#
# Script to install the environment and launch the streamlit app
# in standalone machines.
#
# Usage:
#   bash streamlit_run.sh
#

python_ver=$(python --version 2>/dev/null)
if [ "$python_ver" == "" ]; then
    echo "Python 3.10+ will be installed to run this app"
    sudo apt install python=3.10.16
else
    echo "You are running Python version $python_ver"
fi

pip_ver=$(pip --version 2>/dev/null)
if [ "$pip_ver" == "" ]; then
    echo "Pip will be installed to run this app"
    sudo apt install pip
else
    echo "You are running Pip version $pip_ver"
fi

# Check for Conda installation
conda_ver=$(conda --version 2>/dev/null)
if [ "$conda_ver" == "" ]; then
    echo "Conda is not installed, Streamlit will be loaded from a Python venv"

    if [ ! -d "venv" ]; then
        echo "Creating new environment in 'venv'"
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
    fi

    if [ "$(streamlit --version 2>/dev/null)" == "" ]; then
        source venv/bin/activate
    fi
else
    echo "You are running Conda version $conda_ver, environment $CONDA_DEFAULT_ENV"

    if [ "$(streamlit --version 2>/dev/null)" == "" ]; then
        echo "Streamlit was not found in the active Conda environment, please update the environment and retry"
    fi
fi

st_ver=$(streamlit --version 2>/dev/null)
echo "Your are running Streamlit version $st_ver"

streamlit run apps/st_cv_demo/main.py \
    --browser.gatherUsageStats=false \
    --global.developmentMode=false \
    --server.headless=true
