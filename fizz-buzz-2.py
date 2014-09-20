number = int(raw_input('Gimme a number! '))

print 'Fizz buzz counting up to ' + str(number) + ':'

for num in range(1,number + 1):
  if num == 1:
  	print num,
  elif num % 3 == 0 and num % 5 == 0:
    print ', fizz buzz',
  elif num % 3 == 0 and num % 5 != 0:
    print ', fizz',
  elif num % 3 !=0 and num % 5 == 0:
    print ', buzz',
  else:
    print ', ' + str(num),