my_list = [10, 20, 30, 40]
my_list.insert(1, 15)
new_list = [50, 60, 70]
my_list.extend(new_list)
print(my_list)

my_list.pop()
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

# Had to reverse to ensure the sorting actually since the data was already in ascending order
my_list.sort()
print(my_list)

# The following line is incorrect, should use indexing instead of calling
# my_list(3)
print(my_list[3])

print(my_list)

print(my_list.index(30))

position = my_list.index(30)
print(position)