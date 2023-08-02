#!/bin/bash

nome_arquivo=$(ls -t | head -n 1)

if [ -w "nome_arquivo" ]; then
    echo "Digite o conteúdo do arquivo"
    read conteudo
    echo "$conteudo" >> "$nome_arquivo"
    echo "Conteudo adicionado"
else
    echo "O arquivo não tem permisão de escrita"
fi