# Trabalho Final de Engenharia de Software III

### Descrição
  O sistema foi feito em Django, framework de desenvolvimento web baseado em Python. O padrão de projeto adotado na tecnologia utilizada é o Model-View-Template que, em termos básicos:
  - O Model, tal como no MVC, é onde ficam as regras de negócio do projeto. 
  - Na View é onde são realizadas funções similares às de um Controller no MVC, mediando a entrada e saída de dados do Banco. 
  - Já no Template é onde ocorre a interação direta do usuário com o sistema, tal como nas Views do MVC.

### Escopo
  O sistema implementou, tal como fora pedido em video-aula online, pelo menos duas funcionalidades do sistema estudado durante toda a disciplina: visualizar notas e realizar matrícula. Para isso, foram implementados os casos de uso "Realizar Matrícula" é "Cadastrar Disciplina", bem como todos os atores e entidades necessários para este fim.
  
### Configuração do Ambiente: 
#### Pacotes e Versões Necessários:
- Python==3.8.0
- Instalador de pacotes pip
- Django==3.1.5

#### Passo-a-passo no Shell:
Primeiro será necessário configurar o ambiente virtual, caso não tenha o pacote "virtualenv" instale rodando no terminal o comando abaixo
```
pip install virtualenv
```
Em sistemas linux, talvez seja necessário usar o comando abaixo
```
pip3 install virtualenv
```
Após isso você deve criar o ambiente virtual com o comando
```
virtualenv aps_env
```
No windows, você precisará rodar o seguinte comando para ativar o ambiente virtual
```
aps_env\Scripts\activate
```
No Mac ou Linux, o comando é
```
source aps_env/bin/activate
```
Após isso você deverá instalar o django, então é só rodar
```
pip install django==3.1.5
```
ou
```
pip3 install django==3.1.5
```

Então para rodar o projeto, é necessário que sejam feitas as migrações primeiro. Logo, abra o shell de sua preferência dentro da pasta principal do projeto (onde está o arquivo "manage.py"), e digite:
```
python manage.py makemigrations
```

E, então, aplicam-se as migrações:
```
python manage.py migrate
```

Para criar um super usuário, basta executar:
```
python manage.py createsuperuser
```

E fornecer os dados requeridos.

Por fim, para iniciar o servidor:
```
python manage.py runserver <numero_da_porta>
```

#### Uso do sistema 
O sistema apresenta diferentes funções de acordo com usuário logado. Caso o arquivo db.sqlite3 esteja presente estarão cadastrados dois usuários para fins de testes,
caso contrário, deverá ser criado no painel de administrador.

<strong>Professor</strong><br>
Usuário -> 20191prof0000 <br>
Senha -> senha1234<br>

<strong>Aluno</strong><br>
Usuário -> 20191ads0000 <br>
Senha -> senha1234<br>