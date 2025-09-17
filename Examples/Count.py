while True:
    number = input("Enter a number: ")
    if number.isdigit() == True:
        for i in range(0, int(number)):
            print(i+1)
        break
    else:
        print("Enter a valid digit!")
