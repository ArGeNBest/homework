# Problem 0
dates_of_birth =  {3, 10, 11, 13, 31, 21, 1, 10, 3, 5, 6, 6}
dates_of_birth.remove(6)
print(dates_of_birth)


# Problem 1
# Приходилось сделать заморожения множество, чтобы обойти ошибку Unhashable set, это возникает из-за того что изменяемые типы данных не имеет хеш.
group_1 = frozenset({'ss'})
group_2 = {'s'}
group_2.add(group_1)
group_2 = frozenset(group_2)

group = {'sss', group_2}
print(group)


# Problem 2
farm_1 = {'dog', 'cat', 'mouse', 'sheep'}
farm_2 = {'cow', 'horse', 'donkey', 'cat', 'dog'}

# Разность farm_1\farm_2
farm_3 = farm_2.difference(farm_1)
print(farm_3)


# Problem 3
five = {1, 2, 3, 4, 5}
five.pop()
print(five)


# problem 4
numbers = set()

for i in range(10):
    number = int(input("Enter the number: "))
    numbers.add(number)

numbers = frozenset(numbers)
print(numbers)


# Problem 5
# Объединение двух множеств
farm_1 = {'dog', 'cat', 'mouse', 'sheep'}
farm_2 = {'cow', 'horse', 'donkey', 'cat', 'dog'}

general = farm_1.union(farm_2)
print(general)

print(farm_1.difference(farm_2))



