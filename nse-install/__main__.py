import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="nse-install",description='Install and update external NSE script for Nmap')
    
    parser.add_argument("-l","--list", help="List available sources and scripts")
    parser.add_argument("-i","--install", help="Install a nse-script from source")
    parser.add_argument("-u","--update", help="update a previously installed nse scripts")
    parser.add_argument("-a", "--all", help="Install all or Update all")
    
