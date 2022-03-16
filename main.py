import random
from tqdm import tqdm
import numpy as np
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","W","X","Y","Z"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*",".","(",")"]
alphabet = alphabet+digits+symbols
#print(alphabet)
#print(len(alphabet))
lunghezza_pass = input("Quanto deve essere lunga la password?\n")
lunghezza_pass = int(lunghezza_pass)
password = np.tile(None,lunghezza_pass)
#print(password)
#print(lunghezza_pass)
affidabilità = input("Livello affidabilità password: [numero intero]\n")
affidabilità = int(affidabilità)
print("Your password is:")
counter = 0
container = []
for i in tqdm(range(int(affidabilità))):
    a = random.sample(alphabet,lunghezza_pass)
    container = container+a
    random.shuffle(container)
    #print(container)
print("################################################")
print(*random.sample(container,lunghezza_pass),sep="")
print("################################################")
k = input("Press enter to exit\n")