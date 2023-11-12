import grf
from industry.lib.cargo import ACargo, CargoUnit

the_cargo = ACargo(
    0x0A,
    b"GOLD",
    grf.CargoClass.ARMOURED,
    weight=8,
    units_text=CargoUnit.BAG,
    is_freight=1,
    penalty1=30,
    penalty2=255,
    base_price=152,
)
