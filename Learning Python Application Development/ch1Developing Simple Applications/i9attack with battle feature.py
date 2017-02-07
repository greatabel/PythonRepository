import random
import textwrap

def print_bold(msg, end='\n'):
    print("\033[1m" + msg + "\033[0m", end=end)

def print_dotted_line(width=72):
    print('-'*width)

def show_theme_message(width):
    print_dotted_line()
    print("\033[1m" + "Attack of The Orcs v0.0.1;" + "\033[0m")

    msg = (
            "The war between humans and their arch enemies, Orcs, was in the "
            "offing. Sir Foo, one of the brave knights guarding the southern "
            "plains began a long journey towards the east through an unknown "
            "dense forest. On his way, he spotted a small isolated settlement."
            " Tired and hoping to replenish his food stock, he decided to take"
            " a detour. As he approached the village, he saw five huts. There "
            "was no one to be seen around. Hesitantly, he  decided to enter.."
          )
    print(textwrap.fill(msg, width=width))

def show_game_mission():
    print_bold("Mission:")
    print("\tChoose a hut where Sir Foo can rest...")
    print_bold("TIP:")
    print("Be careful as there are enemies lurking around!")
    print_dotted_line()

def occupy_huts():
    huts = []
    occupants = ['enemy', 'friend', 'unoccupied']
    while len(huts) < 5:
        coumputer_choice = random.choice(occupants)
        huts.append(coumputer_choice)
    return huts

def reveal_occupants(idx, huts):
    # Print the occupant info
    print("Revealing the occupants...")
    # print('*'*5, idx, huts[idx-1])
    msg = ""
    for i in range(len(huts)):
        occupant_info = "<%d:%s>" % (i + 1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "
    print("\t" + msg)
    print_dotted_line()

def process_user_choice():
    # Prompt user to select a hut
    msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx

def show_health(health_meter, bold=False):
    msg = "Health: Sir Foo: %d, Enemy: %d" \
          % (health_meter['player'], health_meter['enemy'])
    if bold:
        print_bold(msg)
    else:
        print(msg)

def attack(health_meter):
    hit_list = 4 * ['player'] + 6 * ['enemy']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("ATTACK! ", end='')
    show_health(health_meter)


def enter_hut(idx, huts,health_meter):
    # Determine and announce the winner
    if huts[idx-1] != 'enemy':
        print_bold("Congratulations! YOU WIN!!!")
    else:
        print_bold("ENEMY Sighted!", end='')
        show_health(health_meter, bold=True)

        continue_attck = True
        while continue_attck:
            continue_attck = input("...continue attack? (y/n): ")
            if continue_attck == 'n':
                print_bold("Running Away with following health status..")
                show_health(health_meter, bold=True)
                print_bold("Game Over!")
                break

            attack(health_meter)
            # Check if either one of the opponents is defeated
            if health_meter['enemy'] <= 0:
                print_bold("GOOD JOB! Enemy defeated! YOU WIN!!!")
                break

            if health_meter['player'] <= 0:
                print_bold("YOU LOSE  :(  Better luck next time")
                break

    print_dotted_line()

def reset_health_meter(health_meter):
    health_meter['player'] = 40
    health_meter['enemy'] = 30

def play_game(health_meter):
    huts = occupy_huts()
    idx = process_user_choice()
    reveal_occupants(idx, huts)
    print_bold("Entering hut %d..." % idx)
    enter_hut(idx, huts,health_meter)

def run_application():
    keep_playing = 'y'
    width = 72
    health_meter = {}
    reset_health_meter(health_meter)

    show_theme_message(width)
    show_game_mission()

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("Play again? Yes(y)/No(n):")

if __name__ == "__main__":
    run_application()
