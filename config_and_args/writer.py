from configparser import ConfigParser

def main():
    configobj = ConfigParser(allow_no_value=True)
    configobj["SAGE_LSTM"] = {
        "test": False,
        "epochs": 100,
        "from_checkpoint":"",
        "graph_hid_dim":7,
        "adj_mx_path":"",
        "popularity_path":"",
        "percent":10,
        "remap_id_path":"",
    }

    with open('config.ini','w') as conf:
        configobj.write(conf)

if __name__=="__main__":
    main()
