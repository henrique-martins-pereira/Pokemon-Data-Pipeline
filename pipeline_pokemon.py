import requests as rq
import time
import sqlite3

conn = sqlite3.connect('pokemons.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pokemons (
    id_pokemon INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_pokemon TEXT NOT NULL,
    tipo_1 TEXT NOT NULL,
    tipo_2 TEXT NOT NULL,
    base_state_hp INTEGER NOT NULL,
    base_state_attack INTEGER NOT NULL,
    base_state_defense INTEGER NOT NULL,
    base_state_sp_atk INTEGER NOT NULL,
    base_state_sp_def INTEGER NOT NULL,
    base_state_speed INTEGER NOT NULL
)
''')

conn.commit()

def adicionar_banco(nome, tipo_1, tipo_2, base_state_hp, base_state_attack, base_state_defense, base_state_sp_atk, base_state_sp_def, base_state_speed):
    cursor.execute('''
    INSERT INTO pokemons (nome_pokemon, tipo_1, tipo_2, base_state_hp, base_state_attack, base_state_defense, base_state_sp_atk, base_state_sp_def, base_state_speed)
    VALUES (?,?,?,?,?,?,?,?,?)''', (nome, tipo_1, tipo_2, base_state_hp, base_state_attack, base_state_defense, base_state_sp_atk, base_state_sp_def, base_state_speed))

def buscar_dados(url):
    while True:
        try:
            resultado = rq.get(url)

            if resultado.status_code == 429:
                espera = resultado.headers.get('Retry-After', 20)
                print(f'Esperando{espera} segundos...')
                time.sleep(espera)
                continue

            resultado.raise_for_status()
            return resultado.json()
        except Exception as erro:
            print(f'Erro encontrado {erro}')
            continue

base_url = 'https://pokeapi.co/api/v2/pokemon'
resultados = []

for indice in range(1,1026):
    print(f'Coletando dados do indice {indice}')

    url_pokemon = f'{base_url}/{indice}'
    dados_pokemon = buscar_dados(url_pokemon)

    nome = dados_pokemon['species']['name']
    type_1 = dados_pokemon['types'][0]['type']['name']
    type_2 = 'Não tem segundo tipo'

    if len(dados_pokemon['types']) > 1:
        type_2 = dados_pokemon['types'][1]['type']['name']

    base_state_hp = dados_pokemon['stats'][0]['base_stat']

    base_state_attack = dados_pokemon['stats'][1]['base_stat']

    base_state_defense = dados_pokemon['stats'][2]['base_stat']

    base_state_sp_atk = dados_pokemon['stats'][3]['base_stat']

    base_state_sp_def = dados_pokemon['stats'][4]['base_stat']

    base_state_speed = dados_pokemon['stats'][5]['base_stat']

    resultados.append({
        'nome': nome,
        'type_1': type_1,
        'type_2': type_2,
        'base_state_hp': base_state_hp,
        'base_state_attack': base_state_attack,
        'base_state_defense': base_state_defense,
        'base_state_sp_atk': base_state_sp_atk,
        'base_state_sp_def': base_state_sp_def,
        'base_state_speed': base_state_speed
    })

for resultado in resultados:
    nome = resultado['nome'].capitalize()
    type_1 = resultado['type_1']
    type_2 = resultado['type_2']
    base_state_hp = resultado['base_state_hp']
    base_state_attack = resultado['base_state_attack']
    base_state_defense = resultado['base_state_defense']
    base_state_sp_atk = resultado['base_state_sp_atk']
    base_state_sp_def = resultado['base_state_sp_def']
    base_state_speed = resultado['base_state_speed']
    adicionar_banco(nome,type_1, type_2, base_state_hp, base_state_attack, base_state_defense, base_state_sp_atk, base_state_sp_def, base_state_speed)

print('Pipeline Completa!!')

conn.commit()
conn.close()