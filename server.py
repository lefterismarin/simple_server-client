import socket
import sys
from _thread import *					
import string
'''εδω τελειωνουν τα imports'''


	
'''δημιουργια socket server'''
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=50010

#δεσμευση host και θυρας
sock.bind((host,port))
print("Server waiting for connections...")
#αριθμος των clients που μπορουν να συνδεθουν παραλληλα
sock.listen(10)


	
'''thread για καθε συνδεδεμενο client'''
def client_thread(conn):
    first_message="Server>>Connected to Server" #στελνει μηνυμα σε οποιον client συνδεθει
    conn.send(first_message.encode())
    while 1:					#loop για συνεχη συνδεση με τον client
        message_rcv = conn.recv(1024)  			#αναμονη απαντησης απο τον client
        print("Client>>"+message_rcv.decode())
        response="Encrypted Message Received"  
        conn.sendall(response.encode())  #επιστρεφει το αποτελεσμα στον client
		  
    conn.close()

while 1:
    #περιμενει να συνδεθει καποιος client και οταν το κανει δημιουργει thread γι' αυτον
    conn, addr = sock.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))  #εκτυπωνει την διευθυνση του client που συνδεθηκε
    start_new_thread(client_thread, (conn,))

sock.close()


