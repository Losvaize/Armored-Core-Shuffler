class FCS():
    weight: int
    energy_drain: int
    maximum_lock: int
    lock_type: str

    def __init__(self, _id: int, name: str, part_type: str, price: int,
                 weight: int, energy_drain: int, maximum_lock: int,
                 lock_type: str, tier: int):
        self.id = _id
        self.name = name
        self.part_type = part_type
        self.price = price
        self.weight = weight
        self.energy_drain = energy_drain
        self.maximum_lock = maximum_lock
        self.lock_type = lock_type
        self.tier = tier

all_fcs =(
    FCS(0x44, "COMDEX-C7", "FCS", 11100, 14, 24, 4, "STANDARD", 1), #Maximum of 4 lock-ons, average performance
    FCS(0x45, "COMDEX-G0", "FCS", 22500, 14, 24, 4, "STANDARD", 1), #Maximum of 4 lock-ons, fast lock-on.
    FCS(0x46, "COMDEX-G8", "FCS", 16400, 14, 24, 6, "STANDARD", 1), #Maximum of 6 lock-ons, long-distance lock-on.
    FCS(0x47, "QX-21", "FCS", 20300, 8, 12, 1, "WIDE & SHALLOW", 1), #Maximum of 1 lock-on, short lock over a wide area. 
    FCS(0x48, "QX-AF", "FCS", 35700, 10, 16, 2, "WIDE & SHALLOW", 1), #Maximum of 2 lock-ons, short lock. 
    FCS(0x49, "TRYX-BOXER", "FCS", 48100, 10, 19, 3, "TALL", 3), #Maximum of 3 lock-ons, vertical sight. 
    FCS(0x4A, "TRYX-QUAD", "FCS", 63000, 18, 38, 6, "WIDE", 3), #Maximum of 6 lock-ons, horizontal sight.
    FCS(0x4B, "QX-9009", "FCS", 96000, 24, 55, 6, "NARROW & DEEP", 3) #Maximum of 6 lock-ons, longest lock distance.  
    )