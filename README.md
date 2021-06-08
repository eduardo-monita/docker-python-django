# docker-python-django
Meu projeto de referência utilizando Docker com aplicações em Django

## Dependencias
- Se você deseja executar o projeto, primeiro certifique-se de ter o docker instalado em seu computador. Se não, você pode obte-lo cliquando [aqui](https://docs.docker.com/get-docker/ "aqui").

- Logo em seguida, Git clone este repositório para o seu PC

        git clone https://github.com/eduardo-monita/docker-python-django.git
        
### Instalação (Desenvolvimento)
- Para instalação do projeto, seguindo os pré-requisitos, basta possuir o Docker instalado na máquina na versão mais atualizada possível.

- Após baixado o projeto, basta construir o container no local que estiver presente o arquivo `docker-compose.yml` com o seguinte comando:

        docker-compose build
- Com isso, você conseguirá subir o container em sua máquina com o seguinte comando:

        docker-compose up -d
- Após esses passos, a instalação do container foi finalizada e podemos preparar para realizar as seguintes instruções para configuração do projeto no novo container.

- Obs: Para para o container, segue o seguinte comando: `docker-compose down` 

## Configuração do container (Desenvolvimento)
- Para a configuração do container, será necessário acessá-lo, os comandos abaixo fora do container comprometerá o funcionamento adequado da sua própria máquina, o contrário também é verídico, por isso, atenção sobre qual ambiente você está localizado.

        docker exec -it docker-python-django-web-dev sh
        python manage.py migrate
        python manage.py collectstatic --no-input
        python manage.py createsuperuser
        
## Executá-lo (Desenvolvimento)
- Agora você pode acessar o serviço API de arquivo em seu navegador usando:

        http://localhost:8080/
        
### Instalação (Produção)
- Para construir o container de produção é necessário especificar o arquivo docker dele (`docker-compose.prd.yml`) com o seguinte comando:

        docker-compose -f docker-compose.prd.yml build
        docker-compose -f docker-compose.prd.yml up -d
        
- Obs: Para para o container, segue o seguinte comando: `docker-compose -f docker-compose.prd.yml down` 

## Configuração do container (Produção)
- Para a configuração do container, será necessário acessá-lo, os comandos abaixo fora do container comprometerá o funcionamento adequado da sua própria máquina, o contrário também é verídico, por isso, atenção sobre qual ambiente você está localizado.

        docker exec -it docker-python-django-web-prd sh
        python manage.py migrate
        python manage.py collectstatic --no-input
        python manage.py createsuperuser
        
## Executá-lo (Produção)
- Agora você pode acessar o serviço API de arquivo em seu navegador usando:

        http://localhost:9100/

## Testes Unitários
- Para rodar os exemplos de testes unitários, segue o comando abaixo:

        python manage.py test
        
## Rotas
Rotas |HTTP | Resultado
-- | -- |-- 
`admin` | GET | Para acessar o admin padrão do próprio Django
`api/client` | GET | Pegar a lista de clientes
`api/client/{id}` | GET | Pegar um único cliente em específico
