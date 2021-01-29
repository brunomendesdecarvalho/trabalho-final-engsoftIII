# Trabalho Final de Análise e Projeto de Sistemas

### Descrição
  O sistema foi feito em Django, framework de desenvolvimento web baseado em Python, juntamente com o Django Rest Framework. O padrão de projeto adotado na tecnologia utilizada é o Model-View-Template. O Model, tal como no MVC, é onde ficam as regras de negócio do projeto. Na View é onde são realizadas funções similares às de um Controller no MVC, mediando a entrada e saída de dados do Banco. Já no Template é onde ocorre a interação direta do usuário com o sistema, tal como nas Views do MVC.

### Escopo
  O sistema implementou, tal como fora pedido em video-aula online, pelo menos duas funcionalidades do sistema estudado durante toda a disciplina: visualizar notas e realizar matrícula. Para isso, foram implementados os casos de uso "Realizar Matrícula" é "Cadastrar Disciplina", bem como todos os atores e entidades necessários para este fim.
  
### Configuração do Ambiente: 
#### Pacotes e Versões Necessários:
- Python==3.8.0
- Django==3.1.5
- django-filter==2.4.0
- djangorestframework==3.12.2

#### Passo-a-passo no Shell:
Para rodar o projeto, é importante que sejam feitas as migrações primeiro. Logo, abra o shell de sua preferência dentro da pasta principal do projeto (onde está o arquivo "manage.py"), e digite:
```
python manage.py makemigrations
```

E, então, aplicam-se as migrações:
```
python manage.py migrate
```

Para cadastrar um super usuário, basta executar:
```
python manage.py createsuperuser
```

E fornecer os dados requeridos.

Por fim, para iniciar o servidor:
```
python manage.py runserver 8000
```
