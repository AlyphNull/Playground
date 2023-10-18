"""Trying to confirm a palindrome"""


for i in range (5):


    word = input()
    wordlist = list(word)
    wordlist.reverse()  # Reverse the list in place
    A = ''.join(wordlist)

    if word == A:
        print("Palindrome")
    else:
        print("Not a palindrome")
