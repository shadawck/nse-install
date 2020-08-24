import toml

def load(toml_config):
    if toml_config.split(".")[-1] == "toml":
        toml.load(toml_config)
    toml.load(toml_config+".toml")

def install_nse():
    pass

def install_all_nse():
    pass

def update_nse():
    pass

def update_nse_all():
    pass

def add_script():
    pass
