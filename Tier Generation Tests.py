import Parts
import random
#testing weighted probabilities

def get_random_head_by_tier():
    tiers = [1, 2, 3, 4] 
    tier_weights = [100, 0, 0, 0] # %chance of each part being selected by the tier.

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_heads = Parts.heads_by_tier[1]
    elif selected_tier == 2:
        eligible_heads = Parts.heads_by_tier[2]
    elif selected_tier == 3:
        eligible_heads = Parts.heads_by_tier[3]
    elif selected_tier == 4:
        eligible_heads = Parts.all_heads
    else:
        return None
    
    #print(f"Selected tier: {selected_tier}")
    #print(f"Eligible heads for this tier: {eligible_heads}")

    return random.choice(eligible_heads)

def get_random_core_by_tier():
    tiers = [1, 2]
    tier_weights = [50, 50]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_cores = Parts.Cores_by_tier[1]
    elif selected_tier == 2:
        eligible_cores  = Parts.all_cores
    else:
        return None

    return random.choice(eligible_cores)

def get_random_arms_by_tier():
    tiers = [1, 2, 3, 4]
    tier_weights = [100, 0, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_Arms = Parts.Arms_by_tier[1]
    elif selected_tier == 2:
        eligible_Arms = Parts.Arms_by_tier[2]
    elif selected_tier == 3 or selected_tier == 4:
        eligible_Arms  = Parts.all_arms
    else:
        return None

    return random.choice(eligible_Arms)

def get_random_legs_by_tier():
    tiers = [1, 2, 3, 4]
    tier_weights = [100, 0, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_Legs = Parts.Legs_by_tier[1]
    elif selected_tier == 2:
        eligible_Legs = Parts.Legs_by_tier[2]
    elif selected_tier == 3:
        eligible_Legs  = Parts.Legs_by_tier[3]
    elif selected_tier == 4:
        eligible_Legs = Parts.Legs_by_tier[4]

    else:
        return None

    return random.choice(eligible_Legs)

def get_random_booster_by_tier():
    tiers = [1, 2, 3]
    tier_weights = [100, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_booster = Parts.Booster_by_tier[1]
    elif selected_tier == 2:
        eligible_booster = Parts.Booster_by_tier[2]
    elif selected_tier == 3:
        eligible_booster  = Parts.all_boosters
    else:
        return None

    return random.choice(eligible_booster)

def get_random_generator_by_tier():
    tiers = [1, 2, 3, 4]
    tier_weights = [100, 0, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_generators = Parts.generator_by_tier[1]
    elif selected_tier == 2:
        eligible_generators = Parts.generator_by_tier[2]
    elif selected_tier == 3 or selected_tier == 4:
        eligible_generators = Parts.all_generators
    else:
        return None

    return random.choice(eligible_generators)

def get_random_FCS_by_tier():
    tiers = [1, 2, 3]
    tier_weights = [100, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_FCS = Parts.FCS_by_tier[1]
    elif selected_tier == 2:
        eligible_FCS = Parts.FCS_by_tier[2]
    elif selected_tier == 3:
        eligible_FCS  = Parts.all_fcs
    else:
        return None

    return random.choice(eligible_FCS)

def get_random_Arm_Weapon_R_by_tier():
    tiers = [1, 2, 3, 4]
    tier_weights = [100, 0, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_Arm_r = Parts.Arm_Weapon_R_by_tier[1]
    elif selected_tier == 2:
        eligible_Arm_r = Parts.Arm_Weapon_R_by_tier[2]
    elif selected_tier == 3:
        eligible_Arm_r = Parts.Arm_Weapon_R_by_tier[3]
    elif selected_tier == 4:
        eligible_Arm_r = Parts.all_arm_weapon_r
    else:
        return None

    return random.choice(eligible_Arm_r)

def get_random_Arm_Weapon_L_by_tier():
    tiers = [1, 2, 3]
    tier_weights = [100, 0, 0]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_Arm_l = Parts.Arm_Weapon_L_by_tier[1]
    elif selected_tier == 2:
        eligible_Arm_l = Parts.Arm_Weapon_L_by_tier[2]
    elif selected_tier == 3:
        eligible_Arm_l = Parts.Arm_Weapon_L_by_tier[3]
    elif selected_tier == 4:
        eligible_Arm_l = Parts.all_arm_weapon_l
    else:
        return None

    return random.choice(eligible_Arm_l)

def get_Back_Weapon_by_tier(guarantee_unlocked, RADAR):
    tiers = [1, 2, 3, 4]
    tier_weights = [100, 0, 0, 0]
      
    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_Back_Weapon = Parts.Back_Weapon_by_tier[1]
    elif selected_tier == 2:
        eligible_Back_Weapon = Parts.Back_Weapon_by_tier[2]
    elif selected_tier == 3:
        eligible_Back_Weapon = Parts.Back_Weapon_by_tier[3]
    elif selected_tier == 4:
        eligible_Back_Weapon = Parts.all_back_weapons
    else:
        return None

    back_weapon = random.choice(eligible_Back_Weapon)

    if guarantee_unlocked:
        if back_weapon.fire_unlocked == False:
            back_weapon_inelgible = True
        else:
            back_weapon_inelgible = False
        while (back_weapon_inelgible):
            back_weapon = random.choice(eligible_Back_Weapon)
            if back_weapon.fire_unlocked == False:
                back_weapon_inelgible = True
            else:
                back_weapon_inelgible = False
    
    if RADAR:
        if back_weapon.part_type == "RADAR":
            back_weapon_inelgible = True
        else:
            back_weapon_inelgible = False
        while (back_weapon_inelgible):
            back_weapon = random.choice(eligible_Back_Weapon)
            if back_weapon.part_type == "RADAR":
                back_weapon_inelgible = True
            else: 
                back_weapon_inelgible = False


    #print(f"Selected tier: {selected_tier}")
    #print(f"Eligible weapons for this tier: {eligible_Back_Weapon}")
    #print(guarantee_unlocked)

    return back_weapon


def generate_AC():
    ac_head = get_random_head_by_tier()
    ac_core = get_random_core_by_tier()
    ac_arms = get_random_arms_by_tier()
    ac_legs = get_random_legs_by_tier()
    ac_booster = get_random_booster_by_tier()
    ac_generator = get_random_generator_by_tier()
    ac_FCS = get_random_FCS_by_tier()
    ac_arm_weapon_r = get_random_Arm_Weapon_R_by_tier()
    ac_arm_weapon_l = get_random_Arm_Weapon_L_by_tier()

    ac_arm_weapon_r_status = "VALID"
    ac_arm_weapon_l_status = "VALID"
    ac_back_weapon_r_status = "VALID"
    ac_back_weapon_l_status = "VALID"
    percentage_chance_r = 80
    percentage_chance_l = 50
    percentage_chance_back_r = 50
    percentage_chance_back_l = 33

    ac_remaining_weight = ac_legs.max_weight - ac_core.weight - ac_generator.weight - ac_arms.weight - ac_booster.weight - ac_head.weight - ac_FCS.weight

    ac_core_weight = ac_core.max_weight - ac_arms.weight

    ac_remaining_energy = ac_generator.energy_output - ac_core.energy_drain - ac_legs.energy_drain - ac_arms.energy_drain - ac_booster.energy_drain - ac_head.energy_drain - ac_FCS.energy_drain
    
    if  ac_arms.humanoid_arm == True:
        if  0 <= percentage_chance_r <= 100:
            ac_arm_weapon_r = get_random_Arm_Weapon_R_by_tier()
        if random.random() < percentage_chance_r / 100:
                ac_remaining_weight -= ac_arm_weapon_r.weight
        else:
            ac_arm_weapon_r_status = "NO EQUIP"

        if 0 <= percentage_chance_l <= 100:
            if ac_arm_weapon_r_status == "NO EQUIP":
                percentage_chance_l = 100
            ac_arm_weapon_l = get_random_Arm_Weapon_L_by_tier()
            if random.random() < percentage_chance_l / 100:
                ac_remaining_weight -= ac_arm_weapon_l.weight
            else:
                ac_arm_weapon_l_status = "NO EQUIP"

    if ac_arms.humanoid_arm == False: #Flag for Weapon names 
        ac_arm_weapon_r_status = "EQUIPMENT IMPOSSIBLE"
        ac_arm_weapon_l_status = "EQUIPMENT IMPOSSIBLE"


# I 100% chance want a back weapon when I have less than 2 Arm weapons or I have Gun arms.
# I want a 50% chance of a Back weapon when I have 2 Weapons.

    if ac_arm_weapon_l_status == "NO EQUIP" or ac_arm_weapon_l_status == "EQUIPMENT IMPOSSIBLE" or ac_arm_weapon_r_status == "NO EQUIP" or ac_arm_weapon_r_status == "EQUIPMENT IMPOSSIBLE":    
        percentage_chance_back_r = 100
    ac_back_weapon_r = get_Back_Weapon_by_tier(guarantee_unlocked = ac_arms.humanoid_arm == False, RADAR = False)
    if random.random() < percentage_chance_back_r / 100:
        ac_remaining_weight -= ac_back_weapon_r.weight 
    
    else : 
        ac_back_weapon_r_status = "NO EQUIP"

    print (percentage_chance_back_r)    
# I want Back weapon L to have a 100% of generating a weapon if the Back weapon r is a radar, and the L cant be a radar.

    if ac_back_weapon_r.part_type == "RADAR":
        percentage_chance_back_l = 100
    ac_back_weapon_l = get_Back_Weapon_by_tier(guarantee_unlocked = False, RADAR = True)
    if random.random() < percentage_chance_back_l / 100:
        ac_remaining_weight -= ac_back_weapon_l.weight
    
    else : 
        ac_back_weapon_l_status = "NO EQUIP"
    
    print (percentage_chance_back_l) 

    if ac_arm_weapon_r == True:
        ac_remaining_energy -= ac_arm_weapon_r.energy_drain

    if ac_arm_weapon_l == True:
        ac_remaining_energy -= ac_arm_weapon_l.energy_drain
    if ac_back_weapon_r == True:
        ac_remaining_energy -= ac_back_weapon_r.energy_drain
    if ac_back_weapon_l == True:
        ac_remaining_energy -= ac_back_weapon_l.energy_drain

    if ac_arms.humanoid_arm == False: #Flag for Weapon names 
        ac_arm_weapon_r_status = "EQUIPMENT IMPOSSIBLE"
        ac_arm_weapon_l_status = "EQUIPMENT IMPOSSIBLE"

    if ac_arms.humanoid_arm == True:
        ac_core_weight -= ac_arm_weapon_r.weight - ac_arm_weapon_l.weight

    if (ac_remaining_weight < 0 or ac_core_weight < 0 or ac_remaining_energy < 0):
        invalid_AC = True
    else:
        invalid_AC = False

    return (invalid_AC, ac_head, ac_core, ac_arms, ac_legs, ac_booster, ac_generator, ac_FCS, ac_arm_weapon_r, ac_arm_weapon_l, ac_back_weapon_r, ac_back_weapon_l, ac_remaining_weight, ac_core_weight, ac_remaining_energy, ac_arm_weapon_r_status, ac_arm_weapon_l_status, ac_back_weapon_r_status, ac_back_weapon_l_status)


def main():
    (invalid_AC, ac_head, ac_core, ac_arms, ac_legs, ac_booster, ac_generator, ac_FCS, ac_arm_weapon_r, ac_arm_weapon_l, ac_back_weapon_r, ac_back_weapon_l, ac_remaining_weight, ac_core_weight, ac_remaining_energy, ac_arm_weapon_r_status, ac_arm_weapon_l_status, ac_back_weapon_r_status, ac_back_weapon_l_status) = generate_AC()
    
    while invalid_AC == True:
        print ("Invalid AC Detected: Retrying...")
        (invalid_AC, ac_head, ac_core, ac_arms, ac_legs, ac_booster, ac_generator, ac_FCS, ac_arm_weapon_r, ac_arm_weapon_l, ac_back_weapon_r, ac_back_weapon_l, ac_remaining_weight, ac_core_weight, ac_remaining_energy, ac_arm_weapon_r_status, ac_arm_weapon_l_status, ac_back_weapon_r_status, ac_back_weapon_l_status) = generate_AC()

    if ac_arm_weapon_l_status == "NO EQUIP":
        ac_arm_weapon_l = "NO EQUIP"
    if ac_arm_weapon_l_status == "EQUIPMENT IMPOSSIBLE":
        ac_arm_weapon_l = "EQUIPMENT IMPOSSIBLE"
    
    if ac_arm_weapon_r_status == "NO EQUIP":
        ac_arm_weapon_r = "NO EQUIP"
    if ac_arm_weapon_r_status == "EQUIPMENT IMPOSSIBLE":
        ac_arm_weapon_r = "EQUIPMENT IMPOSSIBLE"
    
    if ac_back_weapon_r_status == "NO EQUIP":
        ac_back_weapon_r = "NO EQUIP"
    if ac_back_weapon_l_status == "NO EQUIP":
        ac_back_weapon_l     = "NO EQUIP"

    print (ac_head.name)
    print (ac_core.name)
    print (ac_arms.name)
    print (ac_legs.name)
    print (ac_booster.name)
    print (ac_generator.name)
    print (ac_FCS.name)
    print (ac_arm_weapon_r)
    print (ac_arm_weapon_l)
    print (ac_back_weapon_r)
    print (ac_back_weapon_l)
    
    print(f"Remaining Weight:", ac_remaining_weight, f"Remaining Arm Weight:", ac_core_weight, f"Remaining Energy:", ac_remaining_energy)

if __name__ == "__main__":
    main()