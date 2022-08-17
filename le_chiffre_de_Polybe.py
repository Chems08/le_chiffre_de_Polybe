import random


clef = []

alphabet_random = []



alphabet = [["A", "B", "C", "D", "E","F"], 
    ["G", "H", "I", "J", "K", "L"], 
    ["M", "N", "O", "P","Q", "R"], 
    ["S", "T", "U","V", "W", "X"], 
    ["Y", "Z", "0", "1", "2", "3"],
    ["4", "5", "6", "7", "8", "9"]]

#random de l'alphabet

for i in range(6):
    alphabet_random.append(random.sample(alphabet[i],len(alphabet)))

alphabet_random = random.sample(alphabet_random, len(alphabet_random))

print("\nL'alphabet est : \n",alphabet_random)



mot = input("Saisi ton mot en majuscule : ")
mot = mot.upper()
mot = list(mot)

# Si le mot saisi est "BONJOUR" --> mot = ["B","O","N","J","O","U","R"] 



for i in range(len(mot)):
    for k in range(len(alphabet_random)):
        for j in range(len(alphabet_random)):
            if mot[i] in alphabet_random[k][j]:
                print(alphabet_random[k][j], "=",k,j)
                clef.append([k,j])



print("clef : ",clef)



