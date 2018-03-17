#!/bin/bash
# This installer must only be run in this directory. 
./installdeps.sh &
pip install -e ./src
