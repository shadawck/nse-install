#__main__.py
import argparse
from nse_install import nse_install as nse

def main():
    parser = argparse.ArgumentParser(prog="nse-install",description='Install and update external NSE script for Nmap')
    
    parser.add_argument("-l","--list", action="store_true", help="List available sources and scripts")
    parser.add_argument("-c", "--clean",action="store_true", help="Remove all scripts previously installed")
    
    parser.add_argument("-i","--install", help="Install a nse-script from source")
    parser.add_argument("-u","--update", help="Update a previously installed nse script")

    parser.add_argument("-ia", "--installall",action="store_true", help="Install all")
    parser.add_argument("-ua", "--updateall",action="store_true", help="Update all")
    
    
    
    args = parser.parse_args()
    
    CONFIG_DICT = nse.load("script.toml")
    INSTALL_PATH = CONFIG_DICT["install_path"]
    nse.check_nmap_path(CONFIG_DICT)

    ## //TODO clean this with a better impl
    if args.list:
        nse.list_scripts(CONFIG_DICT)
        exit(0)

    if args.clean:
        nse.clean_install(INSTALL_PATH,CONFIG_DICT)
        exit(0)

    if args.installall :  
        nse.install_scripts_all(INSTALL_PATH,CONFIG_DICT)
        exit(0)

    if args.updateall:
        nse.update_scripts_all(INSTALL_PATH,CONFIG_DICT)
        exit(0)

    if args.install:
        nse.install_script(INSTALL_PATH,args.install)
        exit(0)

    if args.update:
        nse.update_script(INSTALL_PATH,args.update)
        exit(0)

if __name__ == "__main__":
    main()