largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
    	num = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = num
    if smallest is None:
        smallest = num
    if largest < num :
        largest = num
    if smallest > num :
        smallest = num

print("Maximum", largest)
print("Minimum", smallest)
