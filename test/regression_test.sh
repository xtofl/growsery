#!/bin/bash
cd $(dirname $0)

python3 ../python/growser.py > current.list.txt
diff current.list.txt reference.list.txt

