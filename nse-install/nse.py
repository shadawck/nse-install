import toml
import glob
import subprocess as sp
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
    
    nse_name = scriptSource.split("/")[-1]
    full_path = installPath + nse_name

    if path.exists(full_path):
        print("Consider updating")
    else:
        sp.run(["git","clone","--depth=1",scriptSource,full_path])
    
    # unpack nse script
    nse_script = glob.glob(full_path+ "/*.nse")
    for file in nse_script:
        sp.run(["cp",file,installPath])
    print(nse_name, "INSTALLED")


def clean_install():
    """Clean install and unnecessary files (like README.md)
    """
    pass

def install_all_script(installPath,dictConfig):
    """Install all NSE script from toml config file
    """
    nse_script_links = dictConfig["nse-scripts"]["script"]

    for links in nse_script_links:
        print("Installing", links.split("/")[-1])
        install_script(installPath,links)

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

src = "https://github.com/s4n7h0/NSE"
install_script(install_path,src)