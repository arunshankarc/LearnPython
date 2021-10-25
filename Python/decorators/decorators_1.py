def be_polite(func):
    def wrapper():
        print("What a pleasure to meet you !!")
        func()
        print("Have a great day !!")
    return wrapper


@be_polite
def greet():
    print("My name is Arun")


greet()
