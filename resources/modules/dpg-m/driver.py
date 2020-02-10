import sys
import time
import telnetlib

host = '192.168.1.1'
port = 4002

if len(sys.argv)>1:
    host = sys.argv[1]
    port = sys.argv[2]

try:
    tn = telnetlib.Telnet(host, port)

    tn.write("@1 M\r\n".encode('ascii'))
    time.sleep(3)

    data = tn.read_very_eager().decode('ascii')

    print(data)


except:
    exit()
