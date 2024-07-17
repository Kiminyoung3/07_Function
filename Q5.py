

def my_num(a):
    b = ""
    if a%2 == 0:
        b = "짝수"
    elif a%2 == 1:
        b = "홀수"
    return b


x = int(input("숫자를 입력하세요.: "))
print(my_num(x))