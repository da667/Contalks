readme.md

#Suricon 2024

Greetings! This directory contains a host of materials I either used or discussed during my Suricon 2024 talk:

 - My powerpoint slide deck
 - `siderator.py`
 - Cyberchef recipe for generating XOR rainbow table rules, based on system artifacts
 - links.md
 - disable.conf
 - enable.conf
 
## Informational_and_Honeytoken_Rules.pptx

- My Suricon 2024 slide deck. Pop this open to get access to my slide deck, and all of the links to various resources contained inside

## xor_rainbowtable_cyberchef_recipe.md

 - This is a markup file that contains instructions on how to reproduce the cyberchef recipe I used for creating a rainbow table of rules for a system artifact/value transformed by various XOR keys. The instructions are comprehensive, and include an example of the expected output via a link to the GCHQ cyberchef instance.
 
## siderator.py

 - This is a python script that will take the default output from the cyberchef recipe above, and assign proper, valid sid numbers to the rules generated. This script has three input options:
  - `-i` for input file (defaults to looking for the file `rules.txt` in the same directory as the `siderator.py` script
  - `-o` for output file (defaults to outputting the newly numbered rules to a file named `local.rules` in the same directory as the `siderator.py script
  - `-s` for starting sid number. This is for users who have a local.rules file and need to pick a different sid number to start from. By default, the starting sid value is `1000000`.
 - The newly generated `local.rules` file will likely need to be moved to the rules directory for your suricata instance, or otherwise imported into whatever tooling you use for managing your suricata rules. If you have an existing `local.rules` file, consider appending the rules you've generated to the existing `local.rules` file. Additionally, make sure that the `suricata.yaml` config file is configured to utilize the newly generated `local.rules` file this script generates. Doesn't do you any good if suricata doesn't know where to find the new rules!
 
## links.md
 
 - I cited a bunch of websites in the creation of my slide deck. Rather than make you dig out the links on your own, here is a markdown file containing all of the links in my slide deck by category
 
## disable.conf

 - this is a _very_ simple `disable.conf` file for `suricata-update`. This config file will disable **all** ET INFO rules.
 
## enable.conf

 - this is an `enable.conf` file for `suricata-update`. This config file enables a specific subset of ET INTO rules.
 