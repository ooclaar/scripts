#!/usr/bin/python3
# Script para se conectar em porta remota e fazer uma interação trocando a saida por um outro valor de entrada. 

import socket
import time

s = socket.socket()

ip = "IP AQUI"
port = 51265

s.connect((ip, port))

time.sleep(1)
msg = s.recv(1024).decode()

time.sleep(1)
s.send(str("y\n").encode())

time.sleep(1)
resp = s.recv(1024).decode()
time.sleep(1)

linhas = resp.splitlines()
quantoutput = len(linhas[1].split(","))
output = linhas[1]

print("P: " + output)

while True:

    if(quantoutput==1):
        output = output.replace('GORGE', 'STOP')
        output = output.replace('PHREAK', 'DROP')
        output = output.replace('FIRE', 'ROLL')
        print("R: "+ output)
        s.send(str(output + "\n").encode())
    else:
        output = output.replace('GORGE', 'STOP')
        output = output.replace('PHREAK', 'DROP')
        output = output.replace('FIRE', 'ROLL')
        output = output.replace(', ', '-')
        print("R: " + output)
        s.send(str(output + "\n").encode())
    
    time.sleep(1)

    resp = s.recv(1024).decode()
    linhas = resp.splitlines() 
    quantoutput = len(linhas[0].split(","))
    output = linhas[0]
    print ("P: " + output)
    
s.close()
