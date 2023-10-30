import grf
from industry.lib.cargo import ACargo, CargoUnit

the_cargo = ACargo(
    0x18,
    b"FMSP",
    grf.CargoClass.EXPRESS | grf.CargoClass.PIECE_GOODS,
    weight=10,
    units_text=CargoUnit.CRATE,
)
