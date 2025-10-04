import random
import Legs
import Cores

def shuffle_random_leg ():
    random_legs = random.choice(Legs.all_legs)
    if (random_legs.name == "DUMMY"):
        is_dummy = True
    else:
        is_dummy = False
    
    while (is_dummy):
        random_legs = random.choice(Legs.all_legs)
        if (random_legs.name == "DUMMY"):
            is_dummy = True
        else:
            is_dummy = False

    #print(random_legs.name)
    return(random_legs)

def shuffle_random_core ():
    random_core = random.choice(Cores.all_cores)
    return(random_core)

def main():
    #Defining each maximum part value
    ac_remaining_weight = 0
    ac_core_weight = 0
    #ac_total_energy = 0
    
    ac_legs = shuffle_random_leg ()
    ac_core = shuffle_random_core ()

    ac_remaining_weight = ac_legs.max_weight - ac_core.weight
    ac_core_weight = ac_core.max_weight

    print(ac_legs.name, ac_legs.max_weight, ac_remaining_weight, ac_core.name, ac_core.weight)


if __name__ == "__main__":
    main()

