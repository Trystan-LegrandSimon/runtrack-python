#!/usr/local/bin/python3

chaine = "abcdefghijklmnopqrstuvwxyz" * 10


for i in range(len(chaine)):
    if i % 2 != 0:
        print(chaine[:i])
    
        
