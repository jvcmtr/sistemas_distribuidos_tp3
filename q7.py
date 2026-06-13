import socket
import ssl
import pprint
import base64

PORT = 443
HOST = "www.google.com"

def print_cert(bytes):
    s = base64.encodebytes(bytes).decode("ascii")
    print(
        "-----BEGIN CERTIFICATE-----\n"
        + s +
        "-----END CERTIFICATE-----\n"
    )

def print_issuer(data, prefix=""):
    for i in data:
        for j in i:
            print(prefix + f"{j[0]} : {j[1]}")


def get_tls_info(hostname, port):

    context = ssl.create_default_context()
    s, s_ssl = None, None

    try:
        s = socket.create_connection((hostname, port))
        s_ssl = context.wrap_socket(s, server_hostname=hostname)
        cert = s_ssl.getpeercert()

        print(f"--- Informações de Conexão TLS com '{hostname}' ---")
        print(f"    - Versão TLS : {s_ssl.version()}")
        print(f"    - Cipher     : {s_ssl.cipher()[0] }")
        print(f"    - Issuer     : ")
        print_issuer(cert['issuer'], prefix="\t")
        print(f"    - Validade   : {cert['notBefore']}    -    {cert['notAfter']}")
        print_cert(s_ssl.getpeercert(binary_form=True))
    
    except Exception as e:
        print(f"    [ERRO] Um erro aconteceu ao estabelecer a conexão TLS com {hostname}:{port} \n{e}")
    finally:
        print(f"    Finalizando programa...")
        if s_ssl: s_ssl.close()
        elif s: s.close()

if __name__ == "__main__":
    get_tls_info(HOST, PORT)