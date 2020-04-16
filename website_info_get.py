import socket
from termcolor import colored
import whois
import pprint


print("""
   ▄████████    ▄████████  ▄████████    ▄█    █▄     ▄█  ███▄▄▄▄   
  ███    ███   ███    ███ ███    ███   ███    ███   ███  ███▀▀▀██▄ 
  ███    █▀    ███    ███ ███    █▀    ███    ███   ███▌ ███   ███ 
  ███          ███    ███ ███         ▄███▄▄▄▄███▄▄ ███▌ ███   ███ 
▀███████████ ▀███████████ ███        ▀▀███▀▀▀▀███▀  ███▌ ███   ███ 
         ███   ███    ███ ███    █▄    ███    ███   ███  ███   ███ 
   ▄█    ███   ███    ███ ███    ███   ███    ███   ███  ███   ███ 
 ▄████████▀    ███    █▀  ████████▀    ███    █▀    █▀    ▀█   █▀  
                                                                   
""")

print(colored('---------------------DNS LOOKUP-----------------', 'blue'))
webiste_name = input("Enter the site Name :")
DNS_LOOKUP = socket.gethostbyname(webiste_name)
print(DNS_LOOKUP)

print(colored('---------------------WHO IS-----------------', 'blue'))

domain = whois.query(webiste_name)

pprint.pprint(domain.__dict__)


