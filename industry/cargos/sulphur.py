import grf
from industry.lib.cargo import ACargo, CargoUnit

the_cargo = ACargo(
    0x2D,
    b"SULP",
    grf.CargoClass.BULK | grf.CargoClass.LIQUID | grf.CargoClass.COVERED,
    units_text=CargoUnit.TONNE,
    is_freight=1,
    penalty1=30,
    penalty2=255,
    base_price=105,
)
