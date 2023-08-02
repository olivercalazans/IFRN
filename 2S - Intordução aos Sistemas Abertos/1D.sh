#!/bin/bash

echo "Informe o nome do arquivo"
read nome_arquivo

caminho="$HOME/$nome_arquivo"

if [ -e "$caminho" ]; then
    echo "Esse nome já existe"
else
    touch "$nome_arquivo"
    chmod 444 "$nome_arquivo"
    echo "Arquivo criado com sucesso"
fi
