### @export "imports"
import numpy
import matplotlib

### @export "setup-pyplot"
matplotlib.use("Agg")
import matplotlib.pyplot as pyplot
pyplot.figure(figsize=(6,3))

### @export "calcs"
sum_fractions = 0.0
values = []
for i in range(1,20):
    sum_fractions += 1.0/(i**2)
    value = numpy.sqrt((6.0 * sum_fractions))
    values.append(value)
    print "After adding 1/%s^2 value is %0.10f" % (i, value)

### @export "graph"
pyplot.axhline(numpy.pi, linewidth=2, color='r')
pyplot.plot(range(1,20), values, color='b')

### @export "save-graph"
filename = "dexy--pi.png"
with open(filename, "wb") as f:
    pyplot.savefig(f)

### @export "calcs-2"
def sqrt_six_times_sum_inv_squares(n):
    return numpy.sqrt(6.0*sum(1.0/k**2 for k in range(1,n)))

def four_times_sum_inv_odds(n):
    return 4.0*sum(((-1.0)**(k+1))/(2*k-1) for k in range(1,n))

for i in range(1, 10):
    value = sqrt_six_times_sum_inv_squares(i)
    print "At step %s value is %0.10f" % (i, value)

for i in range(1, 10):
    value = four_times_sum_inv_odds(i)
    print "At step %s value is %0.10f" % (i, value)

### @export "graph-2"
pyplot.clf()
N = 30
xs = range(1,N)
pyplot.axhline(numpy.pi, linewidth=2, color='r')
pyplot.plot(xs, [sqrt_six_times_sum_inv_squares(i) for i in xs], color='b')
pyplot.plot(xs, [four_times_sum_inv_odds(i) for i in xs], color='g')
pyplot.axis([0, N, 2, 4])

### @export "save-graph-2"
filename = "dexy--pi2.png"
with open(filename, "wb") as f:
    pyplot.savefig(f)
