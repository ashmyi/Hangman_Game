import random

word_list = ["peach", "banana", "football", "cat"]

word = (random.choice(word_list))

placeholder = ["_"] * len(word) #cria uma lista do tamanho da palavra com _

placeholder_list = list(placeholder) #transfomra em uma lista

letters_guessed = set() #conjunto p armazenar as letras 

tries = int(len(word)) #tentativas no tamanho da palavra escolhida

print("The mystery word is: ", end= " ")
print(" ".join(placeholder_list))
print(f"You have {tries} tries.")


while tries > 0 and "_" in placeholder_list:
    guess = input("Guess a letter: ".lower())
    
    if guess in letters_guessed:
        print (f"You already guessed {guess}, try again.")
        continue #pq esse if e sempre verdadeiro, entao vai ficar loop pra sempre
    
    letters_guessed.add(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                placeholder_list[i] = guess
                print(" ".join(placeholder_list))
    else:
        tries -= 1
        print(f"You guessed {guess}, it's not in the word. You got {tries} tries left.")
    


if "_" not in placeholder_list:
    print("Congratulations, you won the game!")
else:
    print("You lost all of your tries! Game Over!" + f" The correct word was {word}")
    


