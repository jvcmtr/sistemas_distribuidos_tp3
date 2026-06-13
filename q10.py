import socket
from net_constants import *
import time

def scan_ports(start_port, end_port, timeout=0.5, verbose=False):
    
    def prt(msg=""):
        if verbose:
            print(msg)

    open_ports = []
    size = end_port - start_port +1
    prt(f"Iniciando varredura de portas no host {IP}")
    prt(f"RANGE: {start_port} - {end_port}")
    prt()

    start = time.time()
    for i in range(size):
        port = start_port+i

        prt(f"[{i}/{size}] Testando porta {port}... ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        
        result = s.connect_ex((IP, port))
        if result == 0:
            open_ports.append(port)
            prt(f"[{i}/{size}] port {port} ABERTO")
        else:
            prt(f"[{i}/{size}] port {port} fechado")

        s.close()
    
    delta = time.time() - start
    return open_ports, delta

if __name__ == "__main__":
    start = 1
    end = 100
    portas, tempo = scan_ports(start, end, verbose=True)
    
    print(f"_____________________________")
    print(f"    VARREDURA FINALIZADA")
    print(f"Host: {IP}")
    print(f"Range: {start}  -  {end}")
    print(f"N Portas analizadas: {end-start+1}")
    print(f"N Portas abertas: {len(portas)}")
    print(f"Tempo total: {tempo:.2f} sec")
    print(f"Portas abertas encontradas:\n\t {portas}")