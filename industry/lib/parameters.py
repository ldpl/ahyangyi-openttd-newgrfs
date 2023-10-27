from agrf.parameters import Parameter, ParameterList, SearchSpace


parameter_list = ParameterList(
    [
        Parameter(
            "ECONOMY",
            0,
            {
                0: "VANILLA_TEMPERATE",
                1: "VANILLA_SUBARCTIC",
                2: "VANILLA_SUBTROPICAL",
                3: "BASIC_TEMPERATE",
                4: "BASIC_ARCTIC",
                # ?: "TOYLAND",
                # ?: "BASIC_SUBTROPICAL",
            },
        ),
        Parameter(
            "PRESET",
            0,
            {
                0: "AEGIS",
                1: "VANILLA",
                2: "FIRS",
                3: "YETI",
                4: "CARIBBEAN",
                5: "LUMBERJACK",
                6: "ITI",
            },
        ),
        Parameter(
            "POLICY",
            0,
            {
                0: "PRESET",
                1: "AUTARKY",
                2: "SELF_SUFFICIENT",
                3: "FREE_TRADE",
                4: "EXPORT",
            },
        ),
        Parameter(
            "PAYMENT",
            0,
            {
                0: "PRESET",
                1: "LINEAR",
                2: "CONSTANT",
            },
        ),
        Parameter(
            "WORKFORCE",
            0,
            {
                0: "PRESET",
                1: "ABSTRACT",
                2: "PROFESSIONAL",
                3: "PROFESSIONAL_PASSENGERS",
                4: "PROFESSIONAL_MAIL",
                5: "PROFESSIONAL_TIRED",
                6: "YETI",
                7: "YETI_PASSENGERS",
                8: "YETI_MAIL",
                9: "YETI_TIRED",
            },
        ),
        Parameter(
            "PRIMARY_INDUSTRY_GROWTH",
            0,
            {
                0: "PRESET",
                1: "NONE",
                2: "GENERIC_SUPPLIES",
                3: "SPECIFIC_SUPPLIES",
                4: "TOWN_POPULATION",
                5: "WORKERS",
                6: "DISCRETE",
                7: "CONTINUOUS",
            },
        ),
        Parameter(
            "PRIMARY_INDUSTRY_CLOSURE",
            0,
            {
                0: "PRESET",
                1: "DISABLED",
                2: "ENABLED",
                3: "RESERVE",
            },
        ),
        Parameter(
            "PRIMARY_INDUSTRY_ZONING",
            0,
            {
                0: "PRESET",
                1: "DISABLED",
                2: "ENABLED",
            },
        ),
        Parameter(
            "SECONDARY_INDUSTRY_PROCESSING",
            0,
            {
                0: "PRESET",
                1: "STRICT",
                2: "NORMAL",
            },
        ),
        Parameter(
            "INDUSTRY_SIZE",
            3,
            {
                0: "ENORMOUS",
                1: "HUGE",
                2: "LARGE",
                3: "REGULAR",
                4: "SMALL",
                5: "TINY",
                6: "ONE_TILE",
                7: "ONE_TILE_FLAT",
            },
        ),
        Parameter(
            "COLOUR_SCHEME",
            0,
            {
                0: "ONE",
                1: "TWO",
                2: "FIRS_3",
                3: "FIRS_4",
                4: "TWO_PER_INDUSTRY",
                5: "ONE_PER_INDUSTRY",
                6: "TWO_GLOBAL",
                7: "ONE_GLOBAL",
                8: "FIXED",
            },
        ),
        Parameter(
            "NIGHT_MODE",
            0,
            {
                0: "AUTO_DETECT",
                1: "ENABLED",
                2: "DISABLED",
            },
        ),
    ]
)


parameter_choices = SearchSpace(
    [
        ("POLICY", ["AUTARKY", "SELF_SUFFICIENT", "FREE_TRADE", "EXPORT"]),
        ("BOOSTER", ["NONE", "UNIVERSAL", "GENERIC", "GENERIC_PASSENGERS"]),
        (
            "WORKFORCE",
            [
                "ABSTRACT",
                "PROFESSIONAL",
                "PROFESSIONAL_PASSENGERS",
                "PROFESSIONAL_MAIL",
                "PROFESSIONAL_TIRED",
                "YETI",
                "YETI_PASSENGERS",
                "YETI_MAIL",
                "YETI_TIRED",
            ],
        ),
        ("LAND_PORTS", ["ORGANIC", "LAND_ONLY", "BOTH", "SEA_ONLY"]),
        ("TOWN_GOODS", ["ORGANIC", "NONE", "SUBARCTIC", "SUBTROPICAL"]),
    ],
    parameter_list,
)


docs_parameter_choices = parameter_choices.copy()
docs_parameter_choices.fix_docs_params("WORKFORCE", ["ABSTRACT", "PROFESSIONAL", "YETI"])
docs_parameter_choices.fix_docs_params("LAND_PORTS", ["ORGANIC"])
docs_parameter_choices.fix_docs_params("TOWN_GOODS", ["ORGANIC"])


PRESETS = {
    "VANILLA": {
        "POLICY": "AUTARKY",
        "BOOSTER": "NONE",
        "WORKFORCE": "ABSTRACT",
        "LAND_PORTS": "ORGANIC",
        "TOWN_GOODS": "ORGANIC",
    },
    "FIRS": {
        "POLICY": "FREE_TRADE",
        "BOOSTER": "GENERIC",
        "WORKFORCE": "ABSTRACT",
        "LAND_PORTS": "ORGANIC",
        "TOWN_GOODS": "ORGANIC",
    },
    "YETI": {
        "POLICY": "AUTARKY",
        "BOOSTER": "UNIVERSAL",
        "WORKFORCE": "YETI",
        "LAND_PORTS": "ORGANIC",
        "TOWN_GOODS": "ORGANIC",
    },
    "CARIBBEAN": {
        "POLICY": "EXPORT",
        "BOOSTER": "GENERIC",
        "WORKFORCE": "ABSTRACT",
        "LAND_PORTS": "ORGANIC",
        "TOWN_GOODS": "ORGANIC",
    },
    "LUMBERJACK": {
        "POLICY": "AUTARKY",
        "BOOSTER": "GENERIC",
        "WORKFORCE": "ABSTRACT",
        "LAND_PORTS": "ORGANIC",
        "TOWN_GOODS": "ORGANIC",
    },
}
