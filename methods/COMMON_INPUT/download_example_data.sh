#!/bin/bash
fileid="15S2vuhv55tUyLFxb4fGtwDP88ry9-FpS"
filename="common_input.tar.gz"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
tar -xvzf common_input.tar.gz
rm -r common_input.tar.gz
