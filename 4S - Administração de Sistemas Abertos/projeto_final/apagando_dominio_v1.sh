#!/bin/bash

DOMINIO=$1


### APAGANDO ARQUIVO DE ZONA

CAMINHO_ARQUIVOS_ZONA='/var/projeto-asa/dns/arquivos_de_zona/'

rm "$CAMINHO_ARQUIVOS_ZONA$DOMINIO.zone"



### APAGANDO CONFIGURACOES DE ZONA

LINHA_INICIAL=$(grep -n "$DOMINIO" /var/projeto-asa/dns/named.asa.zones  | awk -F':' '{print $1}' | head -n 1)
LINHA_FINAL=$(( LINHA_INICIAL + 5 ))

LINHAS="$LINHA_INICIAL,$LINHA_FINAL"d

sed "$LINHAS" /var/projeto-asa/dns/named.asa.zones > temp && mv temp /var/projeto-asa/dns/named.asa.zones



### REINICIANDO BIND
# service named restart
