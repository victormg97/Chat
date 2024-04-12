import xmlrpc.client
numero=0
with xmlrpc.client.ServerProxy("http://10.3.32.12:8000/") as proxy:

    while (numero>=0):
        numero=int(input("Ingrese una opción (1 Agregar un número, 2 Listar números, 3 Salir): "))
        if numero==1:
            num=int(input("Ingrese un número: "))
            print(proxy.agregar(num))
        elif numero==2:
            print(proxy.listado())
        elif numero==3:
            break
        else:
            print("Opción incorrecta")
        
    print("\nFin !!")