import sys
import time
import telnetlib

host = '192.168.1.1'
port = 4002
id = 41

if len(sys.argv)>1:
    host = sys.argv[1]
    port = sys.argv[2]

if len(sys.argv) > 3:
    id = sys.argv[3]

try:
    tn = telnetlib.Telnet(host, port)
    command = f"@{id} M 0\r\n"
    tn.write(command.encode('ascii'))
    time.sleep(3)
    data = tn.read_very_eager().decode('ascii')

    print(data)
    
except:
    exit()
