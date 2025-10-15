import Parts
import random
#testing weighted probabilities

def get_random_head_by_tier():
    tiers = [1, 2, 3, 4]
    tier_weights = [50, 25, 15, 10]

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
    tier_weights = [50, 35, 15, 10]

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
    tier_weights = [50, 35, 15, 10]

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
    tier_weights = [50, 35, 15]

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
    tier_weights = [60, 30, 10, 0]

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
    tier_weights = [50, 35, 15]

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
    tier_weights = [50, 35, 15, 0]

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
    tier_weights = [50, 35, 15]

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

def get_Back_Weapon_by_tier(guarantee_unlocked):
    tiers = [1, 2, 3, 4]
    tier_weights = [50, 25, 15, 10]
      
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
    
    return back_weapon


def main():
    ac_head = get_random_head_by_tier()
    ac_core = get_random_core_by_tier()
    ac_arms = get_random_arms_by_tier()
    ac_legs = get_random_legs_by_tier()
    ac_booster = get_random_booster_by_tier()
    ac_generator = get_random_generator_by_tier()
    ac_FCS = get_random_FCS_by_tier()
    ac_arm_weapon_r = get_random_Arm_Weapon_R_by_tier()
    ac_arm_weapon_l = get_random_Arm_Weapon_L_by_tier()


    percentage_chance_r = 50
    percentage_chance_l = 50
    percentage_chance_back_r = 50
    percentage_chance_back_l = 50

    ac_remaining_weight = ac_legs.max_weight - ac_core.weight - ac_generator.weight - ac_arms.weight - ac_booster.weight - ac_head.weight - ac_FCS.weight

    ac_core_weight = ac_core.max_weight - ac_arms.weight

    ac_remaining_energy = ac_generator.energy_output - ac_core.energy_drain - ac_legs.energy_drain - ac_arms.energy_drain - ac_booster.energy_drain - ac_head.energy_drain - ac_FCS.energy_drain
    
    if  ac_arms.humanoid_arm == True:
        if  0 <= percentage_chance_r <= 100:
            ac_arm_weapon_r = get_random_Arm_Weapon_R_by_tier()
        if random.random() < percentage_chance_r / 100:
                ac_remaining_weight -= ac_arm_weapon_r.weight
        else:
            ac_arm_weapon_r.name = "NO EQUIP"

        if 0 <= percentage_chance_l <= 100:
            if ac_arm_weapon_r.name == "NO EQUIP":
                percentage_chance_l = 100
            ac_arm_weapon_l = get_random_Arm_Weapon_L_by_tier()
            if random.random() < percentage_chance_l / 100:
                ac_remaining_weight -= ac_arm_weapon_l.weight
            else:
                ac_arm_weapon_l.name = "NO EQUIP"

    if ac_arms.humanoid_arm == False: #Flag for Weapon names 
        ac_arm_weapon_r.name = "EQUIPMENT IMPOSSIBLE"
        ac_arm_weapon_l.name = "EQUIPMENT IMPOSSIBLE"


# I 100% chance want a back weapon when I have less than 2 Arm weapons or I have Gun arms.
# I want a 50% chance of a Back weapon when I have 2 Weapons.

    if ac_arm_weapon_l.name or ac_arm_weapon_r.name == "NO EQUIP" or "EQUIPMENT IMPOSSIBLE":
        percentage_chance_back_r = 100
    ac_back_weapon_r = get_Back_Weapon_by_tier(guarantee_unlocked = percentage_chance_back_r == 100)
    if random.random() < percentage_chance_back_r / 100:
        ac_remaining_weight -= ac_back_weapon_r.weight
    else : ac_back_weapon_r.name = "NO EQUIP"
        
# I want a 25% chance of a 2nd back weapon when I have any of the above (back weapon L)

    if ac_arm_weapon_r == True:
        ac_remaining_energy -= ac_arm_weapon_r.energy_drain

    if ac_arm_weapon_l == True:
        ac_remaining_energy -= ac_arm_weapon_l.energy_drain
    if ac_back_weapon_r == True:
        ac_remaining_energy -= ac_back_weapon_r.energy_drain
    #if ac_back_weapon_l == True:
    #    ac_remaining_energy -= ac_back_weapon_l.energy_drain

    if ac_arms.humanoid_arm == False: #Flag for Weapon names 
        ac_arm_weapon_r.name = "EQUIPMENT IMPOSSIBLE"
        ac_arm_weapon_l.name = "EQUIPMENT IMPOSSIBLE"

    if (ac_remaining_weight < 0 or ac_core_weight < 0 or ac_remaining_energy < 0):
        invalid_AC = True

    print (ac_head.name)
    print (ac_core.name)
    print (ac_arms.name)
    print (ac_legs.name)
    print (ac_booster.name)
    print (ac_generator.name)
    print (ac_FCS.name)
    print (ac_arm_weapon_r.name)
    print (ac_arm_weapon_l.name)
    print (ac_back_weapon_r.name)

#Todd wanted me to Loop this over so that all the parameters are met for a valid AC project for later.

    print(f"Remaining Weight:", ac_remaining_weight, f"Remaining Arm Weight:", ac_core_weight, f"Remaining Energy:", ac_remaining_energy)

if __name__ == "__main__":
    main()