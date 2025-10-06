#Import all Parts from Databases
import random
import Legs
import Cores
import Generators
import Arms
import Boosters

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

def shuffle_random_generator():
    random_generator = random.choice(Generators.all_generators)
    return(random_generator)

def shuffle_random_arms():
    random_arms = random.choice(Arms.all_arms)
    return(random_arms)

def shuffle_random_booster():
    random_booster = random.choice(Boosters.all_boosters)
    return(random_booster)

def main():
    #Defining each maximum part value
    Valid_AC = ""
    ac_remaining_weight = 0
    ac_core_weight = 0
    ac_remaining_energy = 0
    
    ac_legs = shuffle_random_leg ()
    ac_core = shuffle_random_core ()
    ac_generator = shuffle_random_generator()
    ac_arms = shuffle_random_arms()
    ac_booster = shuffle_random_booster()

    
    
    ac_remaining_weight = ac_legs.max_weight - ac_core.weight - ac_generator.weight - ac_arms.weight - ac_booster.weight
    ac_core_weight = ac_core.max_weight - ac_arms.weight -
    ac_remaining_energy = ac_generator.energy_output - ac_core.energy_drain - ac_legs.energy_drain - ac_arms.energy_drain - ac_booster.energy_drain

    if (ac_remaining_weight < 0 or ac_core_weight < 0 or ac_remaining_energy < 0):
        invalid_AC = True
    else:
        invalid_AC = False

    while (invalid_AC):  
        if (ac_remaining_weight < 0 or ac_core_weight < 0 or ac_remaining_energy < 0):
            invalid_AC = True
            return print("INVALID AC CONFIGURATION") #closes recursion loop, modify later.
        else:
            invalid_AC = False
    
    print(ac_legs.name, f"Max Weight:", ac_legs.max_weight)
    print(ac_core.name, f"Arm Weight Remaining:", ac_core_weight ) 
    print(ac_arms.name)
    print(ac_generator.name)
    print(f"Remaining Weight:", ac_remaining_weight, f"Remaining Arm Weight:", ac_core_weight, f"Remaining Energy:", ac_remaining_energy )
    
    return(Valid_AC)

if __name__ == "__main__":
    main()

