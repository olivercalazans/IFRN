#!/bon/bash

echo "Informe o caminho"
read caminho

if [ -d "$caminho" ]; then
    echo "É um diretório"
elif [ -f "$caminho" ]; then
    echo "É um arquivo"
else
    echo "Não existe ou não é um diretório ou arquívo."
fi