import sym_sys as s

#Initialise symbols like below

x = s.Symbol('x')

#Use functions like 'derivate' as below

e = s.derivative(s.Number(2)**x, x)

print(e)

print(s.simplify(e))