from agrf.parameters import Parameter, ParameterList, SearchSpace


parameter_list = ParameterList(
    [
        Parameter(
            "VANILLA_RV",
            0,
            {
                0: "DISABLED",
                1: "ENABLED",
            },
        ),
        Parameter("NIGHT_MODE", 0, {0: "AUTO_DETECT", 1: "ENABLED", 2: "DISABLED"}),
        # FIXME: change the order after migrating the code
        Parameter(
            "ROSTER",
            0,
            {
                0: "ALL",
                1: "DOVEMERE",
                2: "NORBURY",
            },
        ),
        Parameter(
            "EARLY_IMPORTED_VEHICLES",
            2,
            {
                0: "DISABLED",
                1: "ENABLED_CHEAP",
                2: "ENABLED",
                3: "ENABLED_COSTLY",
            },
        ),
        Parameter(
            "FANTASY_FREIGHT_TRAMS",
            0,
            {
                0: "DISABLED",
                1: "ENABLED",
            },
        ),
    ]
)
