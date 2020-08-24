import toml
import subprocess as sp
from multiprocessing import Pool
from os import path

def load(toml_config):
    """Load toml config file
    """
    if toml_config.split(".")[-1] == "toml":
        return toml.load(toml_config)
    return toml.load(toml_config+".toml")
    

def check_nmap_path(configDict):
    """check nmap script path and if not, create one.
    """
    install_path = configDict["install_path"]
    if path.exists(install_path):
        return True

    return sp.Popen(["mkdir","-p",install_path])

def install_script(installPath,scriptSource):
    """Clone and install NSE script from CLI
    """

    if path.exists(scriptSource.split("/")[-1]):
        print("Consider updating")
    else:
        print(scriptSource)
        sp.run(["git","clone","--depth=1",scriptSource,installPath])



def clean_install():
    """Clean install and unnecessary files (like README.md)
    """
    pass

def install_all_script(installPath,scriptsList):
    """Install all NSE script from toml config file
    """

    


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


configDict = load("script.toml")
install_path = configDict["install_path"]

src = "https://github.com/theMiddleBlue/nmap-elasticsearch-nse"

print(install_script(install_path,src))