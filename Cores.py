class Core():
    weight: int
    energy_drain: int
    armor_point: int
    def_shell: int
    def_energy: int
    max_weight: int
    anti_missile_response: int
    anti_missile_angle: int
    extension_slots: int

    def __init__(self, 
                 _id: int, 
                 name: str, 
                 part_type: str, 
                 price: int,
                 weight: int, 
                 energy_drain: int, 
                 armor_point: int,
                 def_shell: int, 
                 def_energy: int, 
                 max_weight: int,
                 anti_missile_response: int, 
                 anti_missile_angle: int,
                 extension_slots: int,
                 tier = int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.armor_point = armor_point
        self.def_shell = def_shell
        self.def_energy = def_energy
        self.max_weight = max_weight
        self.anti_missile_response = anti_missile_response
        self.anti_missile_angle = anti_missile_angle
        self.extension_slots = extension_slots
        self.tier = tier # Tier 1 lowest. Tier 4 Highest

all_cores =(
    Core(0x0A, "XCA-00", "CORE UNIT", 61500, 1103, 1046, 2710, 530, 505, 2770, 48, 48, 8, 1), #Standard core unit with average performance overall.
    Core (0x0B, "XCL-01", "CORE UNIT", 88000, 885, 1380, 2380, 492, 610, 2450, 45, 64, 16, 2), #Electronic warfare core with many slots for special equipment.
    Core (0x0C, "XCH-01", "CORE UNIT", 72000, 1384, 873, 3015, 615, 543, 3600, 48, 32, 12, 2), #Heavyweight core with an excellent shoulder load and heavy armor.
)