#!/usr/bin/env bash

printf "\nInstalling dependencies... \n"
python -m pip install django-cors-headers

# Temporarily do this while dependencies are not locked.
# Eventually lock dependencies (use pipfile pipfile.lock)
pip install -r requirements.txt
printf "\nDone\n"