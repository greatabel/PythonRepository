from socket import *
from threading import Thread
import sys, select
from collections import defaultdict
import os


def mycheck_start(serverSocket, threadList, fileList, userFileList, msgList):
    userNameList = []
    usernamePasswordList = []
    if os.path.isfile("credentials.txt") == True:
        with open("credentials.txt") as open_file:
            for line in open_file.readlines():
                line = line.split("\n")
                name_password = line[0].split(" ")

                username = name_password[0]
                password = name_password[1]
                userNameList.append(username)
                usernamePasswordList.append(username + " " + password)

    print("Waiting for clients")
    clientSocket, addr = serverSocket.accept()
    while True:
        username = clientSocket.recv(2048).decode()
        if username in userNameList:
            clientSocket.send("username exists".encode())
            password = clientSocket.recv(2048).decode()
            if username + " " + password in usernamePasswordList:
                print(f"{username} successful login")
                clientSocket.send("OK".encode())
                make_cmd_real(
                    username, clientSocket, threadList, fileList, userFileList, msgList
                )
            else:
                print("incorrect password")
                clientSocket.send("password incorrect".encode())
        else:
            clientSocket.send("username not found".encode())
            print("New user")
            password = clientSocket.recv(2048).decode()
            usernamePasswordList.append(username + " " + password)
            with open("credentials.txt", mode="a+") as open_file:
                open_file.write("\n" + username + " " + password)
            if username + " " + password in usernamePasswordList:
                print(f"{username} successfully logged in")
                clientSocket.send("just so so".encode())
                make_cmd_real(
                    username, clientSocket, threadList, fileList, userFileList, msgList
                )


def make_cmd_real(username, clientSocket, threadList, fileList, userFileList, msgList):
    while True:
        task = clientSocket.recv(2048).decode()
        taskCommand = task.split(" ")[0]
        try:
            if taskCommand == "XIT":
                print(f"{username} exited")
                mycheck_start(serverSocket, threadList, fileList, userFileList, msgList)

            elif taskCommand == "CRT":
                print(f"{username} issued {taskCommand} command")
                taskContent = task.split(" ")[1]
                if os.path.isfile(taskContent) == True:
                    print(f"Thread {taskContent} exists")
                    clientSocket.send(f"Thread {taskContent} exists".encode())

                else:
                    print(f"Thread {taskContent} created")
                    threadList.append(taskContent)
                    userFileList[username].append(taskContent)

                    clientSocket.send(f"Thread {taskContent} created".encode())
                    createFile = open(f"{taskContent}", mode="x")
                    createFile.close()

            elif taskCommand == "LST":
                print(f"{username} issued {taskCommand} command")
                if len(threadList) == 0:
                    clientSocket.send("There is no active threads".encode())
                else:
                    clientSocket.send("The list of active threads:".encode())
                    clientSocket.recv(2048).decode()
                    content = ""
                    for i in threadList:
                        content += i
                        content += "\n"
                    clientSocket.send(content.encode())

            elif taskCommand == "MSG":
                print(f"{username} issued {taskCommand} command")
                taskNumber = task.split(" ")[1]
                if taskNumber in threadList:
                    print(f"Message posted to {taskNumber} thread")
                    clientSocket.send("thread exist".encode())
                    writeFile = open(taskNumber, mode="a+")
                    taskContent = " ".join(task.split(" ")[2:])
                    messageNumber = get_msg_number(taskNumber)
                    writeFile.write(
                        str(messageNumber) + " " + username + ": " + taskContent + "\n"
                    )
                    writeFile.close()
                    msgList.append(
                        str(messageNumber) + " " + username + ": " + taskContent + "\n"
                    )
                else:
                    print(f"{taskNumber} not exist")
                    clientSocket.send("thread not exist".encode())

            elif taskCommand == "RDT":

                print(f"{username} issued {taskCommand} command")
                taskNumber = task.split(" ")[1]
                if taskNumber in threadList:
                    print(f"Thread {taskNumber} read")
                    with open(taskNumber) as openFile:
                        if os.path.getsize(taskNumber) == 0:
                            clientSocket.send(f"Thread {taskNumber} is empty".encode())
                        else:
                            content = ""
                            for line in openFile:
                                content += line
                            clientSocket.send(content.encode())

                else:
                    print(f"{taskNumber} not exist")
                    clientSocket.send("thread not exist".encode())

            elif "RMV" in task:
                taskCommand = task.split(" ")[0]
                print(f"{username} issued {taskCommand} command")
                threadNumber = task.split(" ")[1]
                if threadNumber not in userFileList[username]:
                    print(f"Thread {threadNumber} cannot be removed")
                    clientSocket.send(
                        "The thread was created by another user and cannot be removed".encode()
                    )
                else:
                    os.remove(threadNumber)
                    threadList.remove(threadNumber)
                    for i in msgList:
                        if i.split(" ")[1] == threadNumber + ":":
                            msgList.remove(i)
                    print(f"Thread {threadNumber} removed")
                    clientSocket.send("The thread has been removed".encode())

            elif taskCommand == "DLT":
                taskCommand = task.split(" ")[0]
                print(f"{username} issued {taskCommand} command")
                threadNumber = task.split(" ")[1]
                taskNumber = task.split(" ")[2]
                if threadNumber not in threadList:
                    print("Thread number is not existed and message cannot be deleted")
                    clientSocket.send("Message cannot be deleted".encode())
                # 只能读到这里 helperfunction错了
                else:
                    match_task_number(
                        clientSocket, threadNumber, taskNumber, username, msgList
                    )

            elif taskCommand == "EDT":
                print(f"{username} issued {taskCommand} command")
                threadNumber = task.split(" ")[1]
                taskNumber = task.split(" ")[2]
                taskContent = task.split(" ")[3:]
                taskContent = " ".join(taskContent)
                if threadNumber not in threadList:
                    print("Message cannot be deleted")
                else:
                    edit_task_number(
                        clientSocket,
                        threadNumber,
                        taskNumber,
                        taskContent,
                        username,
                        msgList,
                    )

            elif taskCommand == "UPD":
                print(f"{username} issued {taskCommand} command")
                threadNumber = task.split(" ")[1]
                taskContent = task.split(" ")[2]
                if threadNumber in threadList:
                    print(
                        f"{username} upload file {taskContent} to {threadNumber} thread"
                    )
                    clientSocket.send(
                        f"{taskContent} uploaded to {threadNumber} thread".encode()
                    )
                    fileName = threadNumber + "-" + taskContent
                    writeFile = open(fileName, mode="a+")
                    writeFile.close()
                    with open(threadNumber, mode="a+") as wf:
                        wf.write(username + " uploaded " + taskContent + "\n")
                    fileList.append(fileName)
                else:
                    clientSocket.send(
                        "Thread number is not existed and the file cannot be uploaded".encode()
                    )

            elif taskCommand == "DWN":
                print(f"{username} issued {taskCommand} command")
                threadNumber = task.split(" ")[1]
                taskContent = task.split(" ")[2]
                fileName = threadNumber + "-" + taskContent
                if threadNumber in threadList:
                    if fileName in fileList:
                        clientSocket.send(f"all ready".encode())
                        print(f"{taskContent} downloaded from Thread {threadNumber}")
                    else:
                        clientSocket.send(
                            f"{taskContent} does not exist in Thread {threadNumber}".encode()
                        )
                        print(f"{taskContent} does not exist in Thread {threadNumber}")
                else:
                    clientSocket.send(
                        "Thread number is not existed and the file cannot be download".encode()
                    )
                    print(
                        "Thread number is not existed and the file cannot be download"
                    )

        except:
            clientSocket.send("Incorrect input".encode())


def get_msg_number(taskNumber):
    wf = open(taskNumber, mode="r")
    line = wf.readline()
    messageNumber = 1
    while line:
        if line.split(" ")[0].isdigit() == True:
            messageNumber += 1
        line = wf.readline()
    wf.close()
    return messageNumber


def match_task_number(clientSocket, threadNumber, taskNumber, username, msgList):
    # print(msgList)
    if 1 <= int(taskNumber) <= len(msgList):
        if msgList[int(taskNumber) - 1].strip().split(" ")[1] == username + ":":
            # 可以读到这里
            msgList.remove(msgList[int(taskNumber) - 1])
            clientSocket.send("The message has been deleted".encode())

        else:
            clientSocket.send(
                "The message belongs to another user and cannot be deleted".encode()
            )
    else:
        clientSocket.send(
            "Message number is not existed and the message cannot be deleted".encode()
        )

    with open(threadNumber, mode="w") as writeFile:
        for i in msgList:
            writeFile.write(i + "\n")


def edit_task_number(
    clientSocket, threadNumber, taskNumber, taskContent, username, msgList
):
    if 1 <= int(taskNumber) <= len(msgList):
        if msgList[int(taskNumber) - 1].strip().split(" ")[1] == username + ":":
            msgList[int(taskNumber) - 1] = (
                taskNumber + " " + username + ": " + taskContent
            )
            clientSocket.send("The message has been edited".encode())
        else:
            clientSocket.send(
                "The message belongs to another user and cannot be deleted".encode()
            )
    else:
        clientSocket.send(
            "Message number is not existed and the message cannot be deleted".encode()
        )

    with open(threadNumber, mode="w") as writeFile:
        for i in msgList:
            writeFile.write(i + "\n")
