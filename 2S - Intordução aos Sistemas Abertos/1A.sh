#!/bin/bash

echo "Primeiro número"
read num1
echo "Segundo número"
read num2

if [ "$num1" - eq "$num2"]; then
    echo "Os números são iguais."
elif [ "$num1" -gt "$num2" ]; then
    echo "o número $num1 é maior."
else
    echo "O número $num2 é maior"
fi