import re
b=input()
a=re.match('[1-9]\d{3}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])',b)
if a!=None:
    print("right")
else:
    print('wrong')