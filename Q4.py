#부가세 10퍼센트

def funtion_l(a):
    e_list = []
    for x in a:
        b = int(x*1.1)
        e_list.append(b)
    return e_list



list = [5000, 100, 330, 7777000]

print(funtion_l(list))