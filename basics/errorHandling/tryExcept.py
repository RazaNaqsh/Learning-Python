while True:
    try:
        age = int(input("What is your age?"))
        10 / age
        print(f"So Your age is {age} ssouuukaa")
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
    else:  # if there are no exceptions , after try it goes here
        print("thankYou")
        break
    finally:  # runs regardless at the end
        print("Everythings over")
