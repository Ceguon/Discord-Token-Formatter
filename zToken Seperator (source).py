import threading
import random
import json
import time

TokensFull=open('TokensFull.txt','r').read().splitlines()
count=0
def formatter(TokenFull):
	len(TokenFull.split(':')) == 4
	splitted = TokenFull.split(':')
	email = f"{splitted[0]}"
	password = f"{splitted[1]}"
	token = f"{splitted[2]}"
	with open("Output.txt", "a") as f:
		f.write(f"{token}\n")
		f.close()
for TokenFull in TokensFull:threading.Thread(target=formatter,args=(TokenFull,)).start();count+=1
input(f"{count} Tokens Formatted")