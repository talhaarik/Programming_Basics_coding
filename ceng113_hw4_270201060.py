# Talha Arık 270201060

with open("TaskList.txt", "r") as file:
    task_list = [(line.strip()).split(",") for line in file]

print("Welcome to Hero’s 5 Labors!")
print("Remaining HP for Hero : 3000")
print("Remaining HP for Pegasus: 550")

hero_speed = 20
pegasus_speed = 50
passing_time = 0
total_time = 0
hero_HP, pegasus_HP = 3000, 550


def remaining_task(task_list, num=0):  # Print remaining tasks to the screen using recursive
    if num == 0:
        print(f"Here are the tasks left that hero needs to complete:")
        print(f"_____________________________________________________________\n"
              f"| TaskName    | ByFootDistance    | ByPegasus    | HPNeeded |\n"
              f"_____________________________________________________________")
    if num != len(task_list):
        print(f"| {task_list[num][0]}       | {(task_list[num][1]+' km').ljust(18, ' ')}"
              f"| {task_list[num][2]} km       | {task_list[num][3].ljust(9,' ')}|")
        remaining_task(task_list, num+1)

    if num == len(task_list):
        print("_____________________________________________________________")



def remaining_HP(going_by_what, time):  # the function of printing remaining HP to the screen
    global passing_time
    global hero_HP
    global pegasus_HP
    if (hero_HP < time * 10 and pegasus_HP < time * 15):
        print("Game over!")
        return "Game over!"

    if (going_by_what == "foot"):
        if(hero_HP >= time * 10):
            hero_HP = hero_HP - (time * 10)  # as hero will lose 10 hp per hour
        else:  # hero_HP is not sufficient for this task.
            print("Game over!")
            return "hero_HP is not sufficient"
    elif (going_by_what == "pegasus"):
        if(pegasus_HP >= time * 15):
            pegasus_HP = pegasus_HP - (time * 15)  # as pegasus will lose 15 hp per hour
        else:
            return "pegasus_HP is not sufficient"


def task_to_go():  # places where the hero will go
    global hero_HP
    global pegasus_HP
    global passing_time
    global total_time
    boss_HP = 0
    task_num = 0
    availability1 = False  # task control boolean
    going_where = ""
    while (not availability1):
        going_where = input("Where should Hero go next? ").lower()
        for item in range(len(task_list)):
            if (going_where == task_list[item][0].lower()):  # the situation where the task the user wants to go is in task_list
                availability1 = True
                task_num = item
                boss_HP = int(task_list[item][3])
                break
        if(availability1 == False):
            print("Invalid option.")
            continue

    availability2 = False  # vehicle control boolean

    while (not availability2):
        going_by_what = input("How do you want to travel?(Foot/Pegasus) ").lower()

        if (going_by_what == "foot" and (going_where == "task1" or going_where == "task2")):  # You cannot go to task1 and task2 by foot.
            print("You cannot go there by foot.")
            if (pegasus_HP < passing_time * 15):
                print("Game over!")
                return going_where, False
            if (hero_HP < passing_time * 10 and pegasus_HP < passing_time * 15):
                print("Game over!")
                return going_where, False

            availability2 = False
            continue
        elif (going_by_what not in ("pegasus", "foot")):
            print("Invalid option.")
            availability2 = False
            continue
        else:
            availability2 = True

            if (going_by_what == "foot"):
                for i in range(len(task_list)):
                    if (task_list[i][0].lower() == going_where):
                        passing_time = (int(task_list[i][1]) / hero_speed)  # time = distance / velocity
                call_the_func = remaining_HP(going_by_what, passing_time)
                if (call_the_func == "hero_HP is not sufficient"):
                    availability2 = False
                    continue
                if(call_the_func == "Game over!"):
                    return going_where, False


            elif (going_by_what == "pegasus"):
                for i in range(len(task_list)):
                    if (task_list[i][0].lower() == going_where):
                        passing_time = (int(task_list[i][2]) / pegasus_speed)  # time = distance / velocity
                call_the_func = remaining_HP(going_by_what, passing_time)
                if (call_the_func == "pegasus_HP is not sufficient"):
                    availability2 = False
                    continue
                if (call_the_func == "Game over!"):
                    return going_where, False
    if(hero_HP < boss_HP):
        print("Game over!")
        return going_where, False
    else:
        total_time += passing_time
        hero_HP -= boss_HP
        print("Hero defeated the monster.")
        print("Time passed : {}".format(total_time), "hour"+"\n")
        print("Remaining HP for Hero : {}".format(hero_HP))
        print("Remaining HP for Pegasus : {}".format(pegasus_HP))
        return going_where, True

def go_home(going_where):  # return home after task function
    vehicle_control = False
    global hero_HP
    global pegasus_HP
    global passing_time
    global total_time
    for i in range(len(task_list)):
        if (task_list[i][0].lower() == going_where.lower()):
            task_num = i
    while (not vehicle_control):
        return_by_what = input("How do you want to go home?(Foot/Pegasus)").lower()
        if (return_by_what == "foot" and (going_where == "task1" or going_where == "task2")):  # You cannot go to task1 and task2 by foot.
            print("You cannot go there by foot.")
            if(pegasus_HP < passing_time * 15):
                print("Game over!")
                return going_where, False
            if (hero_HP < passing_time * 10 and pegasus_HP < passing_time * 15):
                print("Game over!")
                return going_where, False
            continue
        if (return_by_what not in ("foot","pegasus")):  # if a valid vehicle is not entered
            print("Invalid option.")
            vehicle_control = False
            continue
        if (return_by_what == "foot"):
            for i in range(len(task_list)):
                if (task_list[i][0].lower() == going_where):
                    passing_time = (int(task_list[i][1]) / hero_speed)
            call_the_func = remaining_HP(return_by_what, passing_time)
            if (call_the_func == "hero_HP is not sufficient"):
                vehicle_control = False
                continue
            if(call_the_func == "Game over!"):
                return going_where, False
            total_time += passing_time
            print("Hero arrived home.")
            print("Time passed : {}".format(total_time), "hour"+"\n")
            print("Remaining HP for Hero : {}".format(hero_HP))
            print("Remaining HP for Pegasus : {}".format(pegasus_HP))
            remove_task(task_num, 0)
            break

        if (return_by_what == "pegasus"):
            for i in range(len(task_list)):
                if (task_list[i][0].lower() == going_where):
                    passing_time = (int(task_list[i][2]) / pegasus_speed)
            call_the_func = remaining_HP(return_by_what, passing_time)
            if (call_the_func == "pegasus_HP is not sufficient"):
                vehicle_control = False
                continue
            elif (call_the_func == "Game over!"):
                return going_where, False
            total_time += passing_time
            print("Hero arrived home.")
            print("Time passed : {}".format(total_time), "hour"+"\n")
            print("Remaining HP for Hero : {}".format(hero_HP))
            print("Remaining HP for Pegasus : {}".format(pegasus_HP))
            remove_task(task_num, 0)
            break

def remove_task(task_num, a): # remove function with recursion
    if a == task_num:
        task_list.pop(a)
    else:
        return remove_task(task_num, a+1)

def main():
    destination = ""
    game_over = False
    remaining_task(task_list, 0)
    print("\n")
    while(task_list != []):
        destination, game_over = task_to_go()
        if (game_over == False):
            return
        if(go_home(destination) == "Game over!"):
            return
        if(task_list != []):
            remaining_task(task_list,0)
        else:
            print("Congratulations, you have completed the task.")
            name = input("What is your name : ")

            hall_of_fame_file = open("hall_of_fame.txt", "a")
            print("Hall of Fame\n"
                  "__________________________\n"
                  "| Name      | Finish Time|\n"
                  "__________________________")
            hall_of_fame_file.write(name + "," + str(total_time) + "\n")
            hall_of_fame_file = open("hall_of_fame.txt", "r")
            hall_of_fame_list = [(line.strip()).split(",") for line in hall_of_fame_file]

            hall_of_fame_list.sort(key=lambda a: a[1])
            for i in range(3):
                if (i < len(hall_of_fame_list)):
                    print(f"| {hall_of_fame_list[i][0].ljust(8, ' ')}  | {str(hall_of_fame_list[i][1]).ljust(4, ' ')} hour  |\n"
                          f"__________________________")
                else:
                    break

            hall_of_fame_file.close()


main()