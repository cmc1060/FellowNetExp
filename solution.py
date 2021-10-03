from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):

    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    subject = "My subject\r\n"



    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    themailserver = ("smtp.gmail.com", 25)
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)
    clientSocket.listen(4)
    # Fill in start
    # Fill in end

    while True:
        recv = clientSocket.recv(port).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
        heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand.encode())
        recv1 = clientSocket.recv(port).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

        mailFromCommand = 'Mail From: <cmc1060@nyu.edu>\r\n'
        clientSocket.send(mailFromCommand.encode())
        recv2 = clientSocket.recv(port).decode()
    #print(MAILFROM)
    # Send MAIL FROM command and print server response.
    # Fill in start
    # Fill in end

    # Send RCPT TO command and print server response.
        rcptToCommand = 'RCPT TO: <ccampbell439@gmail.com>\r\n'
        clientSocket.send(rcptToCommand.encode())
        recv3 = clientSocket.recv(port).decode()
    #print(rcptToCommand)
    # Fill in start
    # Fill in end


    # Send DATA command and print server response.
        dataCommand = "This is my data\r\n"
        clientSocket.send(dataCommand.encode())
        recv4 = clientSocket.recv(1025).decode()
    #print(recv4)
    # Fill in start
    # Fill in end

    # Send message data.
        clientSocket.send(subject.encode())
        clientSocket.send(msg.encode())


    # Fill in start
    # Fill in end

    # Message ends with a single period.
        clientSocket.send(endmsg.encode())
        recv_msg = clientSocket.recv(1025)
    # Fill in start
    # Fill in end

    # Send QUIT command and get server response.
        quitCommand = "Quit\r\n"
        clientSocket.send(quitCommand.encode())
        recv5 = clientSocket.recv(1025).decode
        clientSocket.close()
    # Fill in start
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
