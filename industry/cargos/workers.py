import grf
from industry.lib.cargo import ACargo

the_cargo = ACargo(0x33, b"OTI1", grf.CargoClass.PASSENGERS, capacity_multiplier=0x400, weight=1)
