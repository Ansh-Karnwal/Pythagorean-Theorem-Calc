import math

def side_calculator(side, hyp):
    return round(math.sqrt(hyp**2 - side**2), 2)
def hyp_calculator(side1, side2):
    return round(math.sqrt(side1**2 + side2**2), 2)
def getInput(left, right):
    return float(input("what is " + left)), float(input("what is " + right))
def prettyPrint(sideA, sideB, hyp):
    print(f"Side A is {sideA} when Side B is {sideB} and when Hypotenuse C is {hyp}")
    
print("Welcome! Please start by choosing which side of the right triangle you want to calculate")
options = int(input("Which side of the right triangle do you want to solve? \nType 1 for Side A, Type 2 for Side B, Type 3 for Hypotenuse C: "))
    
if options == 1:
    print("Side A Selected!")
    sideB, hyp = getInput("side B", "hyp")
    sideA = side_calculator(sideB, hyp)
    prettyPrint(sideA, sideB, hyp)
    
elif options == 2:
    print("Side B Selected!")
    sideA, hyp = getInput("side A", "hyp")
    sideB = side_calculator(sideA, hyp)
    prettyPrint(sideA, sideB, hyp)
    
elif options == 3:
    print("Hypotenuse C Selected!")
    sideA, sideB = getInput("side A", "side B")
    hyp= hyp_calculator(sideA, sideB)
    prettyPrint(sideA, sideB, hyp)
    
else:
    print("Choose a valid option please!")