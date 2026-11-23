import random
import json
import sys 
import re

# LexiLands by Luca De Rosa, for CS50P final project, December 2024.
def main():

    # Introduction
    print("Welcome to LexiLands! How many rounds would you like to play? ")
    
    # Here we get the rounds using the get_rounds() function
    rounds = get_rounds()  

    # Now we load dataset from JSON file
    dataset = load_dataset("dataset.json")

    # initialise the score
    score = 0

    # Let's play as many rounds as specified.
    i = 0
    while i < rounds:
        result = play_round(dataset)
        score = score + int(result) #We update the score at every round. 
        i = i + 1 

    # Finally, we print the score:
    print(20*"*")
    print(f"SCORE: {score} out of {rounds}")
    print(20*"*")
    


def get_sample(default = 5, arguments = None):
    if arguments is None: 
        arguments = sys.argv
        # This is a trick we use. We don't need the variable arguments in the main. But it is useful that we are able
        # to pass a parameter to get_sample when we are testing
    try:
        if len(arguments) < 2:
            return default # i.e. if we don't write an additional inline argument, we just use the default.
        
        
        sample_size = int(arguments[1])
        if sample_size <= 0:
            return default
        if sample_size > 30: # We set a limit to 30. This is an improvable limit depending on the size of our dataset.
            return 30
        return  sample_size
    except (ValueError, IndexError):
        return default


def get_rounds(): # This fuction asks the user for the number of rounds they want to play. It returns the rounds as an integer.
    pattern = r"^\d+$"
    while True:
        rounds = input("How many rounds would you like to play? \n")
        match = re.search(pattern, rounds) # We check, using regular expressions, that the input string is a non negative integer number.
        if match:
            return int(rounds) # If the input matches the regular expression, we return it, as in int
        print("Invalid input. Please insert a positive integer.")


def load_dataset(file_path): # This functino loads the data set. It takes as input a file path, and gives as output a loaded json.
    # We use the "with open ... as" construct as seen in class.
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    

def check_round(entry, guess): # This function takes as input an entry (that we imagine being taken at random) and a guess. It check if the guess
    # mathces the random country or language, and return 1 or 0 accordingly.
    language = entry["language"]
    country = entry["country"]
    if (any(guess.lower() == x.lower() for x in language)) or (any(guess.lower() == x.lower() for x in country)):
        return 1
    return 0


def play_round(dataset): #This function picks a random entry from the dataset, and plays a round, i.e. shows you some random cities from the entry
    # and asks you to guess. It returns an int value: 1 if the answer given is correct or 0 if not. If the random entry is, say Italy, both 
    # "italy" and "italian" are accepted as correct. Moreover, The answers are stripped of white spaces and case insensitive.
    try:
        entry = random.choice(dataset)
        language = entry["language"]            
        country = entry["country"]
        sample_size = get_sample()
        cities = random.sample(entry["city"], sample_size)
        alphabet = entry["alphabet"]
        print(f"""-------------------------------------------------------------------------------------
        \n Guess the country/language from these cities and alphabet: \n \n {", ".join(cities)} 
        \n Alphabet: {alphabet} \n""")

        guess = input("Your guess: ").strip()
        result = check_round(entry, guess)

        if result == 1:
            print("\033[32m CORRECT! \033[0m")
            return 1 # We assign 1 here so that we can count the score
        else:
            print(f"\033[31m WRONG! \033[0m The correct answer is {', '.join(country).upper()}, speaking {', '.join(language)}.")
            print()
            return 0
            
    except EOFError: # We want to interrupt when we press control + D.
        sys.exit()



if __name__ == "__main__":
    main()
