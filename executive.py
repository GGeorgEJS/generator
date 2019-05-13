from includes.commands import *
from includes.addition import creat_nicks

def generator(choice):
    dict_ = {'new': new, 'add': add, 'creat': creat_nicks, 'list': list_of_nicks, 'delete': delete}
    if choice in dict_:
        dict_[choice]()
    else:
        print("No such option")

while True:
    decision = input("Command line: ")
    if decision == "exit":
            break
    elif decision == "help":
            print("""commands:
                                new - creating new nickname
                                delete - delete nicks
                                list - show list of nicks
                                add - add your own nick to database
                                exit - exit
            """)
    else:
        generator(decision)