# Repositório do projeto de python para o workshop de CI/CD do glua

Este repositório contêm o código do projeto de demonstração de uma codebase python
com integração contínua através das github actions.

## Instruções de desenvolvimento

Primeiro é necessário instalar as dependências:

```bash
$ pip3 install -r requirements.txt
```

Para correr o programa

```bash
$ python3 app/main.py
```

Para validar o código

```bash
$ flake8 .
```

Para correr os testes

```bash
$ pytest
```

## Workflows

A pasta `.github/workflows` contêm os workflows finais que correm no github.
