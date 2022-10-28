from codecs import utf_8_decode
from email import message
import socket
import os
import sys



os.system("title S.F.W CHAT")
os.system("cls")

ip = str(input("insert ip: "))
os.system("cls")
print("""
  █████████  ███████████ █████   ███   █████      █████████  █████   █████   █████████   ███████████
 ███░░░░░███░░███░░░░░░█░░███   ░███  ░░███      ███░░░░░███░░███   ░░███   ███░░░░░███ ░█░░░███░░░█
░███    ░░░  ░███   █ ░  ░███   ░███   ░███     ███     ░░░  ░███    ░███  ░███    ░███ ░   ░███  ░ 
░░█████████  ░███████    ░███   ░███   ░███    ░███          ░███████████  ░███████████     ░███    
 ░░░░░░░░███ ░███░░░█    ░░███  █████  ███     ░███          ░███░░░░░███  ░███░░░░░███     ░███    
 ███    ░███ ░███  ░      ░░░█████░█████░      ░░███     ███ ░███    ░███  ░███    ░███     ░███    
░░█████████  █████          ░░███ ░░███         ░░█████████  █████   █████ █████   █████    █████   
 ░░░░░░░░░  ░░░░░            ░░░   ░░░           ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░   ░░░░░    ░░░░░    """)
print("author: SysFuckedWorld")
server = socket.socket()


server.bind((ip, 7070))
server.listen()
print(" use [exit] for exit the chat")
client, addr = server.accept()
done = False

while not done:


     msg = client.recv(1024).decode("utf-8")
     if msg == "exit":
        done = True
     else:
      print(msg)
      client.send(input("message: ").encode("utf-8"))

