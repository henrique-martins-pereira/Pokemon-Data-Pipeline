# Pokémon Data Pipeline | Python, PokéAPI e SQLite

## Sobre o projeto

Este projeto consiste no desenvolvimento de um pipeline de dados utilizando Python para consumir informações da PokéAPI, realizar a extração e organização dos dados e armazená-los em um banco de dados SQLite.

O objetivo é demonstrar conhecimentos práticos em coleta de dados via API, manipulação de estruturas JSON, tratamento de informações e armazenamento em bancos de dados relacionais.

O pipeline coleta informações de 1.025 Pokémon, incluindo seus tipos e atributos básicos, criando uma base de dados que pode ser utilizada posteriormente para consultas SQL e análises exploratórias.

## Tecnologias utilizadas

- **Python:** desenvolvimento e execução do pipeline.
- **Requests:** consumo da API e obtenção dos dados.
- **SQLite3:** criação e gerenciamento do banco de dados.
- **PokéAPI:** fonte externa dos dados.
- **Time:** controle do intervalo entre as requisições.

## Funcionamento do pipeline

O projeto segue um fluxo de processamento dividido em quatro etapas:

### 1. Extração dos dados (Extract)

O Python realiza requisições HTTP à PokéAPI, consultando individualmente os Pokémon por meio de seus identificadores.

São coletadas informações como:

- Nome do Pokémon.
- Primeiro tipo.
- Segundo tipo, quando disponível.
- HP (Health Points).
- Attack.
- Defense.
- Special Attack.
- Special Defense.
- Speed.

### 2. Organização dos dados (Transform)

Após a extração, os dados retornados pela API são organizados em estruturas de dicionários Python.

Nessa etapa, o projeto:

- Seleciona os campos necessários.
- Organiza os atributos de cada Pokémon.
- Define uma identificação textual para Pokémon que não possuem segundo tipo.
- Armazena temporariamente os resultados em uma lista.

### 3. Armazenamento (Load)

Os dados organizados são inseridos em um banco de dados SQLite chamado `pokemons.db`.

A tabela `pokemons` possui as seguintes colunas:

| Coluna | Descrição |
|---|---|
| id_pokemon | Identificador interno |
| nome_pokemon | Nome do Pokémon |
| tipo_1 | Tipo principal |
| tipo_2 | Tipo secundário |
| base_state_hp | Pontos de vida |
| base_state_attack | Ataque |
| base_state_defense | Defesa |
| base_state_sp_atk | Ataque especial |
| base_state_sp_def | Defesa especial |
| base_state_speed | Velocidade |

### 4. Disponibilização para análise

Após a conclusão da coleta e inserção, os dados ficam disponíveis no SQLite para consultas SQL.

Isso permite explorar informações e desenvolver análises quantitativas sobre os atributos dos Pokémon.

## Estrutura do projeto

```text
pokemon-data-pipeline/
│
├── pipeline_pokemon.py
├── pokemons.db
└── README.md
```

**Observação:** o arquivo `pokemons.db` é gerado durante a execução do projeto.

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/henrique-martins-pereira/Pokemon-Data-Pipeline
```

### 2. Entre na pasta

```bash
cd pokemon-data-pipeline
```

### 3. Instale a dependência

```bash
pip install requests
```

O SQLite3 e o módulo Time já fazem parte da biblioteca padrão do Python.

### 4. Execute o pipeline

```bash
python pipeline_pokemon.py
```

Após a execução, o banco de dados `pokemons.db` será criado ou atualizado.

## Possibilidades de análise

Com os dados armazenados, é possível desenvolver análises como:

- Identificação dos Pokémon com maiores atributos totais.
- Comparação de ataque e defesa entre diferentes tipos.
- Análise da distribuição de velocidade.
- Comparação dos atributos médios por tipo.
- Identificação dos Pokémon com maior HP.
- Análise da distribuição dos atributos básicos.

### Exemplo de consulta SQL

Identificar os 10 Pokémon com maiores atributos totais:

```sql
SELECT
    nome_pokemon,
    base_state_hp +
    base_state_attack +
    base_state_defense +
    base_state_sp_atk +
    base_state_sp_def +
    base_state_speed AS total_status
FROM pokemons
ORDER BY total_status DESC
LIMIT 10;
```

## Objetivos de aprendizagem

Este projeto foi desenvolvido para praticar conceitos importantes da área de dados:

- Consumo de APIs REST.
- Requisições HTTP.
- Manipulação de JSON.
- Estruturas de dados em Python.
- Automação de coleta de dados.
- Integração entre Python e SQL.
- Modelagem e armazenamento de dados.
- Preparação de bases para análise exploratória.

## Fonte dos dados

Os dados utilizados neste projeto são disponibilizados publicamente pela PokéAPI.

Documentação: https://pokeapi.co/

---

**Projeto desenvolvido com Python, APIs e SQL, com foco em Engenharia e Análise de Dados.**
