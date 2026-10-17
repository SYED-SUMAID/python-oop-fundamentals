class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"name: {self.name}")
        print(f"age : {self.age}")

s1 = student("Sumaid",21)

s1.show()

