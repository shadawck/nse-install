import toml
import subprocess as sp


def load(toml_config):
    """Load toml config file
    """
    if toml_config.split(".")[-1] == "toml":
        return toml.load(toml_config)
    return toml.load(toml_config+".toml")


def load_config(configDict):
    """read user config file
    """
    

def check_nmap_path():
    """check nmap script path
    """
    pass


def clean_install():
    """Clean install and unnecessary files (like README.md)
    """
    pass

def install_script():
    """Clone and install NSE script from toml config file
    """
    pass


def install_all_script():
    """Install all NSE script from toml config file
    """
    pass

def update_script():
    """Update NSE script (git pull) from toml config file
    """
    pass

def update_script_all():
    """Update all script (pull) from toml config file
    """
    pass

def add_script():
    """add NSE script from CLI
    """
    pass


configDict = load("../script.toml")
print(configDict)

load_config(configDict)
