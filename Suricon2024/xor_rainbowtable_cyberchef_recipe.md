# Basic XOR Rainbow Table Recipe:

 - Step 1: XOR Brute Force - Key Length: 1 or 2, Check “Print Key”, Check “Output as Hex"

 - Step 2: Find and Replace - Find:'Key = ', Replace:'alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"XOR_HUNTING BERSERK MAC Address in HTTP POST XOR Key '

 - Step 3: Find and Replace - Find:': ', Replace:'"; flow:established,to_server; http.method; content:"POST"; http.request_body; content:"|'

 - Step 4: Find and Replace - Find:'$', Replace:'|"; classtype:misc-activity; sid:; rev:1;)'

## Notes:

 - Key Length 1 produces 255 rules 256 - 1 (key 0x00 is effectively worthless)

 - Key Length 2 produces 65535 rules 256^2 -1 (key 0x0000 is worthless)

 - the first find/replace (step 2) can be modified to change the header and rule message to change protocols, network vars, port vars, etc.
 
 - the second find/replace can be modified to change the `flow` option (e.g., `flow:established,to_server` or `flow:established,to_client`) or remove the `flow` option entirely. You can also change the sticky buffers or other rule options you would like to use for your rules as desired.

 - the third find/replace can be modified to change the `classtype`, add additional metadata tags (e.g., `reference` or `metadata`)

 - Typically, user-created rules are placed in a `local.rules` file. Locally created rules are typically assigned sids from 1000000 through 1999999 (see also: sidallocation.org)

 - Users will need to either user a script, or one-liner to replace the blank sid number with a sid in the allocation range. Users with existing local rules will need to determine the next available sid number to begin assigning these sids. I've included a simple python script for assigning sid numbers to rules generated using cyberchef in this manner named `siderator.py`

 - Either `suricata.yaml` will need to be modified to include the use of this new `.rules` file generated, or the new `.rules` file will need to have all of its rules appended to the existing `local.rules` file.

- Here is a link to a public cyberchef instance with example output to expect from these cyberchef transforms: https://gchq.github.io/CyberChef/#recipe=XOR_Brute_Force(1,12,0,'Standard',false,true,true,'')Find_/_Replace(%7B'option':'Regex','string':'Key%20%3D%20'%7D,'alert%20http%20$HOME_NET%20any%20-%3E%20$EXTERNAL_NET%20any%20(msg:%22XOR_HUNTING%20BERSERK%20MAC%20Address%20in%20HTTP%20POST%20XOR%20Key%20',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':':%20'%7D,'%22;%20flow:established,to_server;%20http.method;%20content:%22POST%22;%20http.request_body;%20content:%22%7C',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'$'%7D,'%7C%22;%20classtype:misc-activity;%20sid:;%20rev:1;)',true,false,true,false)&input=MDBFMDRDMjJCMURG
