import socket
import sys
import string
'''εδω τελειωνουν τα imports'''



'''δημιουργει συνδεση με τον server'''
sock=socket.socket()
host=socket.gethostname()
port=50010

sock.connect((host,port))

message=sock.recv(1024)  #παραλαβη μηνυματος απο τον server
message=message.decode()	#μετατροπη απο bytes σε string
print(message)
while 1:
	send_message=input(str(">>"))  #ο client γραφει το μηνυμα το οποιο θελει να δει ΜΟΝΟ ο server
	send_message = send_message.encode() #το μηνυμα αυτο παιρνει την μορφη bytes
	sock.sendall(send_message)
	incoming_message=sock.recv(1024)
	incoming_message=incoming_message.decode()
	print("Server>>"+incoming_message)
sock.close()

			

    


	

   

	           
