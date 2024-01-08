#!/bin/bash

IFS=$'\n'

echo 'Atualizando sistema e instalando o net-tools'
if (apt-get update && apt-get install -y net-tools) >/dev/null 2>/dev/null; then
	echo '[ OK ] NET-TOOLS'
else
	echo '[ ERROR ] NET-TOOLS '
fi

echo
echo '### INFORMAÇÕES DAS INTERFACES DE REDE ###'
for interface in `netstat -i | awk '{print $1}' | sed '1,2d'`;do
	linha_do_ipv4=$(ifconfig $interface | grep inet)
	ip=$(echo $linha_do_ipv4 | awk '{print $2}')
	netmask=$(echo $linha_do_ipv4 | awk '{print $4}')
	gateway=$(route | grep "$netmask.*$interface" | awk '{print $2}')

	echo "Interface: $interface"
	echo "IP.......: $ip"
	echo "Netmask..: $netmask"
	echo "Gateway..: $gateway"
	echo
done

echo
echo ' ### INFORMAÇÕES DO SSH'
for ssh in `netstat -nlpt | grep tcp`; do
	echo "program name: $(echo $ssh | awk '{print $7}' | cut -d '/' -f2 | cut -d ':' -f1)"
	echo "Port........: $(echo $ssh | awk '{print $4}' | sed 's/.*[:]\+//')"
	echo "State.......: $(echo $ssh | awk '{print $6}')"
	echo "PID.........: $(echo $ssh | awk '{print $7}' | cut -d '/' -f1)"
	echo
done

echo
echo ' ### TESTANDO A CONECTIVIDADE COM A INTERNET ###'

if ping -c 4 8.8.8.8 &>/dev/null 2>/dev/null; then
        echo 'Conectado a internet'
else
        echo 'Não conectado a internet'
fi

