# Let's minimize the surface z = x^2 + y^2

# We need to make a problem
import optim.Problem as Problem

# And we also want to solve said problem with an algorithm
import optim.algorithms as algorithms


# So let's start with the math problem we want to solve (minimize)
def J(x,y):
    return x**2 + y**2

# Cool. That looks like it's our original equation alright. Now lets define a problem in the programmatic sense
prob = Problem('my_problem')

# Alright. Let's bind our equation to the problem we just made.
prob.Cost(J)

# We have 2 "states".
prob.State('x', lower_bound=-2, upper_bound=2, bits=4)
prob.State('y', lower_bound=-2, upper_bound=2, bits=4)

xopt = algorithms.dga(prob)
print(xopt)