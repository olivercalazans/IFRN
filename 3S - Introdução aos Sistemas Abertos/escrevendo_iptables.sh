#!/bin/bash

read -p 'Informe o IP: ' ip

iptables -t nat -A POSTROUTING -s $ip -j MASQUERADE

echo 1 > /proc/sys/net/ipv4/ip_forward

/etc/init.d/networking restart

echo
echo '===================== IPTABLES ====================='
iptables -t nat -nL
echo '===================================================='
echo
