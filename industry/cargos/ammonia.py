import grf
from industry.lib.cargo import ACargo, CargoUnit

the_cargo = ACargo(
    0x10,
    b"NH3_",
    grf.CargoClass.LIQUID | grf.CargoClass.HAZARDOUS,
    weight=10,
    units_text=CargoUnit.LITRE,
)
