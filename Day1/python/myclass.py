class MyClass:
    # construtor
    def __init__(self):
        print("Myclass constructor")

    # If the function starts with no _ or __ then it is treated as public
    # Same applies for variables
    # These functions are also called as member functions or methods
    def publicMethod(self):
        print("MyClass public method")

    # This is just a convention or a best practice to indicate this protected 
    # but python does enforce this a protected as python really doesn't supported protected 
    # access modifier
    def _protectedMethod(self):
        print("MyClass protected method")

    # Python considers any variable or method that has __ is treated as private
    def __privateMethod(self):
        print("MyClass private method")

# This is the entry point of python - equivalent to main functions in other programming languages
if __name__ == "__main__":
    #Create an object of MyClass - instantiate
    myClassObject = MyClass()
    myClassObject.publicMethod()
    myClassObject._protectedMethod()
    myClassObject.__privateMethod()
