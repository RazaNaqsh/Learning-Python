import utility  # imports the module

# import shopping.shopping_cart  # importing package
from shopping import shopping_cart


# shopping is the package , the folder
# the file inside is the module


# Main file is the file that is run, regardless of the name,
# each file has its own __name__, when ur using the modules

print(__name__)

# Thus for main files we use syntax like

# if we are running the main file then only the imported modules
# shud be used
if __name__ == "__main__":
    print("this is the main file")
    utility.test()

    print(utility.multiply(2, 3))

    # print(shopping.shopping_cart.buy("apple")) #when ur using full import
    print(shopping_cart.buy("apple"))  # when using from shopping import
