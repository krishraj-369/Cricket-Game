import random
l = [1, 2, 3, 4, 5, 6]
toss = ["Head", "Tail"]
bat_ball = ["Bating", "Balling"]
t_runs = []
user = input("Enter your choice (Tail or Head) : ")
toss_result = random.choice(toss)
print(toss_result)
if toss_result == user:
    print("Congruutulation! You won the toss. Choice (Bating or Balling)")
    b_b = input("Enter your choice (Bating or Balling : )")
    if b_b == "Bating":
        print("Let's do Batting and robot do balling.")
        while True:
            f_ball = random.choice(l)
            f_bat = int(input("Enter your run : "))
            print(f"Your runs {f_bat}")
            print(f"Robots run {f_ball}")
            if f_ball == f_bat:
                print("You Out!")
                break
            else:
                print(f"You got {f_bat} runs.\n PLEASE NOTE DOWN THE RUN AND ADD THEM.")
    elif b_b == "Balling":
        print("Let's do balling and robot do bating.")
        while True:
            f_bat = random.choice(l)
            f_ball = int(input("Enter your run : "))
            print(f"Your runs {f_ball}")
            print(f"Robots run {f_bat}")
            if f_ball == f_bat:
                print("Robot Out!")
                break
            else:
                print(f"Robot got {f_bat} runs.\n PLEASE NOTE or WRITE DOWN THE RUN AND ADD THEM.")
    else:
        print("Error occurs try to run the program againg.")
        while True:
            break
else:
    print("You loss the toss.")
    r_b_b = random.choice(bat_ball)
    if r_b_b == "Bating":
        print("Let's do balling and robot do batting.")
        while True:
            f_bat = random.choice(l)
            f_ball = int(input("Enter your run : "))
            print(f"Your runs {f_ball}")
            print(f"Robots run {f_bat}")
            if f_ball == f_bat:
                print("Robot Out!")
                break
            else:
                print(f"Robot got {f_bat} runs.\n PLEASE NOTE or WRITE DOWN THE RUN AND ADD THEM.")

    else:
        print("Let's do bating and robot do balling.")
        while True:
            f_ball = random.choice(l)
            f_bat = int(input("Enter your run : "))
            print(f"Your runs {f_bat}")
            print(f"Robots run {f_ball}")
            if f_ball == f_bat:
                print("You Out!")
                break
            else:
                print(f"You got {f_bat} runs.\n PLEASE NOTE DOWN THE RUN AND ADD THEM.")