import grf
import struct
from cargos import cargos as cargo_table


class ACargo(grf.SpriteGenerator):
    def __init__(self, id, label, cargo_class, capacity_multiplier=0x100, weight=16, **props):
        self.id = id
        self.label = label
        self.cargo_class = cargo_class
        self.capacity_multiplier = capacity_multiplier
        self.weight = weight
        self._props = {
            "label": struct.unpack("<I", label)[0],
            "classes": cargo_class,
            "capacity_mult": capacity_multiplier,
            "weight": weight,
            **props,
        }
        self.callbacks = grf.make_callback_manager(grf.CARGO, {})

    def get_sprites(self, g):
        res = []
        res.append(
            definition := grf.Define(feature=grf.CARGO, id=self.id, props={**self._props, "bit_number": self.id})
        )
        self.callbacks.graphics = 0
        res.append(self.callbacks.make_map_action(definition))

        return res

    @property
    def translated_id(self):
        return cargo_table.index(self.label)

    def __repr__(self):
        return f"<Cargo:{self.label}>"
