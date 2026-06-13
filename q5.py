import socket
from net_constants import *

NOT_FOUND = "<html><body><h1>404 Not Found</h1></body></html>"
PATHS = {
    "/": "<html><body><h1>HOME</h1></body></html>",
    "/foo": "<html><body><h1>FOO</h1></body></html>"
}

def http_response(content, encode=DEFAULT_DECODE_FORMAT):
    content_length = len(content.encode(encode))
    return (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {content_length}\r\n" 
        + "Connection: close\r\n"
        + "\r\n"
        +f"{content}").encode(encode) 

def handle_http_request(conn, buffer_size=DEFAULT_BUFFER_SIZE, encode=DEFAULT_DECODE_FORMAT):
    print("__________")
    print(" Nova requisição recebida")
    request = conn.recv(buffer_size).decode(encode)
    if not request: return
    
    path = request.split()[1]
    
    if PATHS.get(path):
        body = PATHS[path]
    else:
        body = NOT_FOUND
    
    print(f"\t- path: '{path}'")
    print(f"\t- resposta: '{body}'")
    conn.sendall(http_response(body, encode))
    conn.close()

def main():
    print("_______________________________")
    print("    INICIANDO SERVIDOR HTTP ")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(ADDR)
        s.listen()
        print(f"- Servidor rodando em http://{ADDR[0]}:{ADDR[1]}")

        while True:
            try:
                conn, _ = s.accept()
                handle_http_request(conn)
            except Exception as e:
                print(f"\t[ERRO] Uma falha ocorreu ao processar uma requisição:")
                print(f"{e}")
                break
    except KeyboardInterrupt:
        print("\n...Finalizando programa ")
    finally:
        if s: s.close()

if __name__ == "__main__":
    main()