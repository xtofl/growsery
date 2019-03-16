#!/bin/sh

here=$(cd $(dirname $0) && pwd)
cd $here
PYTHONPATH=../src python3 -m shopping_list --pantry pantry.txt --shop shop.txt > lijst.txt
cat lijst.txt