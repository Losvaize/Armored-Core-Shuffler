class Arm_Weapon_R():
    weight: int
    energy_drain: int
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
                 weapon_lock: str, 
                 attack_power: int, 
                 number_of_ammo: int, 
                 ammo_type: str, 
                 ammo_price: int, 
                 arms_range: int, 
                 maximum_lock: int, 
                 reload_time: int): #STILL NEED TO ADD TIERS.
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.weapon_lock = weapon_lock
        self.attack_power = attack_power
        self.number_of_ammo = number_of_ammo
        self.ammo_type = ammo_type
        self.ammo_price = ammo_price
        self.arms_range = arms_range
        self.maximum_lock = maximum_lock
        self.reload_time = reload_time

all_arm_weapon_r = (
    Arm_Weapon_R(0x7F, "NO WEAPON", "- - - - - - - -", 0, 0, 0, "WIDE & SHALLOW", 0, 0, "- - - - - -", 0, 0, 0, 0), #
    Arm_Weapon_R(0x80, "WG-RF35", "RIFLE", 11400, 415, 6, "WIDE & SHALLOW", 218, 200, "SOLID", 18, 8500, 1, 5), #Standard portable rifle. Suitable for various missions.
    Arm_Weapon_R(0x81, "WG-MGA1", "MACHINE GUN", 14000, 370, 4, "WIDE & SHALLOW", 85, 500, "SOLID", 9, 6300, 1, 1), #Fast-reloading solid round machine gun. Low single-round firepower.
    Arm_Weapon_R(0x82, "WG-MG500", "MACHINE GUN", 28400, 458, 4, "WIDE & SHALLOW", 135, 500, "SOLID", 15, 7800, 1, 2), #Enhanced version of the machine gun with higher firepower.
    Arm_Weapon_R(0x83, "WG-AR1000", "MACHINE GUN", 42300, 516, 8, "SPECIAL", 105, 1000, "SOLID", 12, 7000, 1, 1), #Most powerful portable type machine gun.
    Arm_Weapon_R(0x84, "WG-HG235", "HAND GUN", 19000, 170, 22, "WIDE & SHALLOW", 226, 100, "SOLID", 68, 4800, 1, 5), #Wide scatter-shot pistol. Very short range.
    Arm_Weapon_R(0x85, "WG-RF/5", "SNIPER RIFLE", 41500, 295, 5, "SPECIAL", 530, 80, "SOLID", 83, 20000, 1, 10), #Long-barrel sniper rifle.
    Arm_Weapon_R(0x86, "WG-RF/P", "SNIPER RIFLE", 33100, 308, 4, "SPECIAL", 612, 60, "SOLID", 95, 16000, 1, 12), #Superior firepower and range, but low reload rate.
    Arm_Weapon_R(0x87, "WG-HG512", "HAND GUN", 26200, 324, 10, "WIDE & SHALLOW", 437, 120, "SOLID", 48, 5800, 1, 8), #Lower performance, but inexpensive.
    Arm_Weapon_R(0x88, "WG-FG99", "FLAMETHROWER", 58300, 352, 9, "NONE", 512, 500 , "SOLID", 41, 900, 1, 1), #Close-in combat gun shows off its true worth in hand-to-hand combat.
    Arm_Weapon_R(0x89, "WG-B2120", "BAZOOKA", 59740, 778, 13, "NARROW & DEEP", 1250, 80, "SOLID", 163, 8200, 1, 16), #High firepower but slow-moving bazooka fire is easily avoidable.
    Arm_Weapon_R(0x8A, "WG-B2180", "BAZOOKA", 75900, 905, 16, "NARROW & DEEP", 1930, 50, "SOLID", 348, 7800, 1, 22), #Ultra-attack bazooka for betting it all on one shot.
    Arm_Weapon_R(0x8B, "WG-XP1000", "PULSE RIFLE", 46000, 188, 246, "SPECIAL", 302, 180, "ENERGY", 0, 15000, 1, 3), #Energy weapon. Noted for its long range and reload speed.
    Arm_Weapon_R(0x8C, "WG-XP2000", "PULSE RIFLE", 61500, 265, 285, "SPECIAL", 435, 200, "ENERGY", 0, 18000, 1, 6), #Energy weapon. Emphasizes its long range and number of shots.
    Arm_Weapon_R(0x8D, "WG-XC4", "LASER RIFLE", 51000, 686, 308, "SPECIAL", 820, 100, "ENERGY", 0, 8000, 1, 10), #Energy weapon. High firepower and energy consumption.
    Arm_Weapon_R(0x8E, "WG-1-KARASAWA", "LASER RIFLE", 75000, 1000, 422, "SPECIAL", 1550, 50, "ENERGY", 0, 10000, 1, 8) #Energy Weapon. Powerful but heavy.
)