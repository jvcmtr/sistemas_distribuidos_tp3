import socket
import random
from net_constants import *

def main(n=10, min_len=10, max_len=2000):
    print("_____________________________")
    print("    EXECUTANDO CLIENT UDP")
    print("- Criando socket...", end="")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Sucesso")
    
    print(f"- Iniciando o envio de {n} mensagens com conteudo aleatorio para o servidor:")
    errors = 0
    for i in range(10):
        try:
            size = random.randint(min_len, max_len)
            str = ''.join(["A" for x in range(size)])
            msg = f"{i+1} - {str}".encode()
        
            print(f"\t[{i+1}/{n}]Enviando mensagem {i} para o servidor {ADDR} ...", end="")
            s.sendto(msg, ADDR)
            print(f"Mensagem {i} enviada")
        except Exception as e:
            print("ERRO AO ENVIAR A MENSAGEM {i}")
            print(e)

    if not errors:
        print("- Mensagens enviadas com sucesso")
    else:
        print(f"- Erro no envio de {i}/{n} mensagens")
    print("- Fechando socket...", end="")
    s.close()
    print("Sucesso")

if __name__ == "__main__":
    main()