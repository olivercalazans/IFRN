#!/bin/bash

IFS=$'\n'

local=$'tty'
ssh=$'pts'

usuarios_ssh=0
usuarios_local=0

for linha in `who`; do
  if [[ ${linha} == *${local}* ]]; then
    usuarios_local=$((usuarios_local + 1))
  elif [[ ${linha} == *${ssh}* ]]; then
    usuarios_ssh=$((usuarios_ssh + 1))
  fi
done

nome_do_arquivo=$(date +%Y-%m-%d-%H-%M-%S)

echo "#### log produzido pelo script userinfo_v3.sh###
Script executado em $(date) pelo usuário root

Total de usuários conectados localmente...: $usuarios_local
Total de usuários conectados via ssh......: $usuarios_ssh

Estatistica de uso da partição /
  Tamanho Total..: $(df | grep sda1 | awk '{print $2}')
  Total utilizado: $(df | grep sda1 | awk '{print $5}')" > nome_do_arquivo.log
