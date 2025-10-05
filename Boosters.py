class Booster():
    weight: int
    energy_drain: int
    boost_power: int
    charge_drain: int

    def __init__(self, 
                 _id: int, 
                 name: str, 
                 part_type: str, 
                 price: int,
                 weight: int, 
                 energy_drain: int, 
                 boost_power: int,
                 charge_drain: int,
                 tier:int):
        
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.boost_power = boost_power
        self.charge_drain = charge_drain
        self.tier = tier # Tier 1 lowest. Tier 4 Highest

all_boosters = (
    Booster(0x57, "B-P320", "BOOST UNIT", 10800, 208, 28, 9800, 4360, 1), #Low priced but seems a bit underpowered.
    Booster(0x58, "B-P350", "BOOST UNIT", 13700, 162, 33, 12800, 4410, 1), #Economy type with high power but high energy consumption.
    Booster(0x59, "B-T001", "BOOST UNIT", 34000, 149, 30, 17300, 4600, 2), #Achieves both enhanced power and low weight at the same time.
    Booster(0x5A, "B-T2", "BOOST UNIT", 31500, 235, 38, 14800, 3850, 2), #Power itself is low but offers the highest efficiency.
    Booster(0x5B, "B-P351", "BOOST UNIT", 25500, 288, 41, 21000, 6980, 2), #High-Performance model with both high power and energy consumption.
    Booster(0x5C, "B-VR-33", "BOOST UNIT", 48500, 255, 35, 19000, 5070, 3) #Maintains the top-class power to achieve good efficiency.
)