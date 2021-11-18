from socket import *
import sys

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)
	
# Create a server socket, bind it to a port and start listening
serverport=8888
serverip=sys.argv[1]
tcpSerSock = socket(AF_INET, SOCK_STREAM)
addr1=(serverip,serverport)
tcpSerSock.bind(addr1)
tcpSerSock.listen(5)

# Fill in start

# Fill in end

while 1:
	# Strat receiving data from the client
	print('Ready to serve...')
	#tcpCliSock.connect(servername,serverport)
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)
	message =tcpCliSock.recv(1024) 
    # Fill in start
            
              # Fill in End
	print(message)
	# Extract the filename from the given message
	print message.split()[1]
	filename = message.split()[1].partition("/")[2]
	print(filename)
	fileExist = "false"
	filetouse = "/" + filename
	print(filetouse)
	try:
		# Check wether the file exist in the cache
		f = open(filetouse[1:], "r")                      
		outputdata = f.readlines()                        
		fileExist = "true"
		j=len(outputdata)
		# ProxyServer finds a cache hit and generates a response message
		tcpCliSock.send("HTTP/1.0 200 OK\r\n")            
		tcpCliSock.send("Content-Type:text/html\r\n")
		tcpCliSock.send("Content-Type:image/html\r\n")
		for i in range(0, len(outputdata)):
                    tcpCliSock.send(outputdata[i])
        # Fill in start
       
        # Fill in end
       # print('Read from cache')   
	# Error handling for file not found in cache
	except IOError:
		if fileExist == "false":
			c = socket(AF_INET,SOCK_STREAM)
            

                # Fill in end
			hostn = filename.replace("www.","",1)
			print(hostn)                                   
			try:
				c.connect((hostn,80))
				# Connect to the socket to port 80
				#proxyserver should connect to the server in order to get the requested item
                # Fill in start
                
                
                
                # Fill in end
				# Create a temporary file on this socket and ask port 80 for the file requested by the client
				fileobj = c.makefile('r', 0)               
				fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")
				bufff = fileobj.readlines()
				result = []
				for line in bufff:
					l = line.replace('href="/','href="http://' + filename + '/')
					l = l.replace('src="/','href="http://' + filename + '/')
					result.append(l)  
				# Read the response into buffer
                # Fill in start
                
                # Fill in end
				# Create a new file in the cache for the requested file. Also send the response in the buffer to client socket and the corresponding file in the cache
				tmpFile = open("./" + filename,"wb")
				for i in result:
					tmpFile.write(i)
					tcpCliSock.send(i)
                # Fill in end
			except Exception as inst:
				print ('Illegal request');
				print (inst);
				                                               
		else:
			tcpCliSock.shutdown()
			tcpSerSock.shutdown()
			tcpCliSock.close()
			tcpSerSock.close() 
# Fill in start
    
# Fill in end
