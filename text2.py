# Дан список, нужно выводить первый, средний, последний элемент списка.
# def get_first_mid_last_list_elements(numbers: list):
#     if len(numbers) % 2 != 0:
#         return numbers[::int(len(numbers) / 2)]
#     else:
#         return [numbers[0], int((len(numbers) / 2)), numbers[-1]]
    

# b = list(range(1,10))
#print(b)
#get_first_mid_last_list_elements(b)
# a = list(range(1,9))
# print(a)
# get_first_mid_last_list_elements(a)
# get_first_mid_last_list_elements(b)


# Дано две точки, определить какой четверти лежат.
# def choose_pc(ram, hdd, hdd_type, price, condition):
#     if (ram>= 4 and ram <=8) and (hdd_type =='ssd' and hdd >=256 or hdd_type=='hdd' and hdd>=1024) and condition and price <= 1000:
#         return True
#     else:
#         return False

# print(choose_pc(8,1024,'ssd',1000,0))


#  Дом нужен в районе чон-арык, байтик или ортосай Если дом из кирпича и участок до 4 соток, то стоимость должна быть не более 50000. Если дом из пескоблока и участок до 5 соток, то стоимость должна быть не более 45000. Входные параметры: ["чон-арык", "байтик ", "ортосай", "кирпич", "пескоблок"]

def choose_house(district, material, area, price):
    if district in  ["чон-арык", "байтик", "ортосай"]:
        if area <= 4 and material == "кирпич":
            return price <= 50000
        if area <= 5 and material =="пескоблок":
            return price <= 45000
            
    return False

# Хочу лексус или тойоту от 2004 года с пробегом не более 150000, белую или серую, с левым рулем и максимум 2 хозяина. Со стоимостью не больше 10000, или такую же , но с пробегом 200000 и более, но с ценой меньше 8000
#  left_wheel будет типа bool Марки машины пишите на англ: LEXUS, TOYOTA Цвет машины: white, grey
def func(model, year, usage, color, owner, price, left_wheel):
    if model.upper() in ['LEXUS', 'TOYOTA'] and year >= 2004 and \
    left_wheel and color in ['grey', 'white'] and owner <= 2:
        if usage <= 150000:
            return price <= 10000
        else:
            return price <= 8000
        
    return False