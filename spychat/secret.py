import socket

def sendSecretMsg(IP_address, Port) :
    from steganography.steganography import Steganography

    org_img = raw_input("What is the name of the image?")
    op_path = 'output.jpg'
    msg = raw_input("What do you want to say?")
    Steganography.encode(org_img, op_path, msg)

    ADDR = (IP_address, Port)
    BUFSIZE = 4096
    imagefile = "output.jpg"

    bytes = open(imagefile).read()

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.connect(ADDR)
    serv.send(bytes)

    print "Image sent\n"

    serv.close()


def recvSecretMsg (IP_address, Port) :
    from steganography.steganography import Steganography

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((IP_address, Port))
    server.listen(5)
    print 'Listening for client...'

    while True:
        conn, addr = server.accept()
        print 'client connected ... ', addr
        myfile = open('secret.jpg', 'w')

        while True :
            data = conn.recv(4096)

            if not data: break
            myfile.write(data)
            print 'writing file ....'

    myfile.close()
    print "Finished writing."

    conn.close()

    secret_text = Steganography.decode("secret.jpg")

    return secret_text

