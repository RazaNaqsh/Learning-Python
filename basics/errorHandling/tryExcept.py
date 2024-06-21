while True:
    try:
        age = int(input("What is your age?"))
        10 / age
        print(f"So Your age is {age} ssouuukaa")
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
    else:
        print("thankYou")
        break
