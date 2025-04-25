# Lana Musaffer || 1210455 
# Jana Sawalmeh || 1210122 
# Tariq Atrash  || 1210122 

from socket import *

portNum=6060 #server port
serverSocket = socket(AF_INET,SOCK_STREAM) #creating a TCP socket for incoming request
serverSocket.bind(('',portNum)) #associate the server port number with this socket
serverSocket.listen(1) #the server listen for TCP connection requests from the client with i queued connections
print ("The server is ready to receive") #print a message to tell the client that the server is ready to receive 

#start getting requests:
while True:
    connectionSocket, address = serverSocket.accept()     #when a client sends a TCP connection requests
    sent=connectionSocket.recv(2048).decode()     #create "connectionSocket" dedicated to this client
    print(address)
    IP= address[0]
    port=address[1]
    print("IP: "+ str(IP) +",Port: "+ str(port))
    print("********************************************************")
    print(sent)
    print("********************************************************")

    #if the sentence is not empty, the requested file is gotten from request header
    if sent !='':
        # Splitting the sentence by spaces and getting the second element (index 1)
        # which represents the requested file in the URL
        request_File=sent.split(' ')[1].replace('/','') 
        print("The request File is: "+request_File)

    #if the request is empty the connection is closed
    else:
        connectionSocket.close()
        continue

    try:

        #if the requested file is main.html or index.html or empty(default) or en
        if request_File == '' or request_File=='main_en.html' or request_File== 'index.html' or request_File=='en':
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/html \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            mhtml=open('main_en.html', 'rb')
            connectionSocket.send(mhtml.read())
            mhtml.close()

        #If the request is /ar then the server response with main_ar.html which is an Arabic version of main_en.html 
        elif  request_File=='ar':
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/html \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            mhtml=open('main_ar.html', 'rb')
            connectionSocket.send(mhtml.read())
            mhtml.close()

        #if the request is an .html file 
        elif '.html' in request_File:
            # then the server should send the requested html file with Content-Type: text/html.
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/html \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            f= open(str(request_File), 'rb')
            connectionSocket.send(f.read())
            f.close()
            
        #if the request is a .css file 
        elif '.css' in request_File:
            # then the server should send the requested css file with Content-Type: text/css.
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: text/css \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            f= open(str(request_File), 'rb')
            connectionSocket.send(f.read())
            f.close()

        #if the request is a .png 
        elif '.png' in request_File:
            #then the server should send the png image with Content-Type: image/png.
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: image/png \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            f= open(str(request_File), 'rb')
            connectionSocket.send(f.read())
            f.close()

        #if the request is a .jpg 
        elif '.jpg' in request_File:
            #then the server should send the jpg image with Content-Type: image/jpeg.
            connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send(f"Content-Type: image/jpeg \r\n".encode())
            connectionSocket.send(f"\r\n".encode())
            print('response status: 200 OK\n\n')
            f= open(str(request_File), 'rb')
            connectionSocket.send(f.read())
            f.close()

        #If the request is /so 
        elif request_File =='so':
            #then redirect to stackoverflow.com website
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            connectionSocket.send("Location: https://stackoverflow.com/\r\n".encode())

        #If the request is /itc
        elif request_File =='itc':
            # then redirect to itc website
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            connectionSocket.send("Location: https://itc.birzeit.edu/\r\n".encode())

        #this is a handler only in order not to get not found error
        elif 'favicon.ico'  ==request_File:
            print()  
        else:
            raise Exception('Not found')
        
    #if the file wrong or the file doesn’t exist 
    except Exception as e:
        #the server should return a simple HTML webpage that contains (Content-Type: text/html)
        connectionSocket.send(f"HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send(f"Content-Type: text/html \r\n".encode())
        connectionSocket.send(f"\r\n".encode())
        print(request_File +"test")
        print('\b\bResponse status: 404 Not Found')
        f='<!DOCTYPE html><html>' \
        '<style>*{ text-align: center; }' \
        '#Error{ color: red;}#name{ font-weight: bold;}</style>'\
        '<head>  <title>Error 404</title></head>' \
        '<body>  <div id="Error">   <h1>The file is not found</h1> </div>' \
        '<hr> <div id="name"> \
        <p> Lana Musaffer || 1210455     </p> \
        <p> Tariq Atrash  || 1210122   </p>' \
        '<p>Jana Sawalmeh || 1210122   </p> </div><hr> <div>' \
        '<p> IP Adress: '+ str(IP)+ ', Port Number of The Client: ' +str(port)+\
        '</p> </div> </body></html>'
        connectionSocket.send(f.encode())
    connectionSocket.close()