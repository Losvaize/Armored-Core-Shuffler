class Head():
    weight: int
    energy_drain: int
    armor_point: int
    def_shell: int
    def_energy: int
    computer_type: str
    map_type: str
    noise_canceler: str
    bio_sensor: str
    radar_function: str
    radar_range: str
    radar_type: str

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_drain: int, armor_point: int,
                 def_shell: int, def_energy: int, computer_type: str, 
                 map_type: str, noise_canceler: str, bio_sensor: str,
                 radar_function: str, radar_range: int = -1, radar_type: str = "", tier = int ):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.armor_point = armor_point
        self.def_shell = def_shell
        self.def_energy = def_energy
        self.computer_type = computer_type
        self.map_type = map_type
        self.noise_canceler = noise_canceler
        self.bio_sensor = bio_sensor
        self.radar_function = radar_function
        self.radar_range = radar_range
        self.radar_type = radar_type
        self.tier = tier # Tier 1 Lowest, Tier 4 Highest

all_heads = (
    Head(0x00, "HD-01-SRVT", "HEAD UNIT", 26500, 122, 350, 816, 154, 149, "DETAILED", "AREA MEMORY", "NONE", "PROVIDED", "NONE", 1), #Head unit with built-in bio sensor.
    Head(0x01, "HD-2002", "HEAD UNIT", 29000, 156, 457, 787, 140, 154, "STANDARD", "AREA MEMORY", "NONE", "NONE", "PROVIDED", 6000, "STANDARD", 2), #Head unit equipped with radar function.
    Head(0x02, "HD-X1487", "HEAD UNIT", 19000, 166, 420, 975, 160, 185, "ROUGH", "NO MEMORY", "PROVIDED", "PROVIDED", "NONE", 1), #Full range of sensors but without the auto-map function.
    Head(0x03, "HD-REDEYE", "HEAD UNIT", 41100, 146, 538, 840, 148, 151, "DETAILED", "AREA&PLACE NAME", "NONE", "NONE", "PROVIDED", 5980, "STANDARD", 3), #Equipped with radar and an enhanced auto-map function.
    Head(0x04, "HS-D-9066", "HEAD UNIT", 43200, 138, 657, 885, 165, 232, "STANDARD", "AREA MEMORY", "NONE", "PROVIDED", "PROVIDED", 6120, "STANDARD", 2), #Full range of options and good EG shields.
    Head(0x05, "HD-GRY-NX", "HEAD UNIT", 14700, 232, 218, 1001, 194, 134, "ROUGH", "NO MEMORY", "NONE", "NONE", "NONE", 1), #Economy Unit with good shields but no optional equipment.
    Head(0x06, "HD-06-RADAR", "HEAD UNIT", 51800, 145, 875, 741, 109, 194, "STANDARD", "AREA&PLACE NAME", "PROVIDED", "NONE", "PROVIDED", 8120, "STANDARD", 3), #Equiped with wide-area radar and various options.
    Head(0x07, "HD-ONE", "HEAD UNIT", 68100, 161, 304, 800, 132, 129, "DETAILED", "AREA MEMORY", "PROVIDED", "PROVIDED", "PROVIDED", 7980, "STANDARD", 4), #Fully equipped with wide-area radar and all options.
    Head(0x08, "HD-08-DISH", "HEAD UNIT", 33200, 133, 716, 870, 205, 162, "STANDARD", "AREA&PLACE NAME", "NONE", "NONE", "NONE", 2), #Equipped with an enhanced auto-map function.
    Head(0x09, "HD-ZERO", "HEAD UNIT", 22500, 185, 431, 925, 221, 149, "ROUGH", "NO MEMORY", "NONE", "NONE", "PROVIDED", 6300, "STANDARD", 3), #Equipped with radar functions and enhanced shock protection.
)