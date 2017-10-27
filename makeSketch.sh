#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sketchName=$1

cp -rf $DIR/emptySketch ~/code/$sketchName && mv ~/code/$sketchName/emptySketch.pde ~/code/$sketchName/$sketchName.pde
