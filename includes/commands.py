import random
from includes.addition import *
def new():
    res = ''
    dict_ = get_nicks()
    list_p = []
    while True:
        if not res:
                # try:
                res += "{} {}".format(
                        dict_["names"][random.randint(0, len(dict_["names"])-1)],
                        dict_["lasts"][random.randint(0, len(dict_["lasts"])-1)]
                )
                # except  IndexError:
                #         continue 
        if res not in list_p:
                print(res)
                like = input("Do you like it?\n")
                if like == "yes":
                        break
                elif like == "previous":
                        res = list_p[-1]
                        list_p.remove(list_p[-1])
                        continue
                else:
                        list_p.append(res)
                        res = ''
        else:
                res = ''
                continue

# def only_nick():
#         dict_ = get_nicks()
#         res = ''
#         list_p = []
#         while True:
#                 if not res:
#                         try:
#                                 res += f'{name}'
#                         except IndexError:
#                                 continue
#                 if res not in list_p:
                          

        

def add():
        new_nick = input("New nick -> ")
        dict_ = get_nicks()
        if  new_nick in dict_['names']:
            print("Already exist")
        else:
            dict_['names'].append(new_nick)
            refresh_nicks(dict_)

def list_of_nicks():
    dict_ = get_nicks()
    res = ''
    for name in dict_['names']:
        res += f'{name}:\n'
        for surname in dict_['lasts']:
            res += f'\t{name} {surname}\n'
    print(res)

def delete():
    dict_ = get_nicks()
    name_delete = input("Delete naick -> ")
    for args in dict_:
        if name_delete in dict_[args]:
            dict_[args].remove(name_delete)
    refresh_nicks(dict_)

            