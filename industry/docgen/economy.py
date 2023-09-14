import os
from agrf.strings import get_translation


def gen_economy_doc(all_economies, string_manager):
    prefix = "docs/industry/economies"
    for i, entry in enumerate(all_economies):
        v = entry.the_economy
        with open(os.path.join(prefix, f"{v.name}.md"), "w") as f:
            print(
                f"""---
layout: default
title: {v.name}
parent: Economies
grand_parent: Ahyangyi's Extended Generic Industry Set (AEGIS)
nav_order: {i+1}
---
# Flowchart

| Industry | Accepts | Produces |
|----------|---------|----------|""",
                file=f,
            )
            for industry, (i, o) in v.graph.items():
                translate = lambda x: get_translation(string_manager["STR_CARGO_" + x], 0x7F)
                accepts = ", ".join(translate(x.label) for x in i)
                produces = ", ".join(translate(x.label) for x in o)
                print(f"| {industry.name} | {accepts} | {produces} |", file=f)
