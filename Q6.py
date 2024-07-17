#랜덤으로 주어지는 리스트의 요소 값의 평균을 구하는 함수
def my_sum(list):
    y = 0
    for x in list:
        y = y+x
    l = len(list)
    z = y/l
    return z


list = [6, 7, 8, 9, 10, 10, 100, 40000]

print(my_sum(list2))