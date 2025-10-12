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

def get_random_legs_by_tier():
    tiers = [1, 2, 3, 4]
    tier_weights = [50, 35, 15, 10]

    selected_tier = random.choices(tiers, weights = tier_weights, k=1)[0]

    if selected_tier == 1:
        eligible_Legs = Parts.Legs_by_tier[1]
    elif selected_tier == 2:
        eligible_Legs = Parts.Legs_by_tier[2]
    elif selected_tier == 3 or selected_tier == 4:
        eligible_Legs  = Parts.all_legs
    else:
        return None

    return random.choice(eligible_Legs)

def main():
    ac_head = get_random_head_by_tier()
    ac_legs = get_random_legs_by_tier()
    ac_generator = get_random_generator_by_tier()

    print (ac_head.name)
    print (ac_legs.name)
    print (ac_generator.name) 

if __name__ == "__main__":
    main()