CLI Examples
=============

Configuration
==============

All configuration is done in `script.toml`:
Set your installation path (`/usr/share/nmap` by default)


Help
-----

Use ``--help`` flag to get all optionals arguments.

.. code-block:: sh

    >> nse-install --help
    usage: nse-install [-h] [-l] [-c] [-i INSTALL] [-u UPDATE] [-ia] [-ua]

    Install and update external NSE script for Nmap

    optional arguments:
      -h, --help            show this help message and exit
      -l, --list            List available sources and scripts
      -c, --clean           Remove all scripts previously installed
      -i INSTALL, --install INSTALL
                            Install a nse-script from source
      -u UPDATE, --update UPDATE
                            Update a previously installed nse script
      -ia, --installall     Install all
      -ua, --updateall      Update all


List Sources
============

List all sources you can install :
.. code-block:: sh
    >> nse-install -l
    [+] nmap-elasticsearch-nse by @theMiddleBlue at https://github.com/theMiddleBlue/nmap-elasticsearch-nse
    [+] external-nse-script-library by @cldrn at https://github.com/cldrn/external-nse-script-library
    [+] nmap-nse-scripts by @hackertarget at https://github.com/hackertarget/nmap-nse-scripts
    [+] nmap-vulners by @vulnersCom at https://github.com/vulnersCom/nmap-vulners
    [+] nmap-scripts by @takeshixx at https://github.com/takeshixx/nmap-scripts
    [+] freevulnsearch by @OCSAF at https://github.com/OCSAF/freevulnsearch
    [+] nmap-scada by @jpalanco at https://github.com/jpalanco/nmap-scada
    [+] NSE-scripts by @psc4re at https://github.com/psc4re/NSE-scripts
    [+] nse-scripts by @b4ldr at https://github.com/b4ldr/nse-scripts
    [+] NSE by @s4n7h0 at https://github.com/s4n7h0/NSE




Install & Install All
======================

Install a single source : 
.. code-block:: sh
    >> nse-install -i https://github.com/theMiddleBlue/nmap-elasticsearch-nse
    [+] Installing nmap-elasticsearch-nse by @theMiddleBlue
    [+] Unpacking ./test/nmap-elasticsearch-nse/elasticsearch.nse
    [+] nmap-elasticsearch-nse successfully Installed !

Or install all nse-scripts from `script.toml`
.. code-block:: sh
    >> nse-install -ia 
    [+] Installing nmap-elasticsearch-nse by @theMiddleBlue
    [+] Unpacking ./test/nmap-elasticsearch-nse/elasticsearch.nse
    [+] nmap-elasticsearch-nse successfully Installed !

    [+] Installing nmap-nse-scripts by @hackertarget
    [+] Unpacking ./test/nmap-nse-scripts/hostmap-hackertarget.nse
    [+] Unpacking ./test/nmap-nse-scripts/http-wordpress-info.nse
    [+] Unpacking ./test/nmap-nse-scripts/http-wordpress-plugins.nse
    [+] Unpacking ./test/nmap-nse-scripts/http-wordpress-themes.nse
    [+] nmap-nse-scripts successfully Installed !

    [+] Installing nmap-vulners by @vulnersCom
    [+] Unpacking ./test/nmap-vulners/http-vulners-regex.nse
    [+] Unpacking ./test/nmap-vulners/vulners.nse
    [+] Unpacking ./test/nmap-vulners/http-vulners-paths.txt
    [+] Unpacking ./test/nmap-vulners/http-vulners-regex.json
    [+] nmap-vulners successfully Installed !

    ...

Update & Update All
======================

Update a single source:
.. code-block:: sh
    >> nse-install -u https://github.com/theMiddleBlue/nmap-elasticsearch-nse
    [+] Updating nmap-elasticsearch-nse by @theMiddleBlue
    [-] nmap-elasticsearch-nse : Already up to date.

Or update all nse-scripts from `script.toml`
.. code-block:: sh
    >> nse-install -ua
    [+] Updating nmap-elasticsearch-nse by @theMiddleBlue
    [-] nmap-elasticsearch-nse : Already up to date.

    [+] Updating external-nse-script-library by @cldrn
    [-] external-nse-script-library : Already up to date.

    [+] Updating nmap-nse-scripts by @hackertarget
    [-] nmap-nse-scripts : Already up to date.

    ...

Clean
=====

If you want to remove all scripts install with `nse-install`:
.. code-block:: sh
    >> nse-install -c
    [-] Deleting nmap-elasticsearch-nse
    [-] Deleting external-nse-script-library
    [-] Deleting nmap-nse-scripts
    [-] Deleting nmap-vulners
    [-] Deleting nmap-scripts
    [-] Deleting freevulnsearch
    [-] Deleting nmap-scada
    [-] Deleting NSE-scripts
    [-] Deleting nse-scripts
    [-] Deleting NSE
    [+] Everything Cleaned !