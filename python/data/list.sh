#!/bin/sh

here=$(cd $(dirname $0) && pwd)
cd $here
PYTHONPATH=. ../src/growsery/growser.py
