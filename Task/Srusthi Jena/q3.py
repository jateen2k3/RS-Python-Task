
digits = []
length =input('the number of digits u wanna enter')
length = int(length)
digit_int =''
digit_int =str(digit_int)
while length>0:
    digit =input('enetr the digit')
    digits.append(digit)
    digit_int = digit_int + digit
    length = length-1
print(digits)
print(digit_int)
digit_int=int(digit_int)
digit_int=digit_int+1
var = digit_int
digit_int =str(digit_int)
l =len(digit_int)
digits2 = []
m=''
while l>0:
    m=var%10
    digits2.append(m)
    var=var//10
    l=l-1
digits2.reverse()
print(digits2)

