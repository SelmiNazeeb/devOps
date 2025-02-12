#!/bin/bash
#author : selmi
set -x

venv_Path="C:\Users\Administrator\notes\devOps\005_ShellScripting\selmienv"
echo $venv_Path
if [ ! -d $venv_Path ]; then
    python -m venv "$venv_Path"
    echo " environment created"
else
    echo "error"
fi


source "$venv_Path\Scripts\activate"
echo "environment activated"

pip install flask

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

python apps.py





