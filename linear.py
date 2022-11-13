from sympy import Derivative, symbols, solve, plot

x = symbols('x')  # x를 기호 변수화
fx = x**2 - 4

fprime = Derivative(fx, x).doit()  # x에 대해서 미분
print("fx 의 도함수는 : ", fprime, "입니다")

q = solve(fx)
print(q)

p = 10
p1 = plot(fx, show=False)

for i in range(10): # 수치해석 반복

    n = fprime.subs({x: p})

    b = fx.subs(x, p)

    f = n * (x - p) + b
    p = solve(f)
    p = float(p[0])
    print(p)

    p2 = plot(f, show=False)
    p1.append(p2[0])

print(p1)