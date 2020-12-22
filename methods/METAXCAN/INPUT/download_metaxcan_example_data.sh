#!/bin/bash
fileid="1akRXhGhwc97FgMolN1wUMiivwTiJxiH5"
filename="metaxcan_example_data.tar.gz"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
tar -xvzf metaxcan_example_data.tar.gz
rm -r metaxcan_example_data.tar.gz
