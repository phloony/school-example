# School Example

Esse projeto tem o objetivo de simular um sistema escolar simples
focado no uso de APIs

# Instalando ambiente de desenvolvimento

- Necessário ter docker e docker-compose instalado.

1. Crie um arquivo **.env** com base no .env-sample.
    O sample já possui os dados utilizados para funcionar em desenvolvimento.

2. Faça o build da imagem docker

    ```bash
    docker-compose build
    ```

3. Suba o banco de dados

    ```bash
    docker-compose up -d db
    ```

4. Execute as migrações iniciais

    ```bash
    docker-compose run --rm web python app/manage.py migrate
    ```

5. Carregue dados de exemplo iniciais (não é necessário, mas facilita na visualização inicial)

    ```bash
    docker-compose run --rm web python app/manage.py loaddata app/initial_sample.json
    ```

6. Executar os testes e verificar a cobertura

    ```bash
    docker-compose run --rm web coverage run app/manage.py test students classes
    ```

7. Obter o reporte dos testes e verificar a cobertura

    ```bash
    docker-compose run --rm web coverage report
    ```

    Também é possível gerar um html para melhor visualização com o comando (ficará salvo por padrão na pasta htmlcov):

    ```bash
    docker-compose run --rm web coverage html
    ```
    Para visualizar é só abrir o arquivo htmlcov/index.html

8. Para executar a aplicação

    ```bash
    docker-compose run --rm --service-ports web
    ```

Feito isso, a aplicação estará rodando localmente (padrão porta 8000)


# Documentação Swagger

Para facilitar a compreensão dos endpoits disponíveis, a página inicial da aplicação já contém o que pode ser acessado e o formato esperado na forma de uma simples documentação Swagger, já com os campos possíveis de serem filtrados.

Dividi o projeto em duas apps distintas (Students e Classes), com o intuito de que estaria aberto a ser desenvolvidos diversas funções específicas mantendo a organização

O setor "Schemas" exibe os campos e seus tipos esperados pelos endpoints

![image](https://user-images.githubusercontent.com/51096623/155822985-d5b536e3-0348-42a2-abe8-08c04c99a6c1.png)


## Melhorias já observadas

- Por se tratar de um exemplo/amostra, os campos e modelos de dados estão simples e não muito elaborados, principalmente no quesito aulas/notas;
- Pelo mesmo motivo ainda não foi adicionado gerenciamento de permissões e usuário logado.
