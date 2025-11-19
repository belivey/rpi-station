import sys
import time
import telnetlib

host = '192.168.1.1'
port = 4001
id = None

if len(sys.argv)>1:
    host = sys.argv[1]
    port = sys.argv[2]

if len(sys.argv) > 3:
    id = sys.argv[3]

try:
    tn = telnetlib.Telnet(host, port)

    if id != None:
        command = "@" + id + " M 0\r\n"
        tn.write(command.encode('ascii'))
    else:
        tn.write("M 0\r\n".encode('ascii'))
    time.sleep(3)

    data = tn.read_very_eager().decode('ascii')

    print(data)
    
    if id != None:
        command = "@" + id + " R\r\n"
        tn.write(command.encode('ascii'))
    else:
        tn.write("R\r\n".encode('ascii'))    
    
except:
    exit()
