# First thing would be to learn how to take the derivative of a function in code, but first we need learn how to express any kind of function in code. This way when I write my functions for calculating the derivative, I can use them with both linear and nonlinear functions. 

def f(x):
    new_value = 2*x**2 + 4*x - 10
    print(new_value)
f(7)

# The function that we want to write is f(x) = 2X**2 + 4X - 10. For this we will use a tuple (a list whose elements cannot be reassigned

tuple = (7, 3)
tuple[0] # 7
tuple[1] # 3

# Below is a list of tuples:

four_x_squared_plus_four_x_minus_ten = [(4, 2), (4, 1), (-10, 0)]

# Each tuple on that list represents a different term in the function. Always the first element is the "n" value multiplying the X, and the second value is the exponent of the X. Therefore, 4X**2 translates as (4, 2) and -10 translates as (-10, 0) which results as -10*X**0.

# Try now to express: f(x) = 4*x**3 + 11*X**2

four_x_cubic_plus_eleven_x_square = [(4, 3), (11, 2)]


# Now that we can represent a function in code, let's write a Python function called term_output that can evaluate what a single term equals at a value of x.
# For example x = 2, the term 3*X**2 = 12
# So we represent 3*x**2 in code as (3, 2), and:
# term_output((3, 2), 2) should return 12

def term_output(term, input_value):
    pass
term_output((3, 2), 2)

def output_at(list_of_terms, x_value):
    pass

three_x_squared_minus_eleven = [(3, 2), (-11, 0)]
output_at(three_x_squared_minus_eleven, 2)
output_at(three_x_squared_minus_eleven, 3)

# Now we can use the output_at function to display our function graphically. We have to declare x_values and calculate output_at for each of the x_values
# First I had to installed plotly.py by using the "pip install plotly" command line

import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

from graph import plot, trace_values
x_values = list(range(-30, 30, 1))
y_values = list(map(lambda x: output_at(three_x_squared_minus_eleven, x), x_values))

three_x_squared_minus_eleven_trace = trace_values(x_values, y_values, mode = 'lines')
plot([three_x_squared_minus_eleven_trace], {'title': '3x^2 - 11'})

# Let's start with a function f(x) = 4X +15

four_x_plus_fifteen = [(4, 1), (15, 0)]


