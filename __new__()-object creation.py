class Positivenumber(int):
    def __new__(cls, value):
        if value < 0:
            value = 0

        return super().__new__(cls, value)


n1 = Positivenumber(10)
n2 = Positivenumber(-5)  


print(n1)  # Output: 10
print(n2)  # Output: 0