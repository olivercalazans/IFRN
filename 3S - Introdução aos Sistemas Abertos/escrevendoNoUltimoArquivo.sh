#!/bin/bash

ultimoArquivo=$(ls -t $HOME | head -n 1)

if [ -w $HOME/$ultimoArquivo ]; then
	read -p ">" texto
	echo $texto >> $HOME/$ultimoArquivo
	echo "Texto adicionado a $HOME/$ultimoArquivo"
else
	echo "O arquivo $ultimoArquivo não tem permissão de escrita"
fi
