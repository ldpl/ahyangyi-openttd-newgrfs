import grf
import struct
from industry.lib.parameters import parameter_list
from agrf.lib.cargo import Cargo
from cargos import cargos as cargo_table
from agrf.strings import get_translation
from agrf.split_action import SplitDefinition, MetaSpriteMixin


class CargoUnit:
    PASSENGER = 0x4F
    TONNE = 0x50
    BAG = 0x51
    LITRE = 0x52
    ITEM = 0x53
    CRATE = 0x54


# FIXME: merge with the other props_hash
def props_hash(parameters):
    ret = []
    for k, v in sorted(parameters.items()):
        ret.append((k, v))
    return hash(tuple(ret))


class ACargo(Cargo, MetaSpriteMixin):
    def __init__(self, id, label, cargo_class, capacity_multiplier=0x100, weight=16, **props):
        super().__init__(
            id=id, **{"classes": cargo_class, "capacity_mult": capacity_multiplier, "weight": weight, **props}
        )
        MetaSpriteMixin.__init__(self, grf.CARGO, props_hash, parameter_list)
        self.label = label
        self.cargo_class = cargo_class

    def postprocess_props(self, props):
        return ACargo.translate_strings(props, self._g)

    def get_definitions(self, g):
        res, _ = self.dynamic_definitions(self.dynamic_prop_variables, {}, 0)
        return [sprite for sprite_group in res for sprite in sprite_group]

    def get_sprites(self, g):
        s = g.strings
        self._props["type_text"] = s[f"STR_CARGO_NAME_{self.label.decode()}"]
        self._props["unit_text"] = s[f"STR_CARGO_NAME_{self.label.decode()}"]
        self._props["one_text"] = s[f"STR_CARGO_UNIT_{self.label.decode()}"]
        self._props["many_text"] = s[f"STR_CARGO_UNIT_{self.label.decode()}"]
        self._props["abbr_text"] = s[f"STR_CARGO_NAME_{self.label.decode()}"]
        self._props["bit_number"] = self.id
        self._props["label"] = struct.unpack("<I", self.label)[0]
        self._g = g  # FIXME?
        return super().get_sprites(g)

    @property
    def capacity_multiplier(self):
        return self._props["capacity_mult"]

    @property
    def weight(self):
        return self._props["weight"]

    @property
    def translated_id(self):
        return cargo_table.index(self.label)

    def __repr__(self):
        return f"<Cargo:{self.label}>"

    def name(self, string_manager, lang_id=0x7F):
        return get_translation(string_manager[f"STR_CARGO_NAME_{self.label.decode()}"], 0x7F)

    @property
    def penalty1(self):
        return self._props["penalty1"]

    @property
    def penalty2(self):
        return self._props["penalty2"]

    @property
    def base_price(self):
        return self._props["base_price"]
