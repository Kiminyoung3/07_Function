#문자메세지를 입력받아 요금을 반환하는 함수 생성.
def m_funtion (m):
    l = 0
    if len(m) <= 20:
        l = 50
        print("문자 요금은:", l)
    else:       #elif len(m) >20:
        l = 100
        print("문자 요금은:", l)

    return l

k = input("문자메세지를 입력하세요: ")
m_funtion(k)
