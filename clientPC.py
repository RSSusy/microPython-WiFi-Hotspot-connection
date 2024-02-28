import socket

clientTCP = socket.socket()
# ----------------------------------------------------------------------------------
# Knowing the IP address from the server (microcontroller) given by the status[0]
# from the server.py code, using the same port -> 80, we verify that there's
# connection between "Server" and "Client"
# ----------------------------------------------------------------------------------
socketInfo = socket.getaddrinfo('192.168.4.1', 80)[0][-1]
clientTCP.connect(socketInfo)
print('Conectado al Servidor: ', str(socketInfo))

print("\n")
recvData, address = clientTCP.recvfrom(1024)
dataPrint = recvData.decode('utf-8')
print(str(dataPrint))

data = 'Respuesta del Cliente'
dataSend = data.encode('utf-8')
clientTCP.send(dataSend)
