#Import all Parts from Databases
import random
import Legs
import Cores
import Generators
import Heads 
import Arms
import Boosters
import FCS
import Arm_Weapon_R
import Arm_Weapon_L
import Back_Weapons


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

def shuffle_random_head():
    random_head = random.choice(Heads.all_heads)
    return(random_head)

def shuffle_random_FCS():
    random_FCS = random.choice(FCS.all_fcs)
    return(random_FCS)

def shuffle_random_arm_weapon_r():
    random_arm_weapon_r = random.choice(Arm_Weapon_R.all_arm_weapon_r)
    return(random_arm_weapon_r)

def shuffle_random_arm_weapon_l():
    random_arm_weapon_l = random.choice(Arm_Weapon_L.all_arm_weapon_l)
    return(random_arm_weapon_l)

def shuffle_back_weapon():
    random_back_weapon = random.choice(Back_Weapons.all_back_weapons) #attempting to set a %chance of a weapon being generated. 
    return(random_back_weapon)




def main():

    #Defining each maximum part value
    Valid_AC = ()
    ac_remaining_weight = 0
    ac_core_weight = 0
    ac_remaining_energy = 0
    
    ac_legs = shuffle_random_leg ()
    ac_core = shuffle_random_core ()
    ac_generator = shuffle_random_generator()
    ac_arms = shuffle_random_arms()
    ac_booster = shuffle_random_booster()
    ac_head = shuffle_random_head ()
    ac_FCS = shuffle_random_FCS ()
    ac_arm_weapon_r = shuffle_random_arm_weapon_r()
    ac_arm_weapon_l = shuffle_random_arm_weapon_l()

    percentage_chance = 50


    
    if 0 <= percentage_chance <= 100:
        if random.random() < percentage_chance / 100:
            ac_back_weapon_l = shuffle_back_weapon()



    ac_remaining_weight = ac_legs.max_weight - ac_core.weight - ac_generator.weight - ac_arms.weight - ac_booster.weight - ac_head.weight - ac_FCS.weight 

    if 0 <= percentage_chance <= 100:
            percentage_chance = 50
            ac_arm_weapon_r = shuffle_random_arm_weapon_r()
    if random.random() < percentage_chance / 100:
        if ac_arms.humanoid_arm == True:
            ac_remaining_weight -= ac_arm_weapon_r.weight
    else:
        ac_arm_weapon_r.name = "EQUIPMENT IMPOSSIBLE"


    if 0 <= percentage_chance <= 100:
        if ac_arm_weapon_r == False and ac_arms.humanoid_arm == True:
            percentage_chance = 100
        ac_arm_weapon_l = shuffle_random_arm_weapon_l()
        if random.random() < percentage_chance / 100:
            ac_remaining_weight -= ac_arm_weapon_l.weight
        else:
            if ac_arms.humanoid_arm == False:
                ac_arm_weapon_l.name = "EQUIPMENT IMPOSSIBLE"
            ac_arm_weapon_l.name == "NO EQUIP"
            

    if 0 <= percentage_chance <= 100: #if part is generated, minus weight from total weight. 
        ac_back_weapon_r = shuffle_back_weapon()
        if random.random() < percentage_chance / 100:
            ac_remaining_weight -= ac_back_weapon_r.weight
        else:
            ac_back_weapon_r.name = "NO EQUIP"
    
    if 0 <= percentage_chance <= 100:
        if ac_back_weapon_r == False:
            percentage_chance = 100
        ac_back_weapon_l = shuffle_back_weapon()
        if random.random() < percentage_chance / 100:
            ac_remaining_weight -= ac_back_weapon_l.weight
        else:
            ac_back_weapon_l.name = "NO EQUIP"


    

    ac_core_weight = ac_core.max_weight - ac_arms.weight
    if ac_arms.humanoid_arm == True:
        ac_core_weight -= ac_arm_weapon_r.weight - ac_arm_weapon_l.weight

    ac_remaining_energy = ac_generator.energy_output - ac_core.energy_drain - ac_legs.energy_drain - ac_arms.energy_drain - ac_booster.energy_drain - ac_head.energy_drain - ac_FCS.energy_drain
    if ac_arm_weapon_r == True:
        ac_remaining_energy -= ac_arm_weapon_r.energy_drain
    if ac_arm_weapon_l == True:
        ac_remaining_energy -= ac_arm_weapon_l.energy_drain
    if ac_back_weapon_r == True:
        ac_remaining_energy -= ac_back_weapon_r.energy_drain
    if ac_back_weapon_l == True:
        ac_remaining_energy -= ac_back_weapon_l.energy_drain

    if (ac_remaining_weight < 0 or ac_core_weight < 0 or ac_remaining_energy < 0):
        invalid_AC = True
    else:
        invalid_AC = False

    while (invalid_AC):  
        if (ac_remaining_weight < 0):    
            invalid_AC = True
            return print("INVALID AC CONFIGURATION - OVERWEIGHT ", ac_remaining_weight) #closes recursion loop, modify later to add new part.
        if (ac_core_weight < 0):
            invalid_AC = True
            return print("INVALID AC CONFIGURATION - ARMS OVERWEIGHT ", ac_core_weight) 
        if (ac_remaining_energy <0):
            invalid_AC = True
            return print("INVALID AC CONFIGURATION - NOT ENOUGH ENERGY ", ac_remaining_energy) 
        else:
            invalid_AC = False
    
    print(ac_legs.name, f"Max Weight:", ac_legs.max_weight)
    print(ac_core.name, f"Arm Weight Remaining:", ac_core_weight ) 
    print(ac_arms.name)
    print(ac_generator.name)
    print(ac_booster.name)
    print(ac_head.name)
    print(ac_FCS.name)
    print(ac_arm_weapon_r.name)
    print(ac_arm_weapon_l.name)
    print(ac_back_weapon_r.name)
    print(ac_back_weapon_l.name)
    print(f"Remaining Weight:", ac_remaining_weight, f"Remaining Arm Weight:", ac_core_weight, f"Remaining Energy:", ac_remaining_energy)
    
    return(Valid_AC)

if __name__ == "__main__":
    main()

