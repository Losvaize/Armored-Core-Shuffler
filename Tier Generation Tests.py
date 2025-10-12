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


def main():
    ac_head = get_random_head_by_tier()
    ac_core = get_random_core_by_tier()
    ac_arms = get_random_arms_by_tier()
    ac_legs = get_random_legs_by_tier()
    ac_booster = get_random_booster_by_tier()
    ac_generator = get_random_generator_by_tier()
    ac_FCS = get_random_FCS_by_tier()

    ac_remaining_weight = ac_legs.max_weight - ac_core.weight - ac_generator.weight - ac_arms.weight - ac_booster.weight - ac_head.weight - ac_FCS.weight

    ac_core_weight = ac_core.max_weight - ac_arms.weight

    ac_remaining_energy = ac_generator.energy_output - ac_core.energy_drain - ac_legs.energy_drain - ac_arms.energy_drain - ac_booster.energy_drain - ac_head.energy_drain - ac_FCS.energy_drain
    
    print (ac_head.name)
    print (ac_core.name)
    print (ac_arms.name)
    print (ac_legs.name)
    print (ac_booster.name)
    print (ac_generator.name)
    print (ac_FCS.name) 
    print(f"Remaining Weight:", ac_remaining_weight, f"Remaining Arm Weight:", ac_core_weight, f"Remaining Energy:", ac_remaining_energy)

if __name__ == "__main__":
    main()