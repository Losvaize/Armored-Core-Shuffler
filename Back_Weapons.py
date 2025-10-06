class Back_Weapon():
    weight: int
    energy_drain: int
    radar_function: str
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
                 radar_function: str, 
                 weapon_lock: str, 
                 attack_power: int, 
                 number_of_ammo: int = -1, 
                 ammo_type: str = "", 
                 ammo_price: int = -1, 
                 arms_range: int = -1, 
                 maximum_lock: int = -1, 
                 reload_time: int = -1,
                 fire_unlocked = bool,
                 tier = int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.radar_function = radar_function
        self.weapon_lock = weapon_lock
        self.attack_power = attack_power
        self.number_of_ammo = number_of_ammo
        self.ammo_type = ammo_type
        self.ammo_price = ammo_price
        self.arms_range = arms_range
        self.maximum_lock = maximum_lock
        self.reload_time = reload_time
        self.fire_unlocked = fire_unlocked #can the weapon fire without a lock, needed for progression.
        self.tier = tier # Tier 1 Lowest, Tier 4 Highest

all_back_weapons = (
    Back_Weapon(0x5D, "WM-S40/1", "SMALL MISSILE", 18700, 245, 245, "NONE", "STANDARD", 830, 40, "SOLID", 130, 9000, 1, 10, False, 1), #Pod that fires single small missiles.
    Back_Weapon(0x5E, "WM-S40/2", "SMALL MISSILE", 23000, 337, 320, "NONE", "STANDARD", 830, 40, "SOLID", 130, 9000, 2, 10, False, 1), #Fires up to 2 small missiles at once.
    Back_Weapon(0x5F, "WM-S60/4", "SMALL MISSILE", 28800, 520, 349, "NONE", "STANDARD", 830, 60, "SOLID", 130, 9000, 4, 10, False, 1), #Fires up to 4 small missiles at once.
    Back_Weapon(0x60, "WM-S60/6", "SMALL MISSILE", 38100, 583, 353, "NONE", "STANDARD", 830, 60, "SOLID", 130, 9000, 6, 10, False, 2), #Fires up to 6 small missiles at once.
    Back_Weapon(0x61, "WM-MVG404", "MISSILE", 31000, 620, 280, "NONE", "STANDARD", 1560, 24, "SOLID", 252, 10000, 1, 10, False, 2), #Pod that fires singles missiles.
    Back_Weapon(0x62, "WM-MVG802", "MISSILE", 44000, 718, 220, "NONE", "STANDARD", 1560, 32, "SOLID", 252, 10000, 2, 10, False, 2), #Fires up to 2 missiles at once.
    Back_Weapon(0x63, "WM-L201", "LARGE MISSILE", 46200, 835, 180, "NONE", "STANDARD", 4300, 12, "SOLID", 897, 12500, 1, 10, False, 3), #Powerful large missiles fired singly
    Back_Weapon(0x64, "WM-X201", "MULTI MISSILE", 62250, 720, 250, "NONE", "STANDARD", 980, 18, "SOLID", 1125, 12000, 1, 15, False, 3), #Multi-warhead missile that scatters warheads in flight.
    Back_Weapon(0x65, "WM-X5-AA", "BOMB DISPENSER", 19300, 616, 85, "NONE", "NONE", 675, 10, "SOLID", 270, 0, 0, 50, True, 1), #Drops 8 ground-attack mines. For experts.
    Back_Weapon(0x66, "WM-X10", "BOMB DISPENSER", 24800, 939, 105, "NONE", "NONE", 675, 10, "SOLID", 560, 0, 0, 50, True, 1), #Drops 16 powerful ground-attack mines.
    Back_Weapon(0x67, "WM-P40001", "DUAL MISSILE", 43800, 755, 320, "NONE", "STANDARD", 830, 60, "SOLID", 130, 9000, 1, 10, False, 2), #Fires 2 left or right curving indirect attack missiles.
    Back_Weapon(0x68, "WM-PS-2", "TRIPLE MISSILE", 66700, 1125, 360, "NONE", "STANDARD", 830, 90, "SOLID", 130, 9000, 1, 10, False, 2), #Fires 3 up-curving indirect attack missiles.
    Back_Weapon(0x69, "WR-S50", "SMALL ROCKET", 15900, 218, 8, "NONE", "NONE", 1310, 50, "SOLID", 110, 12500, 0, 8, True, 1), #Carries 50 small rockets.
    Back_Weapon(0x6A, "WR-S100", "SMALL ROCKET", 32400, 846, 15, "NONE", "NONE", 1310, 100, "SOLID", 110, 12500, 0, 12, True, 2), #Carries 100 small rockets.
    Back_Weapon(0x6B, "WR-M50", "ROCKET", 27600, 677, 13, "NONE", "NONE", 2240, 50, "SOLID", 220, 14000, 0, 12, True, 2), #Carries 50 rockets.
    Back_Weapon(0x6C, "WR-M70", "ROCKET", 36500, 718, 24, "NONE", "NONE", 2240, 70, "SOLID", 220, 14000, 0, 16, True, 2), #Carries 70 rockets.
    Back_Weapon(0x6D, "WR-L24", "LARGE ROCKET", 29460, 805, 18, "NONE", "NONE", 3980, 24, "SOLID", 417, 17700, 0, 16, True, 3), #This Rocket has the greatest firepower of any single weapon.
    Back_Weapon(0x6E, "WC-CN35", "CHAIN GUN", 32750, 593, 11, "NONE", "SPECIAL", 338, 250, "SOLID", 52, 10000, 1, 2, True, 3), #Fast reloading rifle. Easy to use.
    Back_Weapon(0x6F, "WC-ST120", "SLUG GUN", 56000, 827, 6, "NONE", "SPECIAL", 183, 80, "SOLID", 156, 8100, 1, 22, True, 2), #Fires 7 simultaneous shots that scatter over a wide range.
    Back_Weapon(0x70, "WC-LN350", "LINEAR GUN", 41800, 425, 8, "NONE", "SPECIAL", 690, 120, "SOLID", 108, 9000, 1, 6, True, 3), #Burst-fire type weapon emphasizing firepower over number of shots.
    Back_Weapon(0x71, "WC-GN230", "GRENADE LAUNCHER", 75200, 1230, 8, "NONE", "NARROW & DEEP", 3520, 15, "SOLID", 985, 12000, 1, 32, True, 4), #An AC’s symbolic weapon that mows down enemies in a firestorm.
    Back_Weapon(0x72, "WC-XP4000", "PULSE CANNON", 61000, 318, 364, "NONE", "NARROW & DEEP", 770, 100, "ENERGY", 0, 9000, 1, 5, True, 3), #Energy weapon. Reloading ion cannon.
    Back_Weapon(0x73, "WC-XC8000", "LASER CANNON", 78700, 1110, 455, "NONE", "NARROW & DEEP", 2065, 50, "ENERGY", 0, 8500, 1, 10, True, 4), #Energy weapon. Fires laser rounds.
    Back_Weapon(0x74, "WC-01QL", "PLASMA CANNON", 69500, 273, 618, "NONE", "NARROW & DEEP", 1531, 80, "ENERGY", 0, 12000, 1, 7, True, 4), #Energy weapon. Beam cuts down enemies.
    Back_Weapon(0x75, "RXA-01WE", "RADAR", 12100, 210, 243, "PROVIDED", 8650, "STANDARD"), #Old-style antenna but still holds up well in use.
    Back_Weapon(0x76, "RZ-A0", "RADAR", 17900, 480, 387, "PROVIDED", 11500, "CIRCLE"), #This radar uses 2 dishes for enhanced enemy-search capability.
    Back_Weapon(0x77, "RXA-99", "RADAR", 14500, 160, 267, "PROVIDED", 8800, "STANDARD"), #New-type radar permits even wider area to be searched.
    Back_Weapon(0x78, "RXA-77", "RADAR", 23000, 125, 274, "PROVIDED", 8700, "STANDARD"), #This radar can detect the approach of homing missiles.
    Back_Weapon(0x79, "RZ-A1", "RADAR", 33000, 433, 403, "PROVIDED", 15700, "CIRCLE"),  #Expands the enemy-search range up to the current technological limit.
    Back_Weapon(0x7A, "RZT-333", "RADAR", 27700, 343, 451, "PROVIDED", 11700, "OCTAGON"), #Combines both missile detection and wide-range search capability.
    Back_Weapon(0x7B, "RZ-BBP", "RADAR", 40900, 454, 566, "PROVIDED", 16300, "CIRCLE"), #Highest-quality radar with highest-class performance.
    Back_Weapon(0x7C, "WX-S800/2", "DUAL MISSILE", 69400, 1650, 415, "NONE", "STANDARD", 1120, 60, "SOLID", 515, 11000, 1, 12, False, 3), #Fires 2 missiles with 1 lock-on
    Back_Weapon(0x7D, "WX-S800-GF", "DUAL MISSILE", 90900, 1110, 656, "NONE", "STANDARD", 1120, 60, "SOLID", 515, 11000, 1, 10, False, 3), #Fires 6 missiles with 1 lock-on
    Back_Weapon(0x7E, "XCS-9900", "MULTI MISSILE", 94500, 1480, 310, "NONE", "STANDARD", 980, 20, "SOLID", 1125, 12000, 1, 15, False, 3) #Fires 2 multi-warhead missiles simultaneously.
) 