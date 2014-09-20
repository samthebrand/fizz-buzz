number = 100

print 'Fizz buzz counting up to ' + str(number)

for num in range(1,number):
  if num % 3 == 0 and num % 5 == 0:
    print ', fizz buzz',
  elif num % 3 == 0 and num % 5 != 0:
    print ', fizz',
  elif num % 3 !=0 and num % 5 == 0:
    print ', buzz',
  else:
    print num,