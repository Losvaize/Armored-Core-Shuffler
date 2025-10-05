class Legs():
    weight: int
    energy_drain: int
    armor_point: int
    def_shell: int
    def_energy: int
    max_weight: int
    speed: int
    stability: int
    jump_function: str

    def __init__ (self,
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
                  speed: int,
                  stability: int, 
                  jump_function: str,
                  tier: int):
        
        self.id = id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.armor_point = armor_point
        self.def_shell = def_shell
        self.def_energy = def_energy
        self.max_weight = max_weight
        self.speed = speed
        self.stability = stability
        self.jump_function = jump_function
        self.tier = tier # Tier 1 lowest. Tier 4 Highest

all_legs = (
    Legs(0x1D, "LN-1001", "HUMANOID LEGS", 28500, 1966, 1725, 3235, 556, 531, 4470, 277, 1018, "PROVIDED"), #Balanced, standard humanoid legs.
	Legs(0x1E, "LN-SSVT", "HUMANOID LEGS", 44000, 1528, 2338, 2795, 482, 507, 3560, 445, 596, "PROVIDED"), #Light, fast humanoid legs but with low load capacity and AP.
	Legs(0x1F, "LN-3001", "HUMANOID LEGS", 52200, 3137, 2206, 3703, 870, 594, 6600, 153, 2518, "PROVIDED"), #Heavily armored humanoid legs with high load capacity. Poor speed. 
	Legs(0x20, "LN-1001-PX-0", "HUMANOID LEGS", 25000, 1892, 1844, 3035, 528, 508, 4100, 280, 904, "PROVIDED"), #Balanced humanoid legs for combat on all terrain.
	Legs(0x21, "LN-501", "HUMANOID LEGS", 71800, 1675, 2910, 2947, 508, 535, 3990, 451, 854, "PROVIDED"), #Has the shield performance and load capacity of a middleweight.
	Legs(0x22, "LN-SSVR", "HUMANOID LEGS", 32400, 2750, 2013, 3606, 805, 532, 5400, 148, 2150, "PROVIDED"), #Lightest of the heavily armored humanoid legs.
	Legs(0x23, "LN-1001B", "HUMANOID LEGS", 45200, 2305, 1889, 3383, 585, 543, 4630, 272, 1320, "PROVIDED"), #Enhanced variation of the LN-1001.
	Legs(0x24, "DUMMY", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
	Legs(0x25, "LN-3001C", "HUMANOID LEGS", 64100, 3528, 2418, 3977, 889, 602, 7100, 151, 2977, "PROVIDED"), #Best AP and shields among the humanoid legs.
	Legs(0x26, "DUMMY", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
	Legs(0x27, "LN-502", "HUMANOID LEGS", 35800, 1790, 2466, 3343, 538, 592, 3800, 275, 843, "PROVIDED"), #This middleweight has reduced weight without sacrificing performance.
	Legs(0x28, "LN-D-8000R", "HUMANOID LEGS", 49000, 2426, 2350, 3532, 510, 656, 4720, 269, 1200, "PROVIDED"), #Humanoid legs with special anti-energy weapon armor.
	Legs(0x29, "DUMMY", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
	Legs(0x2A, "LNKS-1B46J", "HUMANOID LEGS", 48000, 3065, 2304, 3788, 822, 618, 6100, 146, 3802, "PROVIDED"), #Shock absorbing structure reduces recoil from shell hits.
	Legs(0x2B, "LB-4400", "REVERSE JOINT", 17300, 2520, 1400, 3560, 617, 451, 4020, 294, 2084, "PROVIDED"), #Standard reverse joint type. Good maneuverability and inexpensive. 
	Legs(0x2C, "DUMMY", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
	Legs(0x2D, "LB-4401", "REVERSE JOINT", 31800, 2910, 1456, 3810, 672, 468, 4510, 287, 2713, "PROVIDED"), #Best overall performance of the reverse joint types.
	Legs(0x2E, "LB-4303", "REVERSE JOINT", 24000, 2647, 1585, 3575, 643, 488, 4180, 291, 2505, "PROVIDED"), #Increased ground contact area for enhanced shock absorbing capacity.
	Legs(0x2F, "LB-1000-P", "REVERSE JOINT", 20500, 2095, 1228, 3514, 609, 444, 3775, 286, 2310, "PROVIDED"), #Phenomenal maneuverability but low load carrying capacity.
	Legs(0x30, "LBKS-2B45A", "REVERSE JOINT", 27000, 2480, 1703, 3731, 584, 515, 3990, 299, 1985, "PROVIDED"), #Deluxe type with enhanced shielding against energy weapons.
	Legs(0x31, "DUMMY", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
	Legs(0x32, "LF-205-SF", "FOUR LEGS TYPE", 42600, 2137, 2810, 2841, 446, 654, 3450, 483, 580, "PROVIDED"), #Standard four-leg type. Top-class maneuverability. 
	Legs(0x33, "LFH-X3", "FOUR LEGS TYPE", 56000, 2400, 2988, 3100, 468, 610, 3810, 421, 710, "PROVIDED"), #Energy gauge recovers quickly when halted.
	Legs(0x34, "LF-DEX-1", "FOUR LEGS TYPE", 69000, 2650, 4016, 3179, 557, 553, 4450, 360, 820, "PROVIDED"), #Increased load carrying capacity requires vast amounts of power.
	Legs(0x35, "DUMMY", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
	Legs(0x36, "DUMMY", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
	Legs(0x37, "LFH-X5X", "FOUR LEGS TYPE", 82000, 2880, 3584, 3328, 497, 700, 5000, 442, 1110, "PROVIDED"), #New four-leg type pushes the specs to the limit.
	Legs(0x38, "LC-MOS18", "CATERPILLAR", 16000, 4182, 978, 3928, 858, 572, 8000, 105, 4245, "NONE"), #Maximum load carrying capacity but poor speed and weight. 
	Legs(0x39, "LC-UKI60", "CATERPILLAT", 25500, 3860, 1104, 3822, 812, 589, 6950, 138, 3710, "NONE"), #Economy wheeled truck type with finely adjusted performance. 
	Legs(0x3A, "DUMMY", "DUMMY PARTS", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NONE"), #
	Legs(0x3B, "LC-HTP-AAA", "CATERPILLAR", 38500, 2915, 2877, 3688, 728, 694, 4130, 250, 630, "NONE"), #Has performance near that of a four-legged type.
	Legs(0x3C, "LC-MOS4545", "CATERPILLAR", 59000, 3610, 2609, 3990, 905, 753, 7400, 211, 5101, "NONE"), #A dreadfully durable monster machine.
	)  

