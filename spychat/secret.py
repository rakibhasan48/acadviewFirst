import socket

def sendSecretMsg(IP_address, Port) :
    from steganography.steganography import Steganography

    org_img = raw_input("What is the name of the image?")
    op_path = 'output.jpg'
    msg = raw_input("What do you want to say?")
    Steganography.encode(org_img, op_path, msg)

    ADDR = (IP_address, Port)
    imagefile = open('output.jpg', 'rb')

    bytes = imagefile.read(1024)

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.connect(ADDR)
    print "Sending..."

    while bytes :

        serv.send(bytes)
        bytes = imagefile.read(1024)

    imagefile.close()

    print "Image sent\n"

    serv.shutdown(socket.SHUT_WR)

    serv.close()


def recvSecretMsg (IP_address, Port) :
    from steganography.steganography import Steganography

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((IP_address, Port))
    server.listen(5)
    print 'Listening for client...'

    myfile = open('secret.jpg', 'wb')

    while True:
        conn, addr = server.accept()
        print 'client connected ... ', addr

        data = conn.recv(1024)

        print 'Receiving file ....'

        while data :
            myfile.write(data)
            data = conn.recv(1024)

        myfile.close()
        print "Finished writing."

        conn.close()
        break

    secret_text = Steganography.decode("secret.jpg")

    return secret_text

