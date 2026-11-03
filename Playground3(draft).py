so_bi_mat = 7
du_doan = int(input("Choose a number from 1-10: "))

while du_doan != so_bi_mat:
    du_doan = int(input("Guess again: "))
    if du_doan == so_bi_mat:
        print("Right!")
    elif du_doan > so_bi_mat:
        print("Too high!")
    else:
        print("Too low!")