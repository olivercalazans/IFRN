#!/bin/bash

IFS=$'\n'

echo 

for linha in `who | grep -v tty`; do
  nome=$(echo $linha | awk '{print $1}')
  terminal=$(echo $linha | awk '{print $2}')
  data=$(echo $linha | awk '{print $3}')
  hora=$(echo $linha | awk '{print $4}')
  ip=$(echo $linha | awk '{print $5}' | cut -d '(' -f2 | cut -d ')' -f1)

  echo "Usuário....: $nome"
  echo "Terminal...: $terminal"
  echo "Data.......: $data $hora"
  echo "IP.........: $ip"
  echo
done
