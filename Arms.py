class Arms():
    weight: int
    energy_drain: int
    armor_point: int
    def_shell: int
    def_energy: int
    weapon_lock: str
    attack_power: int
    number_of_ammo: int
    ammo_type: str
    ammo_price: int
    arms_range: int
    maximum_lock: int
    reload_time: int

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
                 tier: int,
                 humanoid_arm: bool,  
                 weapon_lock: str = "",
                 attack_power: int = -1, 
                 number_of_ammo: int = -1,
                 ammo_type: str = "", 
                 ammo_price: int = -1, 
                 arms_range: int = -1,
                 maximum_lock: int = -1, 
                 reload_time: int = -1,
                 fire_unlocked : bool = -1,):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.armor_point = armor_point
        self.def_shell = def_shell
        self.def_energy = def_energy
        self.tier = tier #Tier 1 is lowest, Tier 4 is highest.
        self.humanoid_arm = humanoid_arm # Can hold L or R arm weapons. 
        self.weapon_lock = weapon_lock
        self.attack_power = attack_power
        self.number_of_ammo = number_of_ammo
        self.ammo_type = ammo_type
        self.ammo_price = ammo_price
        self.arms_range = arms_range
        self.maximum_lock = maximum_lock
        self.reload_time = reload_time
        self.fire_unlocked = fire_unlocked # can fire unlocked, needed for progression.

all_arms= (
    Arms(0x0D, "AN-101", "ARM UNIT", 19000, 1228, 1006, 1670, 384, 374, 1, True), #Normal arm units with average performance.
    Arms(0x0E, "AN-201", "ARM UNIT", 15300, 1054, 877, 1635, 352, 334, 1, True), #Low energy consumption version of the AN-101.
    Arms(0x0F, "AN-K1", "ARM UNIT", 49000, 905, 930, 1790, 337, 402, 3, True), #Reduced-weight arm units with full AP and shields.
    Arms(0x10, "AN-D-7001", "ARM UNIT", 23000, 1445, 1512, 1743, 306, 453, 1, True), #Average arm units with enhanced performance.
    Arms(0x11, "AN-3001", "ARM UNIT", 39500, 1612, 1258, 1935, 487, 353, 2, True), #Middleweight arms with maximum energy shielding.
    Arms(0x12, "ANKS-1A46J", "ARM UNIT", 42100, 2120, 1415, 1990, 679, 496, 3, True), #Offers the maximum AP but interferes with some parts.
    Arms(0x13, "AN-863-B", "ARM UNIT", 34000, 1726, 1394, 1880, 517, 406, 2, True), #Weight is increased for added durability.
    Arms(0x14, "AN-25", "ARM UNIT", 28400, 853, 682, 1826, 344, 284, 3, True), #Lightweight type arm units with better performance.
    Arms(0x15, "AW-MG25/2", "MACHINE GUN", 54500, 1193, 78, 812, 0, 0, 1, False,  "SPECIAL", 158, 400, "SOLID", 33, 8800, 1, 2, True), #Can strafe with 4 rifles at once
    Arms(0x16, "AW-GT2000", "GATLING GUN", 48600, 1415, 92, 1132, 0, 0, 2, False, "SPECIAL", 305, 300, "SOLID", 62, 7800, 1, 2, True), #Dual Gatling guns can concentrate high-speed rounds at a single point.
    Arms(0x17, "AW-RF105", "CANNON", 77600, 1530, 106, 1280, 0, 0, 3, False, "NARROW & DEEP", 1530, 100, "SOLID", 220, 9300, 1, 15, True), #2 cannons with incredible firepower.
    Arms(0x18, "AW-30/3", "DUAL MISSILE", 56400, 480, 377, 688, 0, 0, 2, False, "STANDARD", 830, 80, "SOLID", 130, 9000, 3, 10, False), #Fires 2 rounds of 3 small missiles for a total of 6 missiles.
    Arms(0x19, "AW-RF120", "CANNON", 67200, 1827, 137, 1420, 0, 0, 3, False, "NARROW & DEEP", 2120, 50, "SOLID", 300, 9800, 1, 18, True), #Enhanced dual cannons. Somewhat fewer shots. 
    Arms(0x1A, "AW-S60/2", "DUAL MISSILE", 66600, 762, 420, 725, 0, 0, 3, False, "STANDARD", 830, 120, "SOLID", 130, 9000, 2, 10, False), #Fires 2 rounds of 2 missiles at once for extra shots.
    Arms(0x1B, "AW-XC5500", "PLASMA CANNON", 83600, 1688, 547, 875, 0, 0, 4, False, "NARROW & DEEP", 1241, 70, "ENERGY", 0, 12000, 1, 7, True), #Energy weapon. Fires twin bursts of light.
    Arms(0x1C, "AW-XC65", "LASER CANNON", 98500, 1905, 625, 792, 0, 0, 4, False, "NARROW & DEEP", 2322, 40, "ENERGY", 0, 8300, 1, 10, True) #Energy Weapon. Fires two beams. 
)