#!/usr/bin/env python
import grf

g = grf.NewGRF(
    grfid=b"\xE5\xBC\x8Br",
    name="Ahyangyi's Dovemere Road Set",
    description="China-inspired road set.",
    id_map_file="road/id_map.json",
    sprite_cache_path="road/.cache",
)

g.write("road.grf")
