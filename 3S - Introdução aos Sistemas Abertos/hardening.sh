#!/bin/bash

IFS=$'\n'

hora_do_inicio_da_execucao=$(date)
arquivo_de_log='scanner.log'
echo "===== Procedimento de hardening executado $(date) =====" >> $arquivo_de_log


# A) atualizando o sistema. ----------------------------------
echo 'Atualizando sistema...' | tee -a $arquivo_de_log

if (apt-get update && apt-get upgrade -y) > /dev/null 2>> $arquivo_de_log ; then
	echo '    -> Atualização concluída' | tee -a $arquivo_de_log
else
	echo '    -> Erro ao atualizar o sistema' | tee -a $arquivo_de_log
fi


# B) Habilitando o NTP(Network Time Protocol) -----------------
echo 'Configurando NTP...' | tee -a $arquivo_de_log
apt-get install ntp &>/dev/null 2>>$arquivo_de_log

echo 'Agendando sincronização' | tee -a $arquivo_de_log
sincronizacao_encontrada='false'
for linha in `crontab -l`; do
	if [[ $linha == '0 1 * * * /etc/init.d/ntp restart' ]]; then
		echo '    -> A sincronização já foi agendada' | tee -a $arquivo_de_log
		sincronizacao_encontrada='true'
		break
	fi
done

if [[ $sincronizacao_encontrada == 'false' ]]; then
	(crontab -l 2> /dev/null; echo "0 1 * * * /etc/init.d/ntp restart") | crontab -
	echo '    -> Sincronização agendada com sucesso' | tee -a $arquivo_de_log
fi

echo 'Concluído' | tee -a $arquivo_de_log


# C) Reboot automático depois de um Kernel Panic
echo 'Configurando reboot automático depois do Kernel Panic'| tee -a $arquivo_de_log

reboot_automatico=false
for linha in `cat /etc/sysctl.conf`; do
	if [[ $linha == "kernel.panic=30" ]]; then
		reboot_automatico=true
		echo '    -> Reboot automático após 30 já configurado' | tee -a $arquivo_de_log
		break
	fi
done

if [[ $reboot_automatico == false ]]; then
	echo 'kernel.panic=30' >> /etc/sysctl.conf
	sysctl -p
	echo '    -> Reboot automático configurado' | tee -a $arquivo_de_log
fi


# D) Removendo programas indesejados/maliciosos
echo 'Removendo programas indesejados/maliciosos' | tee -a $arquivo_de_log

caminho_do_arquivo_de_programas=$(find / -name programas.txt)
for programa in `cat $caminho_do_arquivo_de_programas`; do
	if [ -f $programa ]; then
		echo "    -> Programa encontrado: $programa" | tee -a $arquivo_de_log
		echo "          -> Removendo programa..." | tee -a $arquivo_de_log
		apt-get remove $programa &>/dev/null
	fi
done

echo "Removendo permissões do arquivo 'programas.txt'" | tee -a $arquivo_de_log
chmod 000 $caminho_do_arquivo_de_programas


# E) Desabilitando shell de usuários indesejados
echo 'Desabilitando shell de usuários indesejados' | tee -a $arquivo_de_log

arquivo_de_usuarios=$(find / -name usuarios.txt)

for linha in `cat $arquivo_de_usuarios`; do
        usuario=$(echo $linha | cut -d ':' -f1)
        if  id $usuario &>/dev/null 2>/dev/null; then
                echo "    -> Usuário encontrado: $usuario" | tee -a $arquivo_de_log
		echo '          -> Impedindo login do usuário encontrado...' | tee -a $arquivo_de_log
		usermod -s /usr/sbin/nologin $usuario
        fi
done


# F) Informações passadas ao arquivo "scanner.log" já foram feitas durante a execução de cada parte.


# *SSS) Agendando execução desse script
echo "Agendando execução desse script..." | tee -a $arquivo_de_log
execucao_agendada='false'
caminho_para_hardening=$(find / -name hardening.sh)
for linha in `crontab -l`; do
        if [[ $linha == "0 2 * * * $caminho_para_hardening" ]]; then
                echo '    -> A execução já foi agendada' | tee -a $arquivo_de_log
                execucao_agendada='true'
                break
        fi
done

if [[ $execucao_agendada == 'false' ]]; then
        (crontab -l 2> /dev/null; echo "0 2 * * * $caminho_para_hardening") | crontab -
        echo '    -> Execução agendada com sucesso' | tee -a $arquivo_de_log
fi


# G) Informações do sistema
hora_final_da_execucao=$(date)
echo "Nome e versão.....: $(lsb_release -a 2>/dev/null | grep 'Description' | cut -d '	' '-f2-')" | tee -a $arquivo_de_log
echo "Versão do Kernel..: $(uname -r)" | tee -a $arquivo_de_log
echo "Início da execução: $hora_do_inicio_da_execucao" | tee -a $arquivo_de_log
echo "Fim da execução...: $hora_final_da_execucao" | tee -a $arquivo_de_log
echo -e '============================================================================' | tee -a $arquivo_de_log
