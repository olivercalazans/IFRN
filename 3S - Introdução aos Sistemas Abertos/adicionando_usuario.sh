#!/bin/bash

read -p 'Digite o nome do novo usuário: ' nomeDoUsuario

useradd -m -s /bin/bash "$nomeDoUsuario"

sudo passwd -d "$nomeDoUsuario"
