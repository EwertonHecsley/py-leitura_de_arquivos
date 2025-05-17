from src.games_report import get_all_plataforms

def test_get_all_plataforms():
    data = [
    {
        "id": 1,
        "nome": "Minecraft",
        "plataforma": "Multi",
        "ano_lancamento": 2011,
        "vendas_milhoes": 238,
        "genero": "Sandbox",
        "desenvolvedor": "Mojang"
    },
    {
        "id": 2,
        "nome": "Grand Theft Auto V",
        "plataforma": "Xbox 360",
        "ano_lancamento": 2013,
        "vendas_milhoes": 175,
        "genero": "Ação/Aventura",
        "desenvolvedor": "Rockstar Games"
    },
    {
        "id": 3,
        "nome": "Tetris",
        "plataforma": "Multi",
        "ano_lancamento": 1984,
        "vendas_milhoes": 100,
        "genero": "Puzzle",
        "desenvolvedor": "Alexey Pajitnov"
    },
        ]
    plataforms = get_all_plataforms(data)
    assert plataforms =={"Multi","Xbox 360"}
    