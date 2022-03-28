# Упражнение 1
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for language in languages:
   if lang1 == language:
        print("This language is in list")
   else:
        print("This language is not in list")

# Упражнение 2
for language in languages:
    if language == "php":
        break


# Упражнение 3
for i in range(1,6):
   print(7 ** i)

# Можно обойтись так:
print([7**i for i in range(1,6)][-1])


# Упражнение 4
for i in range(len(languages)):
   print(i, languages[i])

# Упражнение 5
i = 2
for a in range(1,20):
    if a> 10:
        print(a - i)
        i += 2
        continue
    print(a)

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# Тоже самое
# a = 0
# i = 2
# while a < 20:
#     a += 1
#     if a > 10:
#         print(a-i, end=", ")
#         i += 2
#         continue
#     print(a, end=", ")



