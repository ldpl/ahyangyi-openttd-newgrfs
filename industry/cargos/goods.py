import grf
from industry.lib.cargo import ACargo

the_cargo = ACargo(b"GOOD", grf.CargoClass.EXPRESS, capacity_multiplier=0x200, weight=8)
