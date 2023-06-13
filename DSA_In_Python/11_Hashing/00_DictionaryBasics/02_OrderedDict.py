from collections import OrderedDict

dic = {3:"Abdul", 45:"Afraz", 1: "Aysha"}

res = sorted(dic)
print(type(res))

res = OrderedDict(sorted(dic.items()))
print(type(res))

for key in res:
    print(res[key])