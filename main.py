
try:
    print("Enter  problem")
    problem = input("->")

    t1 = "+"
    t2 = "-"
    t3 = "*"
    t4 = "/"



    prob1 = problem.split(t1)

    prob2 = problem.split(t2)

    prob3 = problem.split(t3)

    prob4 = problem.split(t4)

    if prob1 == problem.split(t1):
        prob1[0]
        prob1[1]
        res = float(prob1[0]) + float(prob1[1])
        print(f"Result is {res}")


    if prob2 == problem.split(t2):
        prob2[0]
        prob2[1]
        res = float(prob2[0]) - float(prob2[1])
        print(f"Result is {res}")


    if prob3 == problem.split(t3):
        prob3[0]
        prob3[1]
        res = float(prob3[0]) * float(prob3[1])
        print(f"Result is {res}")


    if prob4 == problem.split(t4):
        prob4[0]
        prob4[1]
        res = float(prob4[0]) / float(prob4[1])
        print(f"Result is {res}")

except Exception as ex:
    print(f"Error : {ex}")