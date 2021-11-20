import random

option_lst = ['rock','paper','pencil','scissors']

cpu_pts = 0
player_pts = 0

print("\t\t\t\t\t\t    \tROCK, PAPER, PENCIL, SCISSORS\n")

while player_pts !=10 and cpu_pts !=10:
    print("1-Rock\n2-paper\n3-pencil\n4-scissors\n")
    while True:
        choice = int(input("choice : "))
        if choice <= 4:
            break
        else :
            print("invalid choice !\n")
    user_action = option_lst[choice - 1]
    cpu_action = random.choice(option_lst)
    print("User : {}\nCPU : {}\n".format(user_action,cpu_action))
    if user_action == 'rock':
        if cpu_action == 'rock':
            print("Draw !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'paper':
            cpu_pts+=1
            print("CPU wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'pencil':
            player_pts+=1
            print("Player wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'scissors':
            player_pts+=1
            print("Player wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))

    elif user_action == 'paper':
        if cpu_action == 'paper':
            print("Draw !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'pencil':
            cpu_pts+=1
            print("CPU wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'scissors':
            cpu_pts+=1
            print("CPU wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'rock':
            player_pts+=1
            print("Player wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))

    elif user_action == 'pencil':
        if cpu_action == 'pencil':
            print("Draw !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'rock':
            cpu_pts+=1
            print("CPU wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'scissors':
            cpu_pts+=1
            print("CPU wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'paper':
            player_pts+=1
            print("Player wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))

    elif user_action == 'scissors':
        if cpu_action == 'scissors':
            print("Draw !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'rock':
            cpu_pts+=1
            print("CPU wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'pencil':
            player_pts+=1
            print("Player wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))
        elif cpu_action == 'paper':
            player_pts+=1
            print("Player wins a point !\nPOINTS-\nCPU : {}\nUser : {}\n".format(cpu_pts,player_pts))

if player_pts == 10:
    print("Player wins the match !!!!")
elif cpu_pts == 10:
    print("CPU wins the match !!")