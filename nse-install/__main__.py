import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="nse-install",description='Install and update external NSE script for Nmap')
    
    parser.add_argument("-l","--list", action="store_true", help="List available sources and scripts")
    parser.add_argument("-i","--install", help="Install a nse-script from source")
    parser.add_argument("-u","--update", help="Update a previously installed nse script")
    parser.add_argument("-a", "--all",action="store_true", help="Install all or Update all")
    
    args = parser.parse_args()
    
    if args.list:
        pass

    if args.all :
        if args.install:
            pass
        elif args.update:
            pass
        else :
            print("You choose Install All & Update All which is a little bit useless but OK !")

    if args.install:
        pass
    elif args.update:
        pass
    else :
        print("You choose Install & Update which is a little bit useless but OK !")

    
