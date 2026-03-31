#Dictionary example
d = {'k1':1, 'k2':2, 'k3':3}
for value in d.values ():
    print(value)

#"Pass" example-means do nothing at all, it helps to use this if your writing code & dont want to (print)
x = [1,2,3]
for item in x:
    pass
print('end of script')

#Continue example-goes to the top of closest enclosing loop
mystring = "Sammy"
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

mystring = "Sammy"
for letter in mystring:
    if letter == 'a':
        break
    print(letter)