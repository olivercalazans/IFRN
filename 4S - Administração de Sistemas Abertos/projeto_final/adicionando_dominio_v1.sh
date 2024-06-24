#!/bin/bash

DOMINIO=$1

IP='192.168.102.120'
ARQUIVO_DE_ZONA="$DOMINIO.zone"

CAMINHO_NAMED='/var/projeto-asa/dns/named.asa.zones'
CAMINHO_ARQUIVOS="/var/projeto-asa/dns/arquivos_de_zona/$ARQUIVO_DE_ZONA"


### CRIACAO DO ARQUIVO DE ZONA ---------------------------------

NS="$DOMINIO.local."
SERIAL=$(date +"%Y%m%d")00
MAIL="mail.$NS"
FTP="ftp.$NS"

echo -e '$TTL 30\n'\
"\$ORIGIN $NS\n"\
"@      IN      SOA     $NS             admin   (\n"\
"               $SERIAL\n"\
'               2M\n'\
'               1M\n'\
'               5M\n'\
'               30      )\n'\
'\n'\
"               IN      A       $IP\n"\
"               IN      NS      $NS\n"\
"               IN      MX  5   $MAIL\n"\
'\n'\
"$MAIL          IN      A       $IP\n"\
"$FTP           IN      CNAME   @" > $CAMINHO_ARQUIVOS



### CRIACAO DAS CONFIGURACOES DE ZONA --------------------------

echo -e "zone \"$DOMINIO.local\" IN {\n"\
'       type master;\n'\
"       file \"/var/projeto-asa/dns/arquivos_de_zona/$ARQUIVO_DE_ZONA\";\n"\
'       allow-query { any; };\n'\
'};\n' >> $CAMINHO_NAMED



### REINICIANDO BIND
service named restart
