import grf
from industry.lib.cargo import ACargo

the_cargo = ACargo(0x1A, b"FISH", grf.CargoClass.BULK | grf.CargoClass.PIECE_GOODS)
