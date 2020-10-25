import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("did you mean %s instead? Enter Y if yes or N if no :" % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The Word does not exit. please Double check the Word "
        else:
            return "We dint understand you're Entry"
    else:
        return "The word does not exist. Please Double check the Word "

word = input("Enter the Word:\t")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
