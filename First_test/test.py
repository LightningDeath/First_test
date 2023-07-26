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

dict_my = {1: 2}
dict_my.update({2: 1})
print(dict_my)
dict_my.update({3: [{1: 2}]})
print(dict_my)
a = list(dict_my)[-1]
print(a)
