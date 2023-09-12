#!/bin/bash

read -p 'Informe o número de votos válidos: ' votosValidos
read -p 'Informe o número de votos em branco: ' votosBrancos
read -p 'Informe o número de votos nulos: ' votosNulos

votosTotal=$((votosValidos + votosBrancos + votosNulos))

validosPorcentagem=$(echo "scale=2; ($votosValidos * 100) / $votosTotal" | bc -l )
brancosPorcentagem=$(echo "scale=2; ($votosBrancos * 100) / $votosTotal" | bc -l )
nulosPorcentagem=$(echo "scale=2; ($votosNulos * 100) / $votosTotal" | bc -l )

echo "Total de votos .....$votosTotal/100%"
echo "Votos válidos/% ....$votosValidos/$validosPorcentagem%"
echo "Votos em branco/%...$votosBrancos/$brancosPorcentagem%"
echo "Votos nulos/% ......$votosNulos/$nulosPorcentagem%"