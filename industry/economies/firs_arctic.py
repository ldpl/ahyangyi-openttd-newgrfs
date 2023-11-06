from industry.lib.economy import Economy, PrimaryIndustry, WorkerYard, SecondaryIndustry, TertiaryIndustry, Town
from industry.cargos import (
    ammonia,
    china_clay,
    engineering_supplies,
    explosives,
    farm_supplies,
    fertiliser,
    fish,
    food,
    mail,
    paper,
    passengers,
    peat,
    phosphate,
    potash,
    pyrite_ore,
    sulphur,
    timber,
    tired_workers,
    water,
    wood,
    workers,
    zinc,
)
from industry.industries import (
    ammonia_plant,
    chemical_plant,
    clay_pit,
    fish_farm,
    fishing_grounds,
    fishing_harbor,
    forest,
    general_store,
    herding_coop,
    paper_mill,
    peatlands,
    phosphate_mine,
    port,
    potash_mine,
    power_station,
    pyrite_mine,
    pyrite_smelter,
    sawmill,
    towns,
    trading_centre,
    water_supply,
    water_tower,
    wharf,
    worker_yard,
)


class TheEconomy:
    def __init__(self):
        self.name = "FIRS Arctic"

    def get_economy(self, parameters):
        ret = Economy(
            {
                ammonia_plant: PrimaryIndustry(ammonia),
                clay_pit: PrimaryIndustry(china_clay),
                peatlands: PrimaryIndustry(peat),
                phosphate_mine: PrimaryIndustry(phosphate),
                potash_mine: PrimaryIndustry(potash),
                pyrite_mine: PrimaryIndustry(pyrite_ore),
                fish_farm: PrimaryIndustry(fish),
                fishing_grounds: PrimaryIndustry(fish),
                forest: PrimaryIndustry(wood),
                herding_coop: PrimaryIndustry(food),
                pyrite_smelter: SecondaryIndustry(pyrite_ore, (sulphur, zinc)),
                sawmill: SecondaryIndustry(wood, timber),
                chemical_plant: SecondaryIndustry(
                    (phosphate, sulphur, ammonia, potash),
                    (explosives, fertiliser),
                ),
                fishing_harbor: SecondaryIndustry(fish, food),
                paper_mill: SecondaryIndustry((wood, sulphur, china_clay), paper),
                power_station: TertiaryIndustry(peat),
                general_store: TertiaryIndustry((explosives, fertiliser, zinc, timber)),
                towns: Town(passengers, mail, food, paper),
            },
            parameters,
        )
        if parameters["POLICY"] == "SELF_SUFFICIENT":
            ret.graph[port] = SecondaryIndustry(timber, china_clay)
            ret.graph[wharf] = SecondaryIndustry(timber, ammonia)
        elif parameters["POLICY"] in ("FREE_TRADE", "EXPORT"):
            ret.graph[port] = SecondaryIndustry(timber, china_clay)
            ret.graph[wharf] = SecondaryIndustry(timber, ammonia)
            del ret.graph[ammonia_plant]
            del ret.graph[clay_pit]

        if parameters["BOOSTER"] == "UNIVERSAL":
            if ammonia_plant in ret.graph:
                ret.graph[ammonia_plant].boosters = engineering_supplies
            if clay_pit in ret.graph:
                ret.graph[clay_pit].boosters = engineering_supplies
            ret.graph[peatlands].boosters = engineering_supplies
            ret.graph[phosphate_mine].boosters = engineering_supplies
            ret.graph[potash_mine].boosters = engineering_supplies
            ret.graph[pyrite_mine].boosters = engineering_supplies

            ret.graph[fish_farm].boosters = engineering_supplies
            ret.graph[forest].boosters = engineering_supplies
            ret.graph[herding_coop].boosters = engineering_supplies

            ret.graph[paper_mill].produces += (engineering_supplies,)
        elif parameters["BOOSTER"] == "GENERIC":
            if ammonia_plant in ret.graph:
                ret.graph[ammonia_plant].boosters = engineering_supplies
            if clay_pit in ret.graph:
                ret.graph[clay_pit].boosters = engineering_supplies
            ret.graph[peatlands].boosters = engineering_supplies
            ret.graph[phosphate_mine].boosters = engineering_supplies
            ret.graph[potash_mine].boosters = engineering_supplies
            ret.graph[pyrite_mine].boosters = engineering_supplies

            ret.graph[fish_farm].boosters = farm_supplies
            ret.graph[forest].boosters = farm_supplies
            ret.graph[herding_coop].boosters = farm_supplies

            ret.graph[paper_mill].produces += (engineering_supplies,)
            ret.graph[chemical_plant].produces += (farm_supplies,)
        elif parameters["BOOSTER"] == "GENERIC_PASSENGERS":
            if ammonia_plant in ret.graph:
                ret.graph[ammonia_plant].boosters = engineering_supplies
            if clay_pit in ret.graph:
                ret.graph[clay_pit].boosters = engineering_supplies
            ret.graph[peatlands].boosters = engineering_supplies
            ret.graph[phosphate_mine].boosters = engineering_supplies
            ret.graph[potash_mine].boosters = engineering_supplies
            ret.graph[pyrite_mine].boosters = engineering_supplies

            ret.graph[fish_farm].boosters = farm_supplies
            ret.graph[forest].boosters = farm_supplies
            ret.graph[herding_coop].boosters = farm_supplies

            ret.graph[paper_mill].produces += (engineering_supplies,)
            ret.graph[chemical_plant].produces += (farm_supplies,)

        if parameters["WORKFORCE"].startswith("YETI"):
            if parameters["WORKFORCE"] == "YETI":
                ret.graph[worker_yard] = WorkerYard(workers, boosters=(paper, zinc))
            elif parameters["WORKFORCE"] == "YETI_PASSENGERS":
                ret.graph[worker_yard] = WorkerYard(workers, boosters=(paper, zinc, passengers))
            elif parameters["WORKFORCE"] == "YETI_MAIL":
                ret.graph[worker_yard] = WorkerYard(workers, boosters=(paper, zinc, mail))
            elif parameters["WORKFORCE"] == "YETI_TIRED":
                ret.graph[worker_yard] = WorkerYard(workers, boosters=(paper, zinc, tired_workers))
                ret.graph[peatlands].produces += (tired_workers,)

            # FIXME
            ret.graph[peatlands].boosters = workers

        if port in ret.graph:
            if parameters["SEA_INDUSTRY"] == "LAND_ONLY":
                ret.graph[trading_centre] = ret.graph[port]
                del ret.graph[port]
            elif parameters["SEA_INDUSTRY"] == "BOTH":
                ret.graph[trading_centre] = ret.graph[port]

        if parameters["TOWN_GOODS"] == "SUBTROPICAL":
            ret.graph[water_supply] = PrimaryIndustry(water)
            ret.graph[water_tower] = TertiaryIndustry(water)

        return ret
