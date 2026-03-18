# pro-3....generate arithmetic exception and log the exception

import logging
logging.basicConfig(filename= "error.txt",level=logging.ERROR)


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b  
    print("Result:", result)

except ZeroDivisionError as e:
    print("Arithmetic Exception occurred!")
    logging.error("Exception occurred: %s", e)

    print("program ended")
