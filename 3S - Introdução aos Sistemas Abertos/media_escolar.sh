#!/bin/bash

read -p 'Quantas notas serão informadas? ' quantidadeNotas

notas=0
for (( i = 1; i <= quantidadeNotas; i++ )); do
    read -p "Informe a $i° nota: " notaInformada
    notas= $((notas + notaInformada))
done

media=$((notas / quantidadeNotas))

if [ $media -ge 7 ]; then
    echo "Nota: $media, Aprovado"
elif [ $media -ge 2 ]; then
    echo "Nota: $media, Recuperação"
else
    echo "Nota: $media, Reprovado"
fi