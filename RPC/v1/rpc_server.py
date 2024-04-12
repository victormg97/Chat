from xmlrpc.server import SimpleXMLRPCServer
import threading
import logging

# Configuración de registro
logging.basicConfig(filename='server_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_even(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
def cuadrado(n):
    f = open('datos.txt','w')
    # Agregar un registro al archivo de registro
    logging.info("El cuadrado de %d es %d" % (n, n ** 2))
    # Agregar un registro al archivo de datos
    f.write("El cuadrado de %d es %d" % (n, n ** 2))
    f.close()
    return n ** 2

def agregar(n):
    f = open('datos.txt','a')
    # Agregar un registro al archivo de registro
    # logging.info("El cuadrado de %d es %d" % (n, n ** 2))
    # Agregar un registro al archivo de datos
    f.write("El cuadrado de %d es %d\n" % (n, n ** 2))
    f.close()
    return ("Agregado")

def listado():
    f = open('datos.txt','r')
    # Agregar un registro al archivo de registro
    # logging.info("El cuadrado de %d es %d" % (n, n ** 2))
    # Agregar un registro al archivo de datos
    contenido = f.read()
    f.close()
    return contenido

def start_server():
    server = SimpleXMLRPCServer(("0.0.0.0", 8000))
    logging.info("Server started listening on port 8000...")
    server.register_function(is_even, "is_even")
    server.register_function(cuadrado, "cuadrado")
    server.register_function(agregar, "agregar")
    server.register_function(listado, "listado")
    server.serve_forever()

server_thread = threading.Thread(target=start_server)
server_thread.start()
server_thread.join()  # Espera a que el hilo del servidor termine antes de que el programa principal continúe
