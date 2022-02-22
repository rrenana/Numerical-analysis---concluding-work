from datetime import datetime
def lottery(id1, id2, id3):
    amount_of_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i, j, c in zip(id1, id2, id3):
        amount_of_number[int(i)] = amount_of_number[int(i)] + int(1)
        amount_of_number[int(j)] = amount_of_number[int(j)] + int(1)
        amount_of_number[int(c)] = amount_of_number[int(c)] + int(1)
    a=(amount_of_number[1])%9
    print("1.",a)
    b = (amount_of_number[2])%9+10
    print("2.",b)
    c = (amount_of_number[3])%12+19
    print("3.",c)
    d = (amount_of_number[4])%6+31
    print("4.",d)
    return amount_of_number

array = lottery([2, 1, 3, 2, 5, 0, 7, 4, 9], [3, 1, 9, 0, 3, 4, 7, 5, 7], [3, 2, 6, 9, 4, 5, 7, 6, 3])

approx = lottery([2, 1, 3, 2, 5, 0, 7, 4, 9], [3, 1, 9, 0, 3, 4, 7, 5, 7], [3, 2, 6, 9, 4, 5, 7, 6, 3])
date = datetime.now()
d = date.day
hour = date.hour
minute = date.minute
print('the answer is:', format(approx)+"00000"+format(d)+format(hour)+format(minute))




