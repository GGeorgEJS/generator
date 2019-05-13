import pickle
def creat_nicks():
    set_names = ["jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul", "ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren", "ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet", "lydia", "charles", "pedro", "bradley"]
    set_last = ["barker", "style", "spirits", "murphy", "blacker", "bleacher", "rogers", "warren", "keller"]
    dict_ = {"names": set_names, "lasts": set_last}
    with open("dict.pickle", "wb") as dict_data:
            pickle.dump(dict_, dict_data)
def get_nicks():
        with open("dict.pickle", "rb") as dict_data:
                dict_ = pickle.load(dict_data)
                return dict_
def refresh_nicks(dict_):
        with open("dict.pickle", "wb") as dict_data:
                pickle.dump(dict_, dict_data)