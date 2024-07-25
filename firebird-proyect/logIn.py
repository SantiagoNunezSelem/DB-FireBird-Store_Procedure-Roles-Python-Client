from connection import create_connection_db

def logIn():
    
    while True:
        print("--- Inicio de sesión ---\n")
        user = str(input("Ingrese el nombre de usuario: "))
        pwd = str(input("Ingrese la contraseña: "))
        role = str(input("Ingrese su rol: "))
        
        try:
            con = create_connection_db(user,pwd,role)
            break
        except:
            print("ERROR")
            print("CREDENCIALES INVALIDAS\n")

    return con