!/bin/bash

read -p 'Informe o nome do usuário: ' nomeDoUsuario

if id "$nomeDoUsuario" &>/dev/null; then
        echo -e '\nO usuário está logado'
        who | grep "$nomeDoUsuario"
        echo
        echo "NAME     LINE         TIME"
        who
        numeroDeUsuarios=$(who | wc -l)
        echo -e "\nUsers = $numeroDeUsuarios"
else
        echo 'Usuário inexistente'
fi
