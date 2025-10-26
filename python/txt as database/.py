from pathlib import Path

path = Path.cwd() / 'python' / 'txt as database' / 'todo.txt'

def todo_reader():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            next(f)
            for line in f:
                if line.strip():

def read_todo():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            next(f)
            for line in f:
                if line.strip():
                    id, todo, status = line.strip().split('|')
                    return [id, todo, status]
            return ['file kosong']
    except FileNotFoundError:
        return ('file tidak ada')

def create_todo():
    todo = input('masukan todo : ')
    try:
        with open(path, 'a', encoding='utf-8') as f:
            f.write(f'\n{id}|{todo}|belum')
    except FileNotFoundError:
        print('file tidak ada')

print(read_todo())
# create_todo()