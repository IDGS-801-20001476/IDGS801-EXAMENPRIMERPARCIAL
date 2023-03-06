from pytest import main

from TuclaseExamen import TuclaseExamen

 
#create the class instance

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(TuclaseExamen.arithmetic_arranger(problems, True))

# Run unit tests automatically
main(['-vv'])
