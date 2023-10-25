#!/bin/bash

read -p 'Nome do arquivo: ' nomeArquivo

if [ -e $HOME/$nomeArquivo ]; then
	echo "O arquivo $nomeArquivo já existe"
else
	touch $HOME/$nomeArquivo
	chmod 711 $HOME/$nomeArquivo
	echo "Arquivo $nomeArquivo criado no seu diretório home"
fi


