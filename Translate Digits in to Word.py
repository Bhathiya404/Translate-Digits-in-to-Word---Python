
# Translate Digits in to Word in a phone number

phone=input("Phone: ")

digits_mapping={

    "1": "one",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"six",
    "7":"seven",
    "8":"Eight",
    "9":"Nine",
    "0":"zero"
}
output=""
for character in phone:
    output =output+digits_mapping.get(character,"!") + " "
print(output)