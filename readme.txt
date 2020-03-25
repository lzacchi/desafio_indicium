Instruções de Execução:

Os arquivos de entrada (companies.tsv, contacts.tsv, deals.tsv e sectors.tsv) devem estar no Diretório 'data/'.
Para rodar o script, execute 'python src/etl.py'
O programa irá ler os arquivos de entrada e, ao final de sua execução, os arquivos csv de saída estarão no diretório 'output/'


Este programa utiliza Poetry como gerenciador de dependências. Para executar o projeto, é preciso utilizar os seguintes comandos:

- 'poetry install'
Isso irá instalar todas as dependencias em um ambiente virtual do projeto

- 'poetry shell'
Esse comando entra na shell do ambiente virtual criado.
Logo após isso, o script pode ser executado com
'python src/etl.py'
