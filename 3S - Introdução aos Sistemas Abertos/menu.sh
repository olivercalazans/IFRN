#!/bin/bash

sleep_longo=5
sleep_curto=2

while true; do
    clear
    echo "Menu"
    echo "1. Mostrar usuários conectados via ssh"
    echo "2. Mostrar utilização de disco"
    echo "0. Sair"
  
    read -p "Informe a opção desejada: " opcao

    case $opcao in
        "1")
            quantidade_de_usuarios_ssh=0
            IFS=$'\n'
      
            while true; do
                clear
                echo '1. Para mostrar na tela'
                echo '2. Para escrever em um arquivo'
                echo
                read -p '>> ' print_ou_arquivo
                clear

                if [[ $print_ou_arquivo -eq 1 ]]; then
                    echo -e 'Usuários conectados via SSH\n'
                    for linha in `who | grep -v tty`; do
                        echo "Usuário....: $(echo $linha | awk '{print $1}')"
                        echo "Terminal...: $(echo $linha | awk '{print $2}')"
                        echo "Data.......: $(echo $linha | awk '{print $3}') $(echo $linha | awk '{print $4}')"
                        echo "IP.........: $(echo $linha | awk '{print $5}')"
                        echo
                        ((quantidade_de_usuarios_ssh++))
                    done
                        echo -e "Quantidade de usuários via SSH: $quantidade_de_usuarios_ssh\n"
                        sleep $sleep_longo
                        break

                elif [[ $print_ou_arquivo -eq 2 ]]; then
                    nome_do_arquivo=$(date +%Y-%m-%d-%H-%M-%S)
                    echo -e "#### log produzido pelo script menu.sh###\nScript executado em $(date) pelo $(whoami)\n\n" >> $nome_do_arquivo.log

                    for linha in `who | grep -v tty`; do
                        nome=$(echo $linha | awk '{print $1}')
                        terminal=$(echo $linha | awk '{print $2}')
                        data=$(echo $linha | awk '{print $3}')
                        hora=$(echo $linha | awk '{print $4}')
                        ip=$(echo $linha | awk '{print $5}' | cut -d '(' -f2 | cut -d ')' -f1)
                        ((quantidade_de_usuarios_ssh++))

                        echo -e "Usuário....: $nome\nTerminal...: $terminal\nData.......: $data $hora\nIP.........: $ip\n" >> $nome_do_arquivo.log
                    done
                    echo "Quantidade de usuários via SSH: $quantidade_de_usuarios_ssh" >> $nome_do_arquivo.log
                    echo 'Arquivo criado com sucesso!!!'
                    sleep $sleep_curto
                    break

                else
                    echo 'Número invalido. Tente novamente'
                    sleep $sleep_curto

                fi
            done
            ;;
        "2")
            clear
            echo 'Estatistica de uso da partição /'
            echo
            echo "Tamanho Total..: $(df | grep sda1 | awk '{print $2}')"
            echo "Total utilizado: $(df | grep sda1 | awk '{print $5}')"
            sleep $sleep_longo
            ;;
        "0")
            echo -e "\nSaindo..."
            sleep $sleep_curto
            exit
            ;;
        *)
            echo "Opção inválida"
            ;;
    esac
done
clear

