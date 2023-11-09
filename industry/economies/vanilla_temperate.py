from industry.lib.economy import (
    Economy,
    PrimaryIndustry,
    WorkerYard,
    FreePort,
    SecondaryIndustry,
    TertiaryIndustry,
    Town,
)
from industry.cargos import (
    coal,
    engineering_supplies,
    farm_supplies,
    food,
    goods,
    grain,
    iron_ore,
    livestock,
    mail,
    oil,
    passengers,
    steel,
    tired_workers,
    valuables,
    water,
    wood,
    workers,
)
from industry.industries import (
    bank,
    coal_mine,
    factory,
    farm,
    food_processing_plant,
    forest,
    iron_ore_mine,
    oil_refinery,
    oil_rig,
    oil_wells,
    port,
    power_station,
    sawmill,
    steel_mill,
    towns,
    water_supply,
    water_tower,
    worker_yard,
)


class TheEconomy:
    def __init__(self):
        self.name = "Vanilla Temperate"

    def get_economy(self, parameters):
        ret = Economy(
            {
                coal_mine: PrimaryIndustry(coal),
                bank: PrimaryIndustry(valuables, valuables),
                farm: PrimaryIndustry((grain, livestock)),
                forest: PrimaryIndustry(wood),
                iron_ore_mine: PrimaryIndustry(iron_ore),
                oil_rig: PrimaryIndustry(oil),
                oil_wells: PrimaryIndustry(oil),
                factory: SecondaryIndustry((grain, livestock, steel), goods),
                oil_refinery: SecondaryIndustry(oil, goods),
                sawmill: SecondaryIndustry(wood, goods),
                steel_mill: SecondaryIndustry(iron_ore, steel),
                power_station: TertiaryIndustry(coal),
                towns: Town(passengers, mail, None, goods),
            },
            parameters,
        )
        if parameters["POLICY"] == "SELF_SUFFICIENT":
            ret.graph[port] = FreePort(wood, valuables)
        elif parameters["POLICY"] in ("FREE_TRADE", "EXPORT"):
            ret.graph[port] = FreePort(wood, valuables)
            ret.graph[bank] = TertiaryIndustry(valuables)

        if parameters["PRIMARY_INDUSTRY_GROWTH"] == "UNIVERSAL_SUPPLIES":
            ret.graph[coal_mine].boosters = engineering_supplies
            ret.graph[oil_wells].boosters = engineering_supplies
            ret.graph[oil_rig].boosters = engineering_supplies
            ret.graph[iron_ore_mine].boosters = engineering_supplies
            ret.graph[farm].boosters = engineering_supplies
            ret.graph[forest].boosters = engineering_supplies

            ret.graph[factory].produces += (engineering_supplies,)
        elif parameters["PRIMARY_INDUSTRY_GROWTH"] == "GENERIC_SUPPLIES":
            ret.graph[coal_mine].boosters = engineering_supplies
            ret.graph[oil_wells].boosters = engineering_supplies
            ret.graph[oil_rig].boosters = engineering_supplies
            ret.graph[iron_ore_mine].boosters = engineering_supplies
            ret.graph[farm].boosters = farm_supplies
            ret.graph[forest].boosters = farm_supplies

            ret.graph[factory].produces += (engineering_supplies,)
            ret.graph[oil_refinery].produces += (farm_supplies,)

        if parameters["WORKFORCE"].startswith("YETI"):
            if parameters["WORKFORCE"] == "YETI":
                ret.graph[worker_yard] = WorkerYard(workers, boosters=(goods, valuables))
            elif parameters["WORKFORCE"] == "YETI_PASSENGERS":
                ret.graph[worker_yard] = WorkerYard(workers, boosters=(goods, valuables, passengers))
            elif parameters["WORKFORCE"] == "YETI_MAIL":
                ret.graph[worker_yard] = WorkerYard(workers, boosters=(goods, valuables, mail))
            elif parameters["WORKFORCE"] == "YETI_TIRED":
                ret.graph[worker_yard] = WorkerYard(workers, boosters=(goods, valuables, tired_workers))
                ret.graph[coal_mine].produces += (tired_workers,)
            # FIXME
            ret.graph[coal_mine].boosters = workers

        if parameters["TOWN_GOODS"] in ("FOOD", "FOOD_AND_WATER"):
            ret.graph[food_processing_plant] = SecondaryIndustry(
                (
                    livestock,
                    grain,
                ),
                food,
            )
            ret.graph[factory].consumes = tuple(x for x in ret.graph[factory].consumes if x not in [livestock, grain])
            ret.graph[towns].food = food
        if parameters["TOWN_GOODS"] == "FOOD_AND_WATER":
            ret.graph[water_supply] = PrimaryIndustry(water)
            ret.graph[water_tower] = TertiaryIndustry(water)

        return ret
