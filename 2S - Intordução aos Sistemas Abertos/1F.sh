#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Só o root pode criar novos usuários"
else
    echo "Informe o nome de usuário"
    read nome

    if grep -q "^$nome:" /etc/paswd; then
        echo "Esse usuário já existe"
    else
        useradd -m -s /bin/bash -c "$nome"
        echo "$nome:" | chpasswd -e
        echo "Usuário criado com sucesso!!!"
    fi
fi
