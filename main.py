from functions import get_todos, write_todos
import time

now_time = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is now {now_time}")
while True:
    user_text = input("Type add, show, edit, complete or exit: ")
    user_text = user_text.strip()

    if user_text.startswith('add'):
        todo = user_text[4:] #we use four as an index, because add is 3 characters and space is one.
        todos = get_todos()
        todos.append(todo + '\n' )
        write_todos(todos)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_text.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_text.startswith('edit'):
        try:
            number = int(user_text[5:])
            print(number)
            number = number - 1
            todos = get_todos('todos.txt')
            new_todo = input("please enter a new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_text.startswith('complete'):
        try:
            number = int(user_text[9:])
            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(number - 1)
            write_todos(todos)
            message = f"Todo {todo_to_remove} has been completed and removed from the list and the list updated."
            print(message)
        except IndexError:
            print("No item with that number!")
            continue
    elif user_text.startswith('exit'):
        break
    else:
        print('Command is not valid!')
print('Bye!')

