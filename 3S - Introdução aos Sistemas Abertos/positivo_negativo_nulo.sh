#!/bin/bash

read -p 'Informe um número: ' numero

if [ $numero -gt 0 ]; then
	echo "$numero é positivo"
elif [ $numero -lt 0 ]; then
	echo "$numero é negativo"
else
	echo "$numero é nulo"
fi
