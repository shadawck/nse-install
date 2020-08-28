from rich.console import Console
from rich import print
import subprocess as sp
from os import path
import toml
import glob

console = Console()

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



def list_scripts(configDict):
    scripts = configDict["nse-scripts"]["scripts"]

    for s in scripts :
        git_data = s.split("/")
        nse_name = git_data[-1]
        git_name = git_data[-2]
        console.print("[bold green][+][/bold green] [bold yellow]%s[/bold yellow] by [bold red]@%s[/bold red] at %s" % (nse_name,git_name,s))



def install_script(installPath,scriptSource):
    """Clone and install NSE script from CLI
    """
    git_data = scriptSource.split("/")
    nse_name = git_data[-1]
    git_name = git_data[-2]
    full_path = installPath + nse_name

    if path.exists(full_path):
        console.print("[+] Consider updating [bold yellow]%s[/bold yellow] by [bold green]@%s[/bold green]" %(nse_name,git_name), style="bold red")
        return 

    print("[bold green][+][/bold green] Installing [bold yellow]%s[/bold yellow] by [bold red]@%s[/bold red]" % (nse_name,git_name))
    capt = sp.run(["git","clone","--depth=1",scriptSource,full_path],stdout=sp.DEVNULL,stderr=sp.DEVNULL)
    
    # unpack nse script
    nse_script = glob.glob(full_path+ "/*.nse") + glob.glob(full_path+ "/*.txt") + glob.glob(full_path+ "/*.json") + glob.glob(full_path+ "/*.csv")
    for file in nse_script:
        sp.run(["cp",file,installPath],stdout=sp.DEVNULL)
        print("[+] Unpacking",file)
    console.print("[bold green][+][/bold green] [bold yellow]%s[/bold yellow] successfully Installed !\n" % (nse_name),style="bold green")
    return



def install_scripts_all(installPath,configDict):
    """Install all NSE script from toml config file
    """
    nse_script_links = configDict["nse-scripts"]["scripts"]

    for links in nse_script_links:
        install_script(installPath,links)



def clean_install(installPath,configDict):
    """Remove installed nse scripts
    """

    scripts = configDict["nse-scripts"]["scripts"]

    for s in scripts : 
        nse_name = s.split("/")[-1]
        full_path = installPath + nse_name

        print("[bold red][-] Deleting[/bold red] [bold yellow]%s[/bold yellow]" %(nse_name))
        sp.Popen(['rm','-rf',full_path])


        nse_script = glob.glob(full_path+ "/*.nse") + glob.glob(full_path+ "/*.txt") + glob.glob(full_path+ "/*.json") + glob.glob(full_path+ "/*.csv")
        nse_script_path = [script.split("/")[-1] for script in nse_script]

        for p in nse_script_path :
            sp.Popen(['rm','-f',installPath + p])
    print("[bold green][+] Everything Cleaned ![/bold green]")



def update_script(installPath,scriptSource):
    """Update NSE script (git pull) from toml config file
    """

    git_data = scriptSource.split("/")
    nse_name = git_data[-1]
    git_name = git_data[-2]
    full_path = installPath + nse_name


    # check if installed 
    if path.exists(full_path) == False:
        console.print("[+] [bold yellow]%s[/bold yellow] not installed !" %(nse_name), style="bold red")
        console.print("[+] Installing [bold yellow]%s[/bold yellow] for you !" %(nse_name), style="bold green")
        install_script(installPath, scriptSource)
        return
    
    # update script with git pull
    print("[bold green][+][/bold green] Updating [bold yellow]%s[/bold yellow] by [bold red]@%s[/bold red]" % (nse_name,git_name))
    update_message = sp.run(["git","-C",full_path,"pull"], stdout=sp.PIPE,universal_newlines=True)

    # the repo is already up to date so do nothing
    if len(str(update_message.stdout)) == 20:
        print("[bold green][-][/bold green] [bold yellow]%s[/bold yellow] : %s" % (nse_name,update_message.stdout))
        return
    # repo is pulled - or error
    # TODO handle error
    else: 
        print("[bold green][-][/bold green] [bold yellow]%s[/bold yellow] : %s" % (nse_name,update_message.stdout))
        nse_script = glob.glob(full_path+ "/*.nse") + glob.glob(full_path+ "/*.txt") + glob.glob(full_path+ "/*.json") + glob.glob(full_path+ "/*.csv")
        for file in nse_script:
            sp.run(["cp",file,installPath],stdout=sp.DEVNULL)
            print("[bold green][+][/bold green]Unpacking",file)
    return



def update_scripts_all(installPath,configDict):
    """Update all script (pull) from toml config file
    """
    nse_script_links = configDict["nse-scripts"]["scripts"]

    for links in nse_script_links:
        update_script(installPath,links)


def add_script():
    """add NSE script from CLI
    """
    pass
