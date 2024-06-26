#!/bin/bash

DOMINIO=$1


### ADICIONANDO UM PONTO (.) CASO NÃO TENHA
if [[ ! $DOMINIO =~ \.$ ]]; then
    DOMINIO="$DOMINIO."
fi


IP='192.168.102.120'

ARQUIVO_DOMINIO="$DOMINIO"zone
CAMINHO_NAMED='/var/projeto-asa/dns/named.conf.projeto'
CAMINHO_ARQUIVOS="/var/projeto-asa/dns/arquivos_de_zona/$ARQUIVO_DOMINIO"


### CRIACAO DO ARQUIVO DE ZONA ---------------------------------

SERIAL=$(date +"%Y%m%d")00
MAIL="mail.$DOMINIO"
FTP="ftp.$DOMINIO"

echo -e '$TTL 30\n'\
"\$ORIGIN $DOMINIO\n"\
"@      IN      SOA     $DOMINIO                admin   (\n"\
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
"$MAIL          IN      A       $IP\n"\
"$FTP           IN      CNAME   @" > $CAMINHO_ARQUIVOS



### CRIACAO DAS CONFIGURACOES DE ZONA --------------------------

echo -e "zone \"$DOMINIO\" IN {\n"\
'       type master;\n'\
"       file \"/var/projeto-asa/dns/arquivos_de_zona/$ARQUIVO_DOMINIO\";\n"\
'       allow-query { any; };\n'\
'};\n' >> $CAMINHO_NAMED



### REINICIANDO BIND
service named restart
