import sys
import time
import telnetlib

host = '192.168.1.26'
port = 4002

if len(sys.argv)>1:
    host = sys.argv[1]
    port = sys.argv[2]

try:
    tn = telnetlib.Telnet(host, port)


    # tn.write(chr(27).encode('ascii'))
    # time.sleep(1)
    tn.write("@2 MES 2\r\n".encode('ascii'))
    time.sleep(1)
    data = tn.read(100).decode('ascii')
    time.sleep(1)
    tn.write("@2 MES 3\r\n".encode('ascii'))
    time.sleep(1)
    data = data + tn.read(100).decode('ascii')

    print(data)


except:
    exit()