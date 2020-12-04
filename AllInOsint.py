import webbrowser
import os
print("Tüm Sorumluluğu Kabul Ettiniz.")
os.system("sudo apt-get install figlet")
os.system("figlet AllInOsint By Arda6 ")
print("""

1) Usernames
2) Email Adress
3) Domain Name
4) Ip Adress 
5) Images / Videos / Docs
6) Social Networks



""")
islem = input("Seçim Yapın :")
if islem == '1': 
 print("""  
      
    1) Namechk
    2) KnowEm
    3) NameCheckr
    4) UserSearch.org
    5) WhatsMyName
    6) Thats Them 
    7) Check Usernames
    8) Name Check Up

""")
username = input("Seçim Yapın :")
if username == '1':
    webbrowser.open_new("https://namechk.com")