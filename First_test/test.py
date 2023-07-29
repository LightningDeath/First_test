# import datefinder
#
# a = datefinder.find_dates('"Дата начисления 21.04.2022". Отсюда мне надо вытащить только "21/04/2022". 22.12.11')
# b = list(a)
# print(b)
#
# # OUT
# # [datetime.datetime(2022, 4, 21, 0, 0), datetime.datetime(2022, 4, 21, 0, 0)]
#
# print(b[0].date().isoformat())
#
# # OUT
# # '2022-04-21'
from collections import OrderedDict
from datetime import datetime

dict_my = {1: [{"2": "va"}]}

dict_my.update({2: [{"2": "vas"}]})
dict_my.update({3: [{"2": "vasia1", "age": 3}]})
dict_my.update({4: [{"2": "v"}]})
dict_my.update({5: [{"2": "vasia1", "age": 2}]})
print(dict_my)
a = list(dict_my)
n_dict_my = {}
n = 1
for i in dict_my:
    if n == 1:
        if dict_my[i][0]["2"] != "vasia1":
            n_dict_my.update({i: [dict_my[i][0]]})
        n += 1
    else:
        if dict_my[i][0]["2"] != "vasia1":
            n_dict_my.update({n: [dict_my[i][0]]})
            n += 1

# try:
#     f = dict_my.pop(3)
# except KeyError:
#     print("Нет")
# if len(n_dict_my) == 0:
#     print("Не найдено")
# else:
for i in n_dict_my:
    print(i)
    print(n_dict_my[i][0]["2"])
