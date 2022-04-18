import re


pattern = r"([^.][a-zA-Z0-9\s!#%&'*+-/=?^_`{|}.~])+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{,63}$"



def Validate_email(email):
    if re.fullmatch (pattern, email):
       print ("Email correct")
    else: 
       print ("Email uncorrect")

email1 = input("Введите своей email: ")
Validate_email(email1)