'''
TO DO:
-MORSE TO TXT
-PRINT HORINZONTAL
'''
import time
dict_txt_to_morse = {"a":".-",

                    "b":"-...",
                    "c":"-.-.",
                    "d":"-..",
                    "e":".",
                    "f":"..-.",
                    "g":"--.",
                    "h":"....",
                    "i":"..",
                    "j":".---",
                    "k":"-.-",
                    "l":".-..",
                    "m":"--",
                    "n":"-.",
                    "o":"---",
                    "p":".--.",
                    "q":"--.-",
                    "r":".-.",
                    "s":"...",
                    "t":"-",
                    "u":"..-",
                    "v":"...-",
                    "w":".--",
                    "x":"-..-",
                    "y":"-.--",
                    "z":"--..",
                    "1":".----",
                    "2":"..---",
                    "3":"...--",
                    "4":"....-",
                    "5":".....",
                    "6":"-....",
                    "7":"--...",
                    "8":"---..",
                    "9":"----.",
                    "0":"-----",
                    " ":" / "}
def txt_to_morse(text):
    for text in text:
        print(dict_txt_to_morse[text])
while True:
    print("Enter the text to morse")
    text = input("->")
    txt_to_morse(text)