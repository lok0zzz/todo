import time

todos_not_completed = {
    'work': 'i need finish my work as sson as possible',
    'study': 'i have a important test tomorrow'
}

todos_completed = {
    'go to gym': 'i need go to ocian praia clube, tomorrow is leg day'
}


# ToDO: criar soluções para possiveis problemas.

# Adiciona uma ToDo.
def add_todo(todo_name, todo_details):
    todos_not_completed[todo_name] = todo_details
    print('\n\n>>>>>>>>> Done!')


# Remove uma ToDO.
def remove_todo(todo_name):
    try:
        del all_todos[todo_name]
        del todos_not_completed[todo_name]
        del todos_completed[todo_name]
    except KeyError as err:
        pass
    except Exception as err:
        print('\n\n>>>>>>>>> ERROR!')

    print('\n\n>>>>>>>>> Done!')


# Faz a ToDo ficar completada.
def todo_completed(todo_name):
    try:
        todo_to_completed_name = todo_name.capitalize()
        todo_to_completed_details = todos_not_completed[todo_name]

        todos_completed[todo_to_completed_name.lower()] = todo_to_completed_details
    except KeyError:
        print("\n\n>>>>>>>>> KeyError, this ToDo doesn't exists.")
    except Exception as err:
        print("\n\n>>>>>>>>> ERROR!")

    del todos_not_completed[todo_to_completed_name.lower()]

    print('\n\n>>>>>>>>> Done!')


# Mostra as ToDos não completadas.
def show_todos_not_completed():
    print('\n\n================= Not-Completed ToDos List =================\n\n')
    print('-------------------------------------')
    for todo in todos_not_completed:
        print(todo.capitalize() + '         | Not done' + '\n-----------------------------------')


# Mostra as ToDos completadas.
def show_todos_completed():
    print('\n\n================= Completed ToDos List =================\n\n')
    print('-------------------------------------')
    for todo in todos_completed:
        print(todo.capitalize() + '         | Done' + '\n-----------------------------------')


# Mostra todas as ToDos
def show_all_todos():
    print('\n\n================= All ToDos =================\n\n')
    print('-------------------------------------')
    for todo in all_todos:
        print(todo.capitalize() + '\n-----------------------------------')


# Traz informações da ToDo.
def open_todo(todo_name):
    try:
        print(f'\n\n================= {todo_name.capitalize()} =================\n\n')
        print('-------------------------------------\n')
        print('      ' + all_todos[todo_name])
        print('\n-------------------------------------')
    except KeyError:
        print("\n\n>>>>>>>>> KeyError, this ToDo doesn't exists.")
    except Exception as err:
        print("\n\n>>>>>>>>> ERROR!")



while True:
    all_todos = dict(todos_completed)
    all_todos.update(todos_not_completed)
    time.sleep(0)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n================= ToDos =================')
    print('\n What you wanna do?\n')
    print('     1. Show not-completed ToDos.\n'
          '     2. Show completed ToDos.\n'
          '     3. Open ToDo.\n'
          '     4. Add a new ToDo.\n'
          '     5. Make a ToDo as completed.\n'
          '     6. Remove a ToDo.\n'
          '     7. Close')

    awnser = input('\n  • ')

    if awnser == '1':
        show_todos_not_completed()

    if awnser == '2':
        show_todos_completed()

    if awnser == '3':
        show_all_todos()
        print('\nWhat ToDo you wanna open?')
        todo_awser = input('\n  • ')
        open_todo(todo_awser.lower())

    if awnser == '4':
        print("What's the ToDo name?")
        name_todo = input('\n  • ')

        print('Give me more details')
        details_todo = input('\n  • ')

        add_todo(name_todo.lower(), details_todo)

    if awnser == '5':
        show_todos_not_completed()

        print("What's the ToDo name?")
        name_todo = input('\n  • ')

        todo_completed(name_todo)

    if awnser == '6':
        show_all_todos()
        print('What ToDo you wanna remove?')
        name_todo = input('\n  • ')

        remove_todo(name_todo)

    if awnser == '7':
        break
