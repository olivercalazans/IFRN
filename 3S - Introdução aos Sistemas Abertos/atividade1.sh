#!bin/bash

echo 'A)'
mkdir -v ~/trabalho

echo 'B)'
cd ~/trabalho ; pwd
mkdir -v projetos

echo 'C)'
mkdir -v ~/pessoal

echo 'D)'
cd ../pessoal ; pwd
mkdir -v ~/pessoal/fotos

echo 'E)'
pwd ; mkdir -v ../trabalho/projetos/documentos

echo 'F)'
mkdir -v ~/trabalho/projetos/documentos/backup

echo 'G)'
pwd ; mkdir -v ../trabalho/projetos/documentos/backup/2022

echo 'H)'
pwd ; mkdir -v ../estudos

echo 'I)'
mkdir -vp ~/estudos/ifrn/2023/isa

echo 'J)'
pwd ; mkdir -v fotos/antigas

echo 'K)'
touch ~/foto{1..2}.jpg ; echo '"foto1.jpg" e "foto2.jpg" criadas'

echo 'L)'
mv -v ~/foto1.jpg ~/pessoal/fotos/antigas/foto1-2021.jpg

echo 'M)'
pwd ; mv ~/foto2.jpg fotos/antigas/foto2-2022.jpg

echo 'N)'
touch ~/linux.doc ~/comandos.txt ; echo '"linux.doc" e "comandos.txt" criados'

echo 'O)'
cd ~ ; pwd
mv -v linux.doc trabalho/projetos/documentos/

echo 'P)'
mv -v comandos.txt trabalho/projetos/documentos/backup/

echo 'Q)'
pwd ; mv -v trabalho/projetos/documentos pessoal

echo 'R)'
pwd ; mv -v pessoal/fotos trabalho/projetos/

echo 'S)'
mv -v ~/trabalho/projetos ~/

echo 'T)'
mv -v ~/pessoal/documentos/backup ~/pessoal

echo 'U)'
mv -v pessoal /tmp/pessoal-$USER

echo 'V)'
pwd ; mv -v /tmp/pessoal-$USER/documentos .

echo 'W)'
rm -v projetos/fotos/antigas/*.jpg

echo 'X)'
rm -vr /tmp/pessoal-$USER/backup/2022

echo 'Y)'
rm -vr /tmp/pessoal-$USER/backup

echo 'Z)'
rm -vr /tmp/pessoal-$USER

echo 'FIM'