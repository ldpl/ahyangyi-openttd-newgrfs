import os
from industry.lib.parameters import (
    docs_parameter_choices,
    parameter_choices,
    PRESETS,
)


default_variation = "1" * len(parameter_choices.choices)


def gen_economy_doc(all_economies, string_manager):
    prefix = "docs/industry/economies"
    for i, meta_economy in enumerate(all_economies):
        for variation in docs_parameter_choices.iterate_variations():
            economy = meta_economy.get_economy(variation)
            variation_desc = economy.parameter_desc
            if variation_desc == default_variation:
                header = f"""---
layout: default
title: {meta_economy.name(string_manager)}
parent: Economies
grand_parent: Ahyangyi's Extended Generic Industry Set (AEGIS)
nav_order: {i+1}"""
            else:
                header = f"""---
layout: default
title: {meta_economy.name(string_manager)}
nav_exclude: true
search_exclude: true"""

            with open(os.path.join(prefix, f"{meta_economy.translation_name}_{variation_desc}.md"), "w") as f:
                # Flowchart
                print(
                    f"""{header}
---
# Flowchart
{{% mermaid %}}
flowchart LR;""",
                    file=f,
                )
                for industry in economy.industries:
                    print(f"INDUSTRY_{industry.translation_name}[{industry.name(string_manager)}];", file=f)
                for cargo in economy.cargos:
                    print(f"CARGO_{cargo.label.decode()}(({cargo.name(string_manager)}));", file=f)
                for industry, flow in economy.graph.items():
                    for cargo in flow.accepts:
                        print(f"CARGO_{cargo.label.decode()} --> INDUSTRY_{industry.translation_name};", file=f)
                    for cargo in flow.produces:
                        print(f"INDUSTRY_{industry.translation_name} --> CARGO_{cargo.label.decode()};", file=f)

                # Industries
                print(
                    f"""{{% endmermaid %}}

# Industries

| Industry | Accepts | Produces |
|----------|---------|----------|""",
                    file=f,
                )
                industrylink = lambda x: f"[{x.name(string_manager)}](../industries/{x.translation_name}.html)"
                cargolink = lambda x: f"[{x.name(string_manager)}](../cargos/{x.label.decode()}.html)"
                for industry, flow in economy.graph.items():
                    accepts = ", ".join(cargolink(x) for x in flow.accepts)
                    produces = ", ".join(cargolink(x) for x in flow.produces)
                    print(f"| {industrylink(industry)} | {accepts} | {produces} |", file=f)

                # Cargos
                print(
                    """
# Cargos

| Cargo | Class | Capacity Multiplier | Weight |
|-------|-------|---------------------|--------|""",
                    file=f,
                )
                for cargo in economy.cargos:
                    from .cargo import cargo_class

                    cargolink = lambda x: f"[{x.name(string_manager)}](../cargos/{x.label.decode()}.html)"

                    print(
                        f"| {cargolink(cargo)} | {cargo_class(cargo.cargo_class)} | {cargo.capacity_multiplier / 0x100} | {cargo.weight / 16} |",
                        file=f,
                    )

                # Links: presets & variations
                print(
                    """
# Presets
""",
                    file=f,
                )

                choices_text = []
                for preset, preset_params in PRESETS.items():
                    preset_desc = parameter_choices.desc(preset_params)
                    if preset_desc == variation_desc:
                        choices_text.append(f"{preset}")
                    else:
                        choices_text.append(f"[{preset}]({meta_economy.translation_name}_{preset_desc}.html)")
                choices_text = " \\| ".join(choices_text)
                print(
                    f"""{choices_text}

# Variations""",
                    file=f,
                )

                for i, (param, choices) in enumerate(docs_parameter_choices.choices):
                    if len(choices) == 1:
                        continue
                    choices_text = []
                    for choice in choices:
                        if variation[param] == choice:
                            choices_text.append(f"{choice}")
                        else:
                            choices_text.append(
                                f"[{choice}]({meta_economy.translation_name}_{parameter_choices.desc({**variation, param: choice})}.html)"
                            )
                    print(
                        f"{param}: " + " \\| ".join(choices_text) + "\n",
                        file=f,
                    )
