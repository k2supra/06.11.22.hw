try:
    print("Enter  problem")
    problem = input("->")

    t1 = "+"
    t2 = "-"
    t3 = "*"
    t4 = "/"


    def gq(gggq):
        prob1 = problem.split(t1)
        if prob1 == problem.split(t1):
            prob1[0]
            prob1[1]
            res = float(prob1[0]) + float(prob1[1])
            print(f"Result is {res}")


    def ggw(ghjkl):
        prob2 = problem.split(t2)
        if prob2 == problem.split(t2):
            prob2[0]
            prob2[1]
            res = float(prob2[0]) - float(prob2[1])
            print(f"Result is {res}")


    def ghv(gho):
        prob3 = problem.split(t3)
        if prob3 == problem.split(t3):
            prob3[0]
            prob3[1]
            res = float(prob3[0]) * float(prob3[1])
            print(f"Result is {res}")


    def dxc(hjn):
        prob4 = problem.split(t4)
        if prob4 == problem.split(t4):
            prob4[0]
            prob4[1]
            res = float(prob4[0]) / float(prob4[1])
            print(f"Result is {res}")


    def main():  # 1
        gq(problem)


    main()


    def main():  # 2
        ggw(problem)


    main()


    def main():  # 3
        ghv(problem)


    main()


    def main():  # 4
        dxc(problem)


    main()
except Exception as ex:
    print(f"Error : {ex}")
