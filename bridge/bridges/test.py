from bridge.lib import ABridge
from datetime import date
import grf

from agrf.graphics.voxel import LazyVoxel, LazySpriteSheet

vox = LazyVoxel(
    "dovemere_yangtze_1",
    prefix=f"bridge/voxels/render/dovemere_yangtze_1",
    voxel_getter=lambda: f"bridge/voxels/dovemere_yangtze_1.vox",
    load_from="bridge/files/gorender.json",
)
vox.render()
voxels = [LazySpriteSheet([vox], [(0, 0)])]

the_bridge = ABridge(
    id=0x01,
    name="Test Bridge",
    front=None,
    back=None,
    pillar=None,
    intro_year_since_1920=0,
    purchase_text="Build Test Bridge",
    description_rail="Test Bridge (rail)",
    description_road="Test Bridge (road)",
)
