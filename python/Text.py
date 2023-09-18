with open('ayush.txt','r') as file:
    text = file.read()
import re
ph_num = re.findall(r'\+91\d{10}',text)
email_adress = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',text)
print(ph_num)
print(email_adress)