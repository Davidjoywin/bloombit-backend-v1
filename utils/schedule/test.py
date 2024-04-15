from base import Base

b = Base()
l = list(range(1, 23, 2))

print(l)
b.getAllData()
b.initiateData(l)
b.getAllData()
print(b.length)