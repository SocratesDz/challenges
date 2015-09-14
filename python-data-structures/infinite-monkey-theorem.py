import string, random

letters = string.ascii_lowercase+" "

target = "methinks it is like a weasel"
best_guess = (0.0, "")

def generate():
    text = "".join([letters[random.randrange(len(letters))] for c in range(len(target))])
    return text

def score(randstr):
    # Scoring
    matches = 0
    common_letters = set(target) & set(randstr)
    if common_letters - set(target) == set():
        for i in range(len(target)-1):
            if randstr[i] == target[i]: matches += 1
    return ((matches/len(target))*100, randstr)

def unmatches(guess_str, target_str):
    unmatches = ""
    for i in range(len(target_str)):
        if(guess_str[i] not in target_str[i]):
            unmatches += guess_str[i]
    return unmatches

'''
Get unmatches...
Keep good string...
Get the quantity of unmatches and retrieve that quantity of letters
Check if some of them match with the missing letters
'''

def run():
    counter = 0
    global best_guess
    while best_guess[0] < 90:
        try_guess = score(generate())
        if(try_guess[0] > best_guess[0]):
            best_guess = try_guess
            print("Guess: %.2f%%; Phrase: %s" % (best_guess[0], best_guess[1]))
        counter += 1

if __name__ == '__main__':
    run()
