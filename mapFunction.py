# How map() Works
def double(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
double_numbers = map(double, numbers)

print(list(double_numbers))

# Using map() with Built-in Functions
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)

words = ["apple", "banana", "blueberry"]
word_lengths = list(map(len, words))
print(word_lengths)

# Using map() with Lambda Functions
numbers = [1, 2, 3, 4, 5] 
doubled = list(map(lambda x: x * 2, numbers)) 
print(doubled)

# Multiple Iterables with map()
list1 = [1, 2, 3, 4] 
list2 = [10, 20, 30] 
lists = list(map(lambda x, y: x + y, list1, list2)) 
print(lists)
