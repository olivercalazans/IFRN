#!/bin/bash

echo "Digite um número"
read num 

if [ "$num" -gt 0 ]; then
    echo "O número é positívo."
elif [ "$num" -lt 0 ]; then
    echo "O número é negatívo"
else
    echo "O número é nulo"
fi