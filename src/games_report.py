import json

def load_games_from_json(file_path):
    '''Funcao para carregar os jogos de um arquivo JSON.'''
    data = []
    try:
        with open(file_path,"r") as file:
            data = json.load(file)    
    except  FileNotFoundError:
        raise FileNotFoundError(f'Endereco de aquivo {file_path} nao encontrado.')
    except json.decoder.JSONDecodeError:
        print('Formato invalido, deve ser JSON')
        
    return data


def get_all_plataforms(games_data):
    '''Funcao para listar todas as plataformas dos jogos.'''
    consoles = set()
    for game in games_data:
        consoles.add(game['plataforma'])
    return consoles    


def get_max_sales(games_data):
    '''Funcao para encontrar o jogo com maior venda.'''
    max_sales = 0
    game_name = ''
    for game in games_data:
        if game['vendas_milhoes'] > max_sales:
            max_sales = game['vendas_milhoes']
            game_name = game['nome']
    return game_name, max_sales



if __name__ == '__main__':
    games_data = load_games_from_json('data/games.json')
    consoles = get_all_plataforms(games_data)
    max_sales = get_max_sales(games_data)
    print(f'Plataformas: {consoles}')
    print(f'Jogo com maior venda: {max_sales[0]} com {max_sales[1]} milhões')
     