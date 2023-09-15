# Projeto TING (Trybe is not Google)

Este projeto implementa um programa que simula um algoritmo de indexação de documentos similar ao do Google, sendo possível identificar ocorrências de termos em arquivos _TXT_.
  
Para isso, o programa desenvolvido tem dois módulos:
- **Módulo de gerenciamento de arquivos** que permite anexar arquivos de texto (formato _TXT_) e;
- **Módulo de buscas** que permite operar funções de busca sobre os arquivos anexados.

## Habilidades exercitadas:

 - Manipular Pilhas;

 - Manipular Deque;

 - Manipular Nó & Listas Ligadas e;

 - Manipular Listas Duplamente Ligadas.

## Tecnologias usadas

 - Python3
 - Pytest 7.1.1
 - Flake8 3.8.4
 - Black

## Instalação

Para instalar, recomenda-se que inicie um ambiente de desenvolvimento virtual python:

```bash
python3 -m venv .venv
```

Para executar o ambiente virtual de desenvolvimento basta executar o script de ativação dentro da pasta <code>.venv/Scripts/</code>.

Feito isso, basta instalar as dependências do projeto:

```bash
python3 -m pip install -r dev-requirements.txt
```

## Como testar

Para testar as funcionalidades escritas no programa, basta executar o script de teste:

```bash
python -m pytest
```
