def make_tuple(x):
    if isinstance(x, tuple):
        return x
    return (x,)


def optional_to_tuple(x):
    if x is None:
        return ()
    return (x,)


class PrimaryIndustry:
    def __init__(self, produces=(), extra_accepts=(), booster=None):
        self.produces = make_tuple(produces)
        self.extra_accepts = make_tuple(extra_accepts)
        self.booster = booster

    def copy(self):
        return PrimaryIndustry(self.produces, self.extra_accepts, self.booster)

    @property
    def accepts(self):
        return self.extra_accepts + optional_to_tuple(self.booster)

    @property
    def consumes(self):
        return ()


class SecondaryIndustry:
    def __init__(self, consumes=(), produces=()):
        self.consumes = make_tuple(consumes)
        self.produces = make_tuple(produces)

    def copy(self):
        return SecondaryIndustry(self.consumes, self.produces)

    @property
    def accepts(self):
        return self.consumes


class TertiaryIndustry:
    def __init__(self, consumes=()):
        self.consumes = make_tuple(consumes)

    def copy(self):
        return TertiaryIndustry(self.consumes)

    @property
    def accepts(self):
        return self.consumes

    @property
    def produces(self):
        return ()


class Town:
    def __init__(self, passengers, mail, food, goods):
        self.passengers = passengers
        self.mail = mail
        self.food = food
        self.goods = goods

    def copy(self):
        return Town(self.passengers, self.mail, self.food, self.goods)

    @property
    def accepts(self):
        return tuple(y for x in (self.passengers, self.mail, self.food, self.goods) for y in optional_to_tuple(x))

    @property
    def consumes(self):
        return ()

    @property
    def produces(self):
        return tuple(y for x in (self.passengers, self.mail) for y in optional_to_tuple(x))


_supported_options = [
    ("policy", ["autarky"]),
    ("booster", ["none", "generic"]),
]


class Economy:
    def __init__(self, name, graph, parameters={}):
        self.name = name
        self.graph = graph
        self.parameters = parameters

    def copy(self):
        return Economy(self.name, {k: v.copy() for k, v in self.graph.items()}, self.parameters.copy())

    @property
    def industries(self):
        return list(self.graph.keys())

    @property
    def cargos(self):
        return list(set(y for x in self.graph.values() for y in x.accepts + x.produces))

    @property
    def parameter_desc(self):
        return "".join(str(_supported_options[i].index(self.parameters[i])) for i in range(len(_supported_options)))

    def iterate_variations(self, i=0):
        if i == len(_supported_options):
            yield self
        else:
            for j in _supported_options[i]:
                copy = self.copy()
                copy.parameters[i] = j
                getattr(copy, f"set_{_supported_options[i]}", lambda x: None)(j)
                for variation in copy.iterate_variations(i + 1):
                    yield variation

    def get_variations(self):
        return list(self.iterate_variations)
