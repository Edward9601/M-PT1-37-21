s =  ""
a=float(input('Введите коэффициент a: '))
if a>0:
    s="ax*x"
else:
    s="-ax*x"
b=float(input('Введите коэффициент b: '))
if b>0:
    s=s + "-bx"
else:
    s=s + "+bx"
c=float(input('Введите коэффициент с: '))
if c>0:
    s=s + "-c=0"
else:
    s=s + "+c=0"

print("Уравнение: \n" )
print(s)

D = b**2-4*a*c

if D>0:
    x1=(-b+D**(1/2))/(2*a)
    x2=(-b-D**(1/2))/(2*a)
    print('Решение: \n')    
    print('x1 = ' + str(x1) + '; x2 = ' + str(x2))
elif D==0:
    x1=-b/(2*a)
    print('Уравнение: ' + str(str(a)+'x*x-'+str(b)+'x-'+str(-c)+'=0'))
    print('Решение: \n')
    print('x1 = ' + str(x1))
else:
    print('Нет корней')