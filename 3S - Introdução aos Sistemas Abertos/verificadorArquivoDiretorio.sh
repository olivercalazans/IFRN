#!/bin/bash

read -p 'Informe o caminho: ' caminho

if [ -e $caminho ]; then
	if [ -d $caminho ]; then
		echo 'O diretório existe'
	else
		echo 'O arquivo existe'
	fi
else
	echo 'Diretório ou aruivo inexistente'
fi
