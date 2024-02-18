count = 0
while True:
    userName = input("Hello! Welcome to FaceSnap! \n\nUsername: ") 
    password = input("Password: ")
    count += 1
    if count == 3:
        #tells user bye
        break #exit
    else:
        if userName == 'elmo' and password == 'blue':
            #let them in
            break #they are in, exit loop
        else:
            #tell them it is wrong and have them retry, stay in loop