import numpy
import sys

# Get inputted arguments
Operation = sys.argv[1].lower()
Coefficients = sys.argv[2].strip('[]').split(',')

# Convert each element in the list from string to float
for i in range(0,len(Coefficients)):
    Coefficients[i] = float(Coefficients[i])

# Create a polynomial from the list of coefficients
polynomial = numpy.poly1d(Coefficients)

# Perform the derivative or differentiation on the polynomial
if Operation=="true":
    calculus = numpy.polyint(polynomial)
else:
    calculus = numpy.polyder(polynomial)

# Return the new set of coefficients
print calculus.coeffs.tolist(),
