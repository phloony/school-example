# School Sample

Esse projeto tem o objetivo de simular um sistema escolar simples
focado no uso de APIs

# Instalando ambiente de dev

- Necessário ter docker e docker-compose instalado.

1. Crie um arquivo **.env** com base no .env-sample.
    O sample já possui os dados para funcionar em desenvolvimento.

2. Faça um build na imagem docker

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

6. Para executar a aplicação

    ```bash
    docker-compose run --rm --service-ports web
    ```

Feito isso, a aplicação estará rodando localmente (padrão porta 8000)