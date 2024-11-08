# data = input()
# name, age = data.split()
#
# print("Name: " + name +", Age:" + age)


numbers = input()
n1, n2, n3 = numbers.split()

average = (int(n1) + int(n2) + int(n3)) / 3
print("%.2f" % average)