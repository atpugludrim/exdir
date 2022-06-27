from configparser import ConfigParser

class Struct:
    def __init__(this, **entries):
        this.__dict__.update(entries)

def booltest(string):
    return string.lower().capitalize() == "True"
def get_config():
    config_object = ConfigParser(allow_no_value=True)
    config_object.read("config.ini")
    config_dict = dict()
    options = {
        "test": booltest,
        "epochs": int,
        "from_checkpoint":str,
        "graph_hid_dim":int,
        "adj_mx_path":str,
        "popularity_path":str,
        "percent":int,
        "remap_id_path":str,
    }
    for opt,typ in options.items():
        config_dict[opt] = typ(config_object["SAGE_LSTM"][opt])
    namtup = Struct(**config_dict)
    return namtup

def main():
    # for debugging only
    namtup = get_config()
    # import pdb;pdb.set_trace()
    print(namtup)

if __name__=="__main__":
    main()
