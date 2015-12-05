import re
import requests

with open('links.txt', 'r') as f:
    text = f.read()
links = text.split('\n')
#print(links)
contacts = []
for link in links:
    page = requests.get(link).text
    emails = re.findall('[\w.]+@[\w.]+', page)
    for adress in emails:
        if adress not in contacts:
            contacts.append(adress)

email_list = open('email_adresses.txt', 'w')
for email in contacts:
    email_list.write(email)
    email_list.write('\n')
email_list.close()
