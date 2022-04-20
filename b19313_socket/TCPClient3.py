"""
    Python 3
    Usage: python3 TCPClient3.py localhost 12000
    coding: utf-8
    
    Author: Wei Song (Tutor for COMP3331/9331)
"""
from socket import *
import sys


login_flag = 0
task_flag = 0


def verify_credential(clientSocket):
    global login_flag
    # print('1. login_flag=', login_flag)
    username = input("Enter username: ")
    clientSocket.send(username.encode())
    username_msg = clientSocket.recv(2048).decode()
    if username_msg == "username exists":
        password = input("Enter password: ")
        clientSocket.send(password.encode())
        password_msg = clientSocket.recv(2048).decode()
        if password_msg == "OK":
            print("Welcome to the forum")
            login_flag = 1
            # print('2.login_flag=', login_flag)
        else:
            print("invalid password")

            verify_credential(clientSocket)

    elif username_msg == "username not found":
        password = input(f"Enter new password for {username}: ")
        clientSocket.send(password.encode())
        password_msg = clientSocket.recv(2048).decode()
        if password_msg == "just so so":
            print(f"new user {username} created")
            login_flag = 1


def run_cmd(clientSocket):
    global task_flag
    task = input(
        "Enter one of the following commands: CRT, MSG, DLT, EDT, LST, RDT, UPD, DWN, RMV, XIT, SHT:"
    )

    if task == "XIT":
        clientSocket.send(task.encode())
        print("Goodbye")
        clientSocket.close()
        task_flag = 1

    elif "CRT" in task:
        clientSocket.send(task.encode())
        print(clientSocket.recv(2048).decode())

    elif task == "LST":
        clientSocket.send(task.encode())
        msg = clientSocket.recv(2048).decode()
        if msg == "There is no active threads":
            print(msg)
        else:
            print(msg)
            clientSocket.send("active threads".encode())
            listContent = clientSocket.recv(2048).decode()
            print(listContent)

    elif "MSG" in task:
        clientSocket.send(task.encode())
        taskContent = task.split(" ")[2:]
        taskContent = " ".join(taskContent)
        threadNumber = task.split(" ")[1]
        if clientSocket.recv(2048).decode() == "thread exist":
            print(f"Message posted to {threadNumber} thread")
        else:
            print(f"{threadNumber} not exist")

    elif "RDT" in task:
        clientSocket.send(task.encode())
        taskContent = clientSocket.recv(2048).decode()
        print(taskContent)

    elif "RMV" in task:
        clientSocket.send(task.encode())
        taskContent = clientSocket.recv(2048).decode()
        print(taskContent)

    elif "DLT" in task:
        clientSocket.send(task.encode())
        taskContent = clientSocket.recv(2048).decode()
        print(taskContent)

    elif "EDT" in task:
        clientSocket.send(task.encode())
        taskContent = clientSocket.recv(2048).decode()
        print(taskContent)

    elif "UPD" in task:
        clientSocket.send(task.encode())
        taskContent = clientSocket.recv(2048).decode()
        print(taskContent)

    elif "DWN" in task:
        clientSocket.send(task.encode())
        fileName = task.split(" ")[2]
        taskContent = clientSocket.recv(2048).decode()
        if taskContent == "all ready":
            with open(fileName, mode="a+") as wf:
                wf.write(taskContent)
            print(f"{fileName} successfully downloaded")
        else:
            print(taskContent)

    else:
        print("Incorrect command")


def main():
    global login_flag
    # Server would be running on the same host as Client
    if len(sys.argv) != 3:
        print(
            "\n===== Error usage, python3 TCPClient3.py SERVER_IP SERVER_PORT ======\n"
        )
        exit(0)
    serverHost = sys.argv[1]
    serverPort = int(sys.argv[2])
    serverAddress = (serverHost, serverPort)

    login_flag = 0
    # define a socket for the client side, it would be used to communicate with the server
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # build connection with the server and send message to it
    clientSocket.connect(serverAddress)

    while True:
        print("===== Please type any messsage you want to send to server: =====\n")
        # message = input("===== Please type any messsage you want to send to server: =====\n")
        # clientSocket.sendall(message.encode())

        # # receive response from the server
        # # 1024 is a suggested packet size, you can specify it as 2048 or others
        # data = clientSocket.recv(1024)
        # receivedMessage = data.decode()

        # # parse the message received from server and take corresponding actions
        # if receivedMessage == "":
        #     print("[recv] Message from server is empty!")
        # elif receivedMessage == "user credentials request":
        #     print("[recv] You need to provide username and password to login")
        # elif receivedMessage == "download filename":
        #     print("[recv] You need to provide the file name you want to download")
        # else:
        #     print("[recv] Message makes no sense")

        # ans = input('\nDo you want to continue(y/n) :')
        # if ans == 'y':
        #     continue
        # else:
        #     break
        
        # print("main login_flag=", login_flag)
        if login_flag == 0:
            verify_credential(clientSocket)
        else:
            break

    while True:
        if task_flag == 0:
            run_cmd(clientSocket)
        else:
            break
    # close the socket
    clientSocket.close()


if __name__ == "__main__":
    main()
