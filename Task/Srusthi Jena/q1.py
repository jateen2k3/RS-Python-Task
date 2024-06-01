
s = input('enter your string')
t = input('enetr another string')
s= s.lower()
t= t.lower()
sorted_s =sorted(s)
sorted_t =sorted(t)
if sorted_s == sorted_t:
      print('true')
else:
   print('false')
