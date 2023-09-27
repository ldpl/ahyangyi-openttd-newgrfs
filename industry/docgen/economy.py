import os
from agrf.strings import get_translation


def gen_economy_doc(all_economies, string_manager):
    prefix = "docs/industry/economies"
    for i, economy in enumerate(all_economies):
        for variation in economy.iterate_variations():
            variation_desc = variation.parameter_desc
            if variation_desc == "00":
                header = f"""---
layout: default
title: {economy.name}
parent: Economies
grand_parent: Ahyangyi's Extended Generic Industry Set (AEGIS)
nav_order: {i+1}"""
            else:
                header = f"""---
layout: default
title: {economy.name}
nav_exclude: true"""
            with open(os.path.join(prefix, f"{economy.name}_{variation_desc}.md"), "w") as f:
                print(
                    f"""{header}
---
# Flowchart

| Industry | Accepts | Produces |
|----------|---------|----------|""",
                    file=f,
                )
                translate = lambda x: get_translation(string_manager["STR_CARGO_" + x.decode()], 0x7F)
                link = lambda x: f"[{translate(x.label)}](/openttd-newgrfs/industry/cargos/{x.label.decode()}.html)"
                for industry, flow in variation.graph.items():
                    accepts = ", ".join(link(x) for x in flow.accepts)
                    produces = ", ".join(link(x) for x in flow.produces)
                    print(f"| {industry.name} | {accepts} | {produces} |", file=f)
