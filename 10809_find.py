word = input()
alphabet = list(range(97, 123))    # ASCII CODE
for i in alphabet:
    print(word.find(chr(i)))
