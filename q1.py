
import socket 

def test_socket(nome, familia, type):
    familia_nm = "IPv4" if familia == socket.AF_INET else "IPv6"
    type_nm = "TCP" if type == socket.SOCK_STREAM else "UDP"

    # Endereços de loopback
    HOST = '127.0.0.1' if familia == socket.AF_INET else '::1'
    PORT = 12345
    
    s = None
    details_str = f"\n\t- Protocolos:\t{familia_nm}/{type_nm}\n\t- Rede:\t\t{HOST}:{PORT}"
    try:
        print(f"____________________________________________")
        print(f"    INICIANDO TESTE {nome}")
        print(f"Iniciando socket com as seguintes configurações: {details_str}")
        
        s = socket.socket(familia, type)
        s.bind((HOST, PORT))

        print(f"Socket iniciado com sucesso: {details_str}")

    except OSError as e:
        print(f"[ERROR] Ocorreu uma falha com o SO: {e} {details_str}")
    except PermissionError:
        print(f"[ERROR] Permissão negada para porta {PORT}. {details_str}")
    except Exception as e:
        print(f"[ERROR] {e} {details_str}")
    finally:
        if s:
            s.close()
            print(f"Socket fechado com sucesso: {familia_nm}/{type_nm}")

if __name__ == "__main__":
    conf = [
        ("AF_INET + STREAM", socket.AF_INET, socket.SOCK_STREAM),
        ("AF_INET + DGRAM", socket.AF_INET, socket.SOCK_DGRAM),
        ("AF_INET6 + STREAM", socket.AF_INET6, socket.SOCK_STREAM),
        ("AF_INET6 + DGRAM", socket.AF_INET6, socket.SOCK_DGRAM)
    ]
    
    for c in conf:
        test_socket(*c)
