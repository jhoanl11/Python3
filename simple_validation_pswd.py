special = "@#~*^()[]"

def validate_password(contrasena):
    validar = False
    validar2 = False
    if len(contrasena) < 8:
        raise ValueError("The password needs more than 8 caracters")
    for i in contrasena:
        if i in special:
            validar = True
        if i.isdigit(): 
            validar2 = True
    if validar2 == True and validar == True:
        print("Your password is valid, sh! dont shared")
    elif validar == False:
        raise TypeError("You need a special caracter in your password")
    elif validar2 == False:
        raise TypeError("You need a digit in yout password")


fel = input()
validate_password(fel)
