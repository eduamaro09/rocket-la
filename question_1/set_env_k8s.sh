#/bin/bash

hostUrl=https://gist.githubusercontent.com/
hostUri="ChrisChinchilla/ada88ea93b3660f69351f632ddd0bf05/raw/2badd1a7f88b201a7229b6478f04ab474bd2284c/postgres-config.yml"
filename=postgress.yml
echo "Inicia descarga de manifiesto yml k8s"
sleep 2
curl -o ./postgress.yml -k $hostUrl$hostUri
echo "Se inicia obtención de valores sobre el arreglo"
while read assign
do export "$assign";  done < <(sed -nr '/data/,$ s/  ([A-Z_]+): (.*)/\1=\2/ p' $filename)
sleep 2
echo "evidencia de printenv"
printenv
