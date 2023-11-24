#!/bin/bash

read -p '1° número: ' primeiro
read -p '2° número: ' segundo

if [ $primeiro -gt $segundo ]; then
	echo "$primeiro é maior que $segundo"
elif [ $primeiro -lt $segundo ]; then
	echo "$segundo é maior que $primeiro"
else
	echo "$primeiro é igual a $segundo"
fi
