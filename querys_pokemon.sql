-- Exemplo de consulta

WITH geracoes AS (
    SELECT *,
        CASE
            WHEN id_pokemon < 152 THEN '1° Geração'
            WHEN id_pokemon BETWEEN 152 AND 251 THEN '2° Geração'
            WHEN id_pokemon BETWEEN 252 AND 386 THEN '3° Geração'
            WHEN id_pokemon BETWEEN 387 AND 493 THEN '4° Geração'
            WHEN id_pokemon BETWEEN 494 AND 649 THEN '5° Geração'
            WHEN id_pokemon BETWEEN 650 AND 721 THEN '6° Geração'
            WHEN id_pokemon BETWEEN 722 AND 809 THEN '7° Geração'
            WHEN id_pokemon BETWEEN 810 AND 905 THEN '8° Geração'
            WHEN id_pokemon BETWEEN 906 AND 1025 THEN '9° Geração'
        END AS geracoes_pokemon
    FROM pokemons
)

-- Pode filtrar as gerações
SELECT *
FROM geracoes
WHERE geracoes_pokemon == '1° Geração'