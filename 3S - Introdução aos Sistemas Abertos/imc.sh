#!/bin/bash

read -p 'Informe o peso: ' peso
read -p 'Informe a altura: ' altura

imc=$(echo "scale=2; $peso / ($altura * $altura)" | bc -l )

if (( $(echo "$imc >= 40.0" | bc -l) )); then
    echo "IMC: $imc, Obesidade grau III"
elif (( $(echo "$imc >= 35.0" | bc -l) )); then
    echo "IMC: $imc, Obesidade grau II"
elif (( $(echo "$imc >= 30.0" | bc -l) )); then
    echo "IMC: $imc, Obesidade grau I"
elif (( $(echo "$imc >= 25.0" | bc -l) )); then
    echo "IMC: $imc, Excesso de peso"
elif (( $(echo "$imc >= 18.5" | bc -l) )); then
    echo "IMC: $imc, Peso normal"
else
    echo "IMC: $imc, Abaixo do peso normal"
fi