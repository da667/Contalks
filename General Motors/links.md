# Rule Category Definitions

 - https://community.emergingthreats.net/t/suricata-5-6-7-rule-categories/

# More about DNS over HTTPS

 - Dohdoor (2026) - https://blog.talosintelligence.com/new-dohdoor-malware-campaign/
 - ChamelGang (2023) - https://www.bleepingcomputer.com/news/security/chinese-hackers-use-dns-over-https-for-linux-malware-communication/
 - Dnstt - https://www.bamsoftware.com/software/dnstt/
 - Godoh - https://github.com/sensepost/godoh
 - https://detect.fyi/detecting-dns-over-https-30fddb55ac78
 - https://github.com/curl/curl/wiki/DNS-over-HTTPS#publicly-available-servers

# Experimental DNS over HTTP Hunting Rules

```
alert tls $EXTERNAL_NET 443 -> $HOME_NET any (msg:"Tracking Repeated Small TLS Segments"; dsize:<300; flowint:tls.smallpayload, +, 1; noalert; sid: 1000000; rev:1;)
alert tls $EXTERNAL_NET 443 -> $HOME_NET any (msg:"Tracking Repeated Small TLS Segments"; dsize:<300; flowint:tls.smallpayload, > 5; flow.age:>10; sid:1000001; rev:1;)
```

 - Warning: These rules do NOT perform well. Ensure hyperscan support is enabled. Consider changing prefilter from `mpm` to `auto`, and prefiltering on `dsize` and/or `flow.age`
 

# More about External IP Address Lookup Services

 - https://isc.sans.edu/diary/APIs+Used+by+Bots+to+Detect+Public+IP+address/29516/OpenSSH
 - https://community.emergingthreats.net/t/external-ip-lookup-rules/2838
 - Agent Tesla - https://blogs.blackberry.com/en/2021/06/threat-thursday-agent-tesla-infostealer-malware
 - Remcos RAT - https://www.cyfirma.com/research/the-persistent-danger-of-remcos-rat/
 - Snake Keylogger - https://www.splunk.com/en_us/blog/security/under-the-hood-of-snakekeylogger-analyzing-its-loader-and-its-tactics-techniques-and-procedures.html
 - Medusa RAT sample - https://www.virustotal.com/gui/file/f38bdee68cad802f724a05aa5bc9886b4c4491bf3e61905fb868b758d0e737ef/behavior
- External IP lookup services sigma rule - https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_susp_external_ip_lookup.yml
- List of External IP Lookup services - https://github.com/chubin/awesome-console-services


# More about pastebin-like services

 - https://socradar.io/top-5-paste-sites-used-by-threat-actors/
 - https://www.bleepingcomputer.com/news/security/malware-campaigns-deliver-payloads-via-obscure-paste-service/
 - https://github.com/lorien/awesome-pastebins


# More about URL shorteners

 - “Silent Librarian” https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta407-silent-librarian
 - https://www.kaspersky.com/blog/malicious-redirect-methods/50045/

# Collection of suspicious domains to watch out for, if they are NOT regularly being used by your organization:

 - https://github.com/BadSamuraiDev/bs-lists

# More about suricata-update

 - https://github.com/OISF/suricata-update
 - https://suricata-update.readthedocs.io/en/latest/
 
# More about canary tokens

 - https://canary.tools
 - https://canarytokens.org/generate
 - Offensive Countermeasures Book - https://www.amazon.com/Offensive-Countermeasures-John-Strand/dp/1974671690
 - Intrusion Detection Honeypots Book - https://www.amazon.com/Intrusion-Detection-Honeypots-through-Deception/dp/1735188301

# Get Cyberchef. Love Cyberchef.

 - https://github.com/gchq/CyberChef

# Keep in contact

 - Emerging Threats forum - https://community.emergingthreats.net
 - Join the Emerging Threats Discord - https://discord.gg/8ZGA6mtfYT
 - Collection of blog posts and books I've wrote, or am currently writing - https://discourse.ifin.network/t/nsm-and-virtual-labbing-mega-thread/319
  - Also consider joining IFIN, an independent threat intelligence sharing network Note: IFIN is not affiliated with Proofpoint, or Emerging Threats in any way.

# Are you using Dalton? You should probably use Dalton. Because its awesome.

 - https://github.com/secureworks/dalton 
 
# Consider taking a look at IoT Hunter - a tool for rapidly developing rules for IoT device exploits

 - https://github.com/EmergingThreats/iot-hunter