import random

result = []
number = 0

while number < 6 :
    number = number+1
    new_number = random.randint(1, 45)
    if new_number in result :
        print("값이 기존에 있습니다. 추가하지 않습니다.")
    else:
        result.append(new_number)

print(result)