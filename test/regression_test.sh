#!/bin/bash
cd $(dirname $0)

python ../python/growser.py > current.list.txt
diff current.list.txt reference.list.txt

