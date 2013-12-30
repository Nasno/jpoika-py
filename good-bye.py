#from string import *
def anti_vowel(text):
    n=""
    for c in "aeiou":
        text=text.replace(c,n)
        text=text.replace(c.upper(),n)
    return text
    
print(anti_vowel("Hello World"))
print("Hello World".replace("Hello","Good-Bye"))

