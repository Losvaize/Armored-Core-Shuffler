class Generator():
    weight: int
    energy_output: int
    maximum_charge: int
    charge_redzone: int

    def __init__(self, 
                 _id: int, 
                 name: str, 
                 part_type:str, 
                 price: int,
                 weight: int, 
                 energy_output: int, 
                 maximum_charge: int,
                 charge_redzone: int,
                 tier: int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_output = energy_output
        self.maximum_charge = maximum_charge
        self.charge_redzone = charge_redzone
        self.tier = tier # Tier 1 lowest. Tier 4 Highest

all_generators = (
    Generator(0x3D, "GPS-VVA", "PULSE GENERATOR", 19500, 308, 4728, 28000, 7800, 1), #Low in both power and capacity. Wide red zone.
	Generator(0x3E, "GPS-V6", "PULSE GENERATOR", 32000, 363, 4728, 43000, 5000, 1), #Load increased to nearly twice that of the GPS-VVA.
	Generator(0x3F, "GRD-RX5", "PULSE GENERATOR", 23300, 225, 5300, 38000, 4000, 1), #Balanced-performance generator.
	Generator(0x40, "GRD-RX6", "PULSE GENERATOR", 27800, 286, 6000, 33000, 4000, 1), #Performance not bad, but the equipment is so-so.
	Generator(0x41, "GRD-RX7", "PULSE GENERATOR", 38700, 348, 6810, 31500, 5000, 2), #Very good power but poor stamina.
	Generator(0x42, "GBG-10000", "PULSE GENERATOR", 43500, 398, 9988, 34000, 2980, 3), #High Power provides a wide selection of equipment.
	Generator(0x43, "GBG-XR", "PULSE GENERATOR", 56000, 452, 8207, 48000, 3250, 3), #Custom-made unit having both power and capacity.
    )