todos = []

def add_todo():
    todo = input("masukan todo :")
    todos.append(todo)
    print(f"{todo} berhasil ditambahkan")

def list_todo():
    if not todos:
        print("To Do List Kosong")
    else:
        print("To Do: ")
        for index, todo in enumerate(todos):
            print(f"To Do #{index}. {todo}")

def update_todo():
    list_todo()
    try:
        index_update = int(input("pilih todo mana yang ingin di update:"))
        if 0 <= index_update < len(todos):
            new_description = input("masukan todo baru:")
            todos[index_update] = new_description
            print(f"To Do {index_update} sudah di update")
        else :
            print("index tidak valid")
    except ValueError:
        print("index yang diberikan tidak valid")
        
def delete_todo():
    list_todo()
    try:
        index_delete = int(input("pilih todo mana yang ingin dihapus:"))
        if 0 <= index_delete < len(todos):
            todos.pop(index_delete)
            print(f"To Do {index_delete} sudah di delete")
        else :
            print("index tidak valid")
    except:
        print("error")

def checklist_todo():
    list_todo()
    try:
        index_todo = int(input("pilih todo mana yang ingin ceklis:"))
        if 0 <= index_todo < len(todos):
            todos[index_todo] += " (sudah)"
            print(f"To Do {index_todo} sudah di ceklis")
        else :
            print("index tidak valid")
    except ValueError:
        print("silahkan masukan index yang valid")


print("generate todo")
while True:
    print("\n")
    print("pilih menu yang tersedia!")
    print("--------------------------------")
    print("1. menambahkan todo")
    print("2. melihat list todo")
    print("3. update todo")
    print("4. menghapus todo")
    print("5. ceklist todo")
    print("6. keluar")

    choice = input("pilih menu:")

    if choice == "1":
        add_todo()
    elif choice == "2":
        list_todo()
    elif choice == "3":
        update_todo()
    elif choice == "4":
        delete_todo()
    elif choice == "5":
        checklist_todo()
    elif choice == "6":
        break

    else: 
        print("pilihan tidak valid")