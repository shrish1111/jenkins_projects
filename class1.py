class square:
    # class parameters
    length = 1
    breadth = 1

    # class methods
    def __init__(self):
        print("First class")
    def area(self,length,breadth):
        return length*breadth
a = square()
print(a.area(2,2))
