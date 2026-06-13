import socket
import threading
from net_constants import *

def run_client(name, msg, buffer_size=DEFAULT_BUFFER_SIZE, encoding=DEFAULT_DECODE_FORMAT):
    
    print(f"[{name}] TREAD INICIALIZADA PARA O CLIENTE: '{name}'")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[{name}] Socket estabelecido. Origem:{client.getsockname()}")

    msg = msg.encode(encoding)

    print(f"[{name}] Enviando mensagem: '{msg}'")
    client.sendall(msg)
    
    print(f"[{name}] Recebendo resposta do servidor...")
    response = client.recv(buffer_size)
    print(f"[{name}] Resposta recebida com sucesso: {response.decode(encoding)}")
    
    print(f"[{name}] Finalizando conexão.")
    client.close()

def main():
    dt = [
        ("A", "Olá"),
        ("B", "Olá mundo"),
        ("C", "Olá python"),
        ("D", "Olá monitor"),
        ("E", "Olá professor"),
    ]
    print("_____________________________________")
    print("    INICIALIZANDO CLIENTES TCP")

    for i in range(len(dt)) :
        try:
            name, msg = dt[i]
            t = threading.Thread(target=run_client, args=(name, msg,))
            print(f"[MAIN] Thread para o cliente {name} criada. ({i}/{len(dt)})")
            t.start()
        except Exception as e:
            print(f"[MAIN] Um erro ocorreu ao iniciar a tread para o cliente: {e}")




# Simulação de 5 clientes simultâneos
if __name__ == "__main__":
    main()