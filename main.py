#Import all Parts from Databases
import random
import Legs
import Cores
import Generators
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

def main():
    #Defining each maximum part value
    ac_remaining_weight = 0
    ac_core_weight = 0
    ac_remaining_energy = 0
    
    ac_legs = shuffle_random_leg ()
    ac_core = shuffle_random_core ()
    ac_generator = shuffle_random_generator()
    
    
    ac_remaining_weight = ac_legs.max_weight - ac_core.weight - ac_generator.weight
    ac_core_weight = ac_core.max_weight
    ac_remaining_energy = ac_generator.energy_output - ac_core.energy_drain - ac_legs.energy_drain 

    print(ac_legs.name, f"Max Weight:", ac_legs.max_weight)
    print(ac_core.name, f"Arm Weight Remaining:", ac_core_weight ) 
    print(ac_generator.name)
    print(f"Remaining Weight:", ac_remaining_weight, f"Remaining Arm Weight:", ac_core_weight, f"Remaining Energy:", ac_remaining_energy )

if __name__ == "__main__":
    main()

