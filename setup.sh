#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

wget -r https://processing.org

python replace.py

echo "if you are using vim-processing, make sure you add"
echo "g:processing_doc_stype='local'"
echo "and"
echo "g:processing_doc_path=''"
