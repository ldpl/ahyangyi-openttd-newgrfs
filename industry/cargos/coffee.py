import grf
from industry.lib.cargo import ACargo, CargoUnit

the_cargo = ACargo(
    0x14,
    b"JAVA",
    grf.CargoClass.EXPRESS | grf.CargoClass.PIECE_GOODS,
    units_text=CargoUnit.BAG,
    is_freight=1,
    penalty1=0,
    penalty2=26,
    base_price=173,
)
