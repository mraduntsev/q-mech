# 2. Пространственные балки (Beam3D)

> Источник: [`docs.sympy.org/latest/modules/physics/continuum_mechanics/beam.html`](https://docs.sympy.org/latest/modules/physics/continuum_mechanics/beam.html)

```python
class sympy.physics.continuum_mechanics.beam.Beam3D(
    length,
    elastic_modulus,
    shear_modulus,
    second_moment,
    area,
    variable=x,
)
```

Данный класс обрабатывает нагрузки, приложенные в любом направлении в трехмерном пространстве, а также учитывает неодинаковые значения момента инерции сечения (второго момента) относительно разных осей.

> [!note] Примечание
> При решении задачи изгиба балки необходимо использовать согласованное правило знаков; результаты будут автоматически следовать выбранному правилу знаков. Данный класс предполагает, что любой вид распределенной нагрузки/момента прикладывается по всей длине пролета балки.

## Пример

Имеется балка длиной l метров. Постоянная распределенная нагрузка величиной q приложена вдоль оси y от начала до конца балки. Постоянный распределенный момент величиной m также приложен вдоль оси z от начала до конца балки. Балка жестко защемлена с обоих концов. Таким образом, прогиб балки на обоих концах ограничен.

```python
from sympy.physics.continuum_mechanics.beam import Beam3D
from sympy import symbols, simplify, collect, factor
l, E, G, I, A = symbols('l, E, G, I, A')
b = Beam3D(l, E, G, I, A)
x, q, m = symbols('x, q, m')
b.apply_load(q, 0, 0, dir="y")
b.apply_moment_load(m, 0, -1, dir="z")
b.shear_force()
b.bending_moment()
b.bc_slope = [(0, [0, 0, 0]), (l, [0, 0, 0])]
b.bc_deflection = [(0, [0, 0, 0]), (l, [0, 0, 0])]
b.solve_slope_deflection()
factor(b.slope())
dx, dy, dz = b.deflection()
dy = collect(simplify(dy), x)
dx == dz == 0
dy == (x*(12*E*I*l*(A*G*l**2*q - 2*A*G*l*m + 12*E*I*q)
+ x*(A*G*l*(3*l*(A*G*l**2*q - 2*A*G*l*m + 12*E*I*q) + x*(-2*A*G*l**2*q + 4*A*G*l*m - 24*E*I*q))
+ A*G*(A*G*l**2 + 12*E*I)*(-2*l**2*q + 6*l*m - 4*m*x + q*x**2)
- 12*E*I*q*(A*G*l**2 + 12*E*I)))/(24*A*E*G*I*(A*G*l**2 + 12*E*I)))
```

### Ссылки

[R729] https://homes.civil.aau.dk/jc/FemteSemester/Beams3D.pdf
