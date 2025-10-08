class Arm_Weapon_L(): #laserblades
    weight: int
    energy_drain: int
    charge_drain: int
    attack_power: int

    def __init__(self, 
                 _id: int, 
                 name: str, 
                 part_type: str, 
                 price: int,
                 weight: int, 
                 energy_drain: int, 
                 charge_drain: int,
                 attack_power: int,
                 tier: int): #1 is Lowest 4 highest.
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.charge_drain = charge_drain
        self.attack_power = attack_power
        self.tier = tier

all_arm_weapon_l = (
    Arm_Weapon_L(0x8F, "LS-2001", "LASERBLADE", 11500, 123, 28, 2050, 738, 1), #Infinitely reusable laser blade.
    Arm_Weapon_L(0x90, "LS-200G", "LASERBLADE", 29000, 181, 45, 1700, 950, 1), #Powerful weapon exclusively for close-in combat.
    Arm_Weapon_L(0x91, "LS-3303", "LASERBLADE", 37200, 224, 43, 2630, 1210, 2), #Enhanced blade weapon. Both power and energy consumption are higher.
    Arm_Weapon_L(0x92, "LS-99-MOONLIGHT", "LASERBLADE", 54000, 336, 93, 810, 2801, 3) #Blade weapon with more than twice the power of conventional blades.
)