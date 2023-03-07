# desafio_biopark
README
Este projeto foi desenvolvido utilizando Python com Django e utiliza uma conexão MySQL local via WampServer no localhost.


O projeto consiste em um sistema para gerenciamento de apartamentos e os alugueis do mesmos. Porém devido ao tempo curto, não consegui desenvolver e aprimorar o código da aplicação


Configurações do ambiente
Instalação do Python
Primeiramente, certifique-se de ter o Python instalado em sua máquina. Caso você não tenha o Python instalado, você pode baixá-lo em python.org.

Instalação do Django
Com o Python instalado, você precisa instalar o Django. Para isso, abra o terminal e digite o seguinte comando:

- pip install Django

Instalação do mysqlclient

- pip install mysqlclient

Instalação do WampServer
O próximo passo é instalar o WampServer, um software que irá criar um servidor local em sua máquina, permitindo a execução do MySQL.

Você pode baixar o WampServer em wampserver.com.

Configuração do MySQL
Após a instalação do WampServer, certifique-se de que o serviço do MySQL esteja rodando. No phpmyadmin logue com 

utilizador: root
palavra-passe: 
Escolha de servidor: MySQL

Crie um banco com o nome 'sistema' e importe a estrutura do arquivo 'sistema.sql' presente na pasta do projeto. 
Em seguida ajuste o Project/settings.py colocando a conexão do banco criado, caso tenha criado o banco seguindo as configurações padrão não será necessário

Configuração do projeto
Com o ambiente configurado você pode executar o sistema utilizando o comando

- python .\manage.py runserver 


Os dados para acessar a aplicação são 
login:'admin'
senha:'123'
 
Os cadastros de data estão no formato mm/dd/yyyy
