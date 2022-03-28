# Строка №1
string1 = '''Google создаст специальную команду для поиска багов в особо 
важных приложениях'''

string1 = string1.split()
print(len(string1))


# Строка №2
string2 = "У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. Надепозитный контракт внесено более 525 288 ETH"

for i in string2.split():
   print(type(i))


# Строка №3
string3 = 'хакеры слили в сеть данные пакистанской энергетической компании k - Electric'
print(string3.upper())


# Строка №5
string5 = 'Ботнет IPStorm, в которой ранее входили лишь Windows -машины, увеличился до 13500 зараженных систем'
print(string5.replace("E", "3"))


string1 = "ArGeN"
print(string1.upper())
print(string1.lower())

bool = True
print(str(bool))


