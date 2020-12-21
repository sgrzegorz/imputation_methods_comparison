#!/bin/bash
fileid="1qTU90yhlsVphiWK2u3ey6KXHIio1kR5J"
filename="helpme.tar.gz"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
tar -xvzf helpme.tar.gz
rm -r helpme.tar.gz
