import socket
from net_constants import *

def main(buffer_size=DEFAULT_BUFFER_SIZE, decode_format=DEFAULT_DECODE_FORMAT):
    print("_______________________________")
    print("    INICIANDO SOCKET UDP ")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(ADDR)
    print(f"- Socket ativo em: {ADDR}")

    while True:
        try:
            data, client = s.recvfrom(buffer_size)
            print("_______________________________")
            print(f"Conexão estabelecida: {client}")
            data = data.decode(decode_format)
            print(f"\t- Cliente                             : {client}")
            print(f"\t- Tamanho da mensagem                 : {len(data)} (caracteres)")
            print(f"\t- Primeiros 20 caracteres da mensagem : '{data[:20]}' (...)")
            print(f"\t- Retornando resposta...", end="")
            s.sendto(data.encode(decode_format), client)
            print(f"Sucesso")
        except Exception as e:
            print(f"\t[ERRO] Uma falha ocorreu ao processar uma mensagem: {e}")
            print(f"\nERRO conexão encerrada")
    print("- Fechando socket...", end="")
    s.close()
    print("Sucesso")

if __name__ == "__main__":
    main()