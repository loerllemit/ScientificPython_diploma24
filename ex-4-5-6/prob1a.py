import sympy as sp
sp.init_printing(order='rev-lex')

def taylor(expr,N):
    h = sp.symbols('h')
    final = 0

    for i in range(N+1): 
        final += sp.diff(expr, x,i).subs(x,h) * (x-h)**i/sp.factorial(i)
    return final

x, h = sp.symbols('x h')
expr = x**2+sp.sin(x)*sp.cos(x)+4*x**3

print(taylor(expr,5))