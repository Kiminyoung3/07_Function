def score(x):
    y = ""
    if 81 <= x <= 100:
        y = "A"
    elif 61 <= x <= 80:
        y = "B"
    elif 41 <= x <= 60:
        y = "C"
    elif 21 <= x <= 40:
        y = "D"
    elif 0 <= x <= 20:
        y = "E"
    else:
        y = "올바른 학점을 입력하세요."
    return y

k = int(input("점수를 입력하세요.: "))
print(score(k))