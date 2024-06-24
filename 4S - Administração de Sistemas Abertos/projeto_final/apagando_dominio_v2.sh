#!/bin/bash

DOMINIO=$1


### ADICIONANDO UM PONTO (.) CASO NÃO TENHA
if [[ ! $DOMINIO =~ \.$ ]]; then
    DOMINIO="$DOMINIO."
fi


### APAGANDO ARQUIVO DE ZONA

CAMINHO_ARQUIVOS_ZONA='/var/projeto-asa/dns/arquivos_de_zona/'

rm "$CAMINHO_ARQUIVOS_ZONA$DOMINIO"zone



### APAGANDO CONFIGURACOES DE ZONA

LINHA_INICIAL=$(grep -n "$DOMINIO" /var/projeto-asa/dns/named.conf.projeto  | awk -F':' '{print $1}' | head -n 1)
LINHA_FINAL=$(( LINHA_INICIAL + 5 ))

LINHAS="$LINHA_INICIAL,$LINHA_FINAL"d

sed "$LINHAS" /var/projeto-asa/dns/named.conf.projeto > temp && mv temp /var/projeto-asa/dns/named.conf.projeto



### REINICIANDO BIND
service named restart
