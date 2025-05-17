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
    
if __name__ == '__main__':
    games_data = load_games_from_json('data/games.json')
    
     