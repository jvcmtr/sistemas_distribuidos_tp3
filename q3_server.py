import socket
import threading
from net_constants import *


def handle_client(conn, addr, buffer_size=DEFAULT_BUFFER_SIZE, format=DEFAULT_DECODE_FORMAT):
    ip, porta = addr
    try:
        while True:
            data = conn.recv(buffer_size)
            if not data: break
            print(f"\t[THREAD][{porta}] Dados recebidos do cliente: {data.decode(format)}")
            conn.sendall(data)
            print(f"\t[THREAD][{porta}] Eccho dos dados realizados com sucesso")
    except Exception as e:
        print(f"\t[ERRO][{porta}] Um erro ocorreu ao PROCESSAR a mensagem do cliente {addr}.\n ERRO:{e}")
    finally:
        conn.close()
        print(f"\t[THREAD][{porta}] Conexão encerrada com o cliente: {ip}:{porta}")
    pass

def main():

    print("_______________________________")
    print("    INICIANDO SOCKET TCP ")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(ADDR)
    s.listen()
    print(f"- Socket ativo em: {ADDR[0]}:{ADDR[1]}")

    while True:
        try:
            client = s.accept()
            t = threading.Thread(target=handle_client, args=client)
            t.start()
            print(f"\t[SERVER] Nova conexão estabelecida: {client[1][0]}:{client[1][1]}\t [{threading.active_count()-1} conexões ativas]")
       
        except Exception as e:
            if client:
                print(f"\t[ERRO] Um erro ocorreu ao receber a mensagem do cliente {client}.\n ERRO:{e}")
            else:
                print(f"\t[ERRO] Não foi possivel estabelecer conexão com o cliente.\n ERRO:{e}")
    
    print("- Fechando socket...", end="")
    s.close()
    print("Sucesso")


if __name__ == "__main__":
    main()