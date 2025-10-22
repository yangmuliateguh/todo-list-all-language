from pathlib import Path

path = Path.cwd() / 'python' / 'txt as database' / 'todo.txt'

def read_todo():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                id, todo, status = line.strip().split('|')
                print(f'{id}. {todo} ({status})')
    except FileNotFoundError:
        print('file tidak ada')

read_todo()