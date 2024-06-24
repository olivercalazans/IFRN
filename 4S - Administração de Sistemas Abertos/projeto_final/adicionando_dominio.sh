#!/bin/bash

DOMINIO=$1

SERIAL=$(date +"%Y%m%d")00
IP='192.168.102.120'
MAIL="mail.$DOMINIO"
ARQUIVO_DE_ZONA="$DOMINIO.zone"

CAMINHO_NAMED='/var/projeto-asa/dns/named.asa.zones'
CAMINHO_ARQUIVOS="/var/projeto-asa/dns/arquivos_de_zona/$ARQUIVO_DE_ZONA"


### CRIACAO DO ARQUIVO DE ZONA ---------------------------------

echo -e '$TTL 30\n'\
"\$ORIGIN local.\n"\
"@      IN      SOA     $DOMINIO        admin   (\n"\
"               $SERIAL\n"\
'               2M\n'\
'               1M\n'\
'               5M\n'\
'               30      )\n'\
'\n'\
"               IN      A       $IP\n"\
"               IN      NS      $DOMINIO\n"\
"               IN      MX  5   $MAIL\n"\
'\n'\
"$MAIL          IN      A       $IP\n"\ > $CAMINHO_ARQUIVOS



### CRIACAO DAS CONFIGURACOES DE ZONA --------------------------

echo -e "zone \"$DOMINIO.local\" IN {\n"\
'       type master;\n'\
"       file \"$/var/projeto-asa/dns/arquivos_de_zona/$ARQUIVO_DE_ZONA\";\n"\
'       allow-query { any; };\n'\
'};\n' >> $CAMINHO_NAMED



### REINICIANDO BIND
# service named restart
