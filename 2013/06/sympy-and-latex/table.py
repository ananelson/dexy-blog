# based on https://github.com/sympy/sympy/wiki/Generating-tables-of-derivatives-and-integrals

### @export "imports"
from sympy import Eq, Derivative, Integral
from sympy import diff, integrate
from sympy import cos, sin, exp
from sympy import latex
from sympy.abc import x
import json

### @export "define-functions"
def derivative_eqn(f, x):
    return Eq(Derivative(f, x), diff(f, x))

def integral_eqn(f, x):
    return Eq(Integral(f, x), integrate(f, x))

### @export "example-deriv"
derivative_eqn(x**2, x)

### @export "example-integral"
integral_eqn(x**2, x)

### @export "define-latex-functions"
def derivative_eqn_latex(f, x):
    return latex(derivative_eqn(f, x))

def integral_eqn_latex(f, x):
    return latex(integral_eqn(f, x))

### @export "example-deriv-latex"
derivative_eqn_latex(x**2, x)

### @export "example-integral-latex"
integral_eqn_latex(x**2, x)

### @export "save-examples-latex"
example_dict = {
    'derivative' : derivative_eqn_latex(x**2, x),
    'integral' : integral_eqn_latex(x**2, x)
}

with open("example-latex.json", "w") as f:
    json.dump(example_dict, f)

### @export "derivatives"
functions = [cos(x)/(1 + sin(x)**i) for i in range(1, 5)]
derivatives_latex = [derivative_eqn_latex(f, x) for f in functions]

with open("derivatives.json", "w") as f:
    json.dump(derivatives_latex, f)

### @export "integrals"
functions = [x**i * exp(i*x) for i in range(1, 5)]
integrals_latex = [integral_eqn_latex(f, x) for f in functions]

with open("integrals.json", "w") as f:
    json.dump(integrals_latex, f)
