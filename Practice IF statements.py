mylist = [1,2,3,4,5,6,7,8,9,10]
for jelly in mylist:
    print('hello')
    for num in mylist:
        if num % 2 == 0:
            print(num)
        else:
            print(f'Odd Number {num}')
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)