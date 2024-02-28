import sys
import socket
import network

ssid = 'hotspotNetwork'
password = '12345'


ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid = ssid, password = password, authmode = network.AUTH_WPA_WPA2_PSK)

while ap.active() == False:
    pass

print('Connection successful')
status = ap.ifconfig()
print(status)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(1)


print('\nWAITING CONNECTION TO THE NETWORK, %s...' % str(ssid))
conn, addr = s.accept()
print('Got a connection from %s' % str(addr[0]))

# s.settimeout(10)
# try:
#     print('\nWAITING CONNECTION TO THE NETWORK, %s...' % str(ssid))
#     conn, addr = s.accept()
#     print('Got a connection from %s' % str(addr[0]))
# except:
#     print('TIME OUT')
#     sys.exit()


addrss = ''
try:
    print('\n')
    # https://docs.micropython.org/en/latest/library/network.html
    # WiFi AP: use 'stations' to retrieve a list of all the STAs connected to the AP.
    # The list contains tuples of the form (MAC, RSSI).
    stat = ap.status('stations')
    listSTA = list(stat[0])
    # Turns listSTA into a MAC address legible format (BSSID)
    addrss = listSTA[0].hex(":")
    print('STATUS, CLIENT BSSID: ', addrss)
except:
    print('NO CLIENT CONNECTED')

# The "if" condition can be avoided. If it is desired to use it so a specific client
# can interact with the server, the client MAC address must be changed on the
# conditional comparison
if addrss == '00:00:00:00:00:00':
    data = 'Message from the server'
    dataSend = data.encode('utf-8')
    conn.send(dataSend)
else:
    print('UNAUTHORIZED DEVICE')
    sys.exit()

print('\n')
recvData, address = conn.recvfrom(1024)
dataPrint = recvData.decode('utf-8')
print(str(dataPrint))
