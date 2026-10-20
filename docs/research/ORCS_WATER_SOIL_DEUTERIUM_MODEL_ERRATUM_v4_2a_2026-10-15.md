# ORCS v4.2a — Water/soil brine white paper numerical erratum

**2026-10-15 | Additive version-correction, ZERO realized credit | prior v4.2 remains intact**

The v4.2 model prototype `prototypes/orcs-water-soil-network-v4_2/national_network.py` contained a self-check for naturally occurring deuterium mass in a nominal 100MGD pure water throughput: `~4780 t/y ±25`. Its defined hydrogen isotope **atomic** abundance 0.000156 and isotope atomic masses actually produce **~4,820 metric tonnes of deuterium content/year**, ~34.88 ppm of water mass. The published assertion would FAIL despite correct formula due to rounding to wrong expected baseline. This is not a recovered product.

The corrected **new** script is `prototypes/orcs-water-soil-network-v4_2a/national_network.py`, with self-check centered 4,820t/y ±10t. Expected Harbor Island feed at 291.2MGD ~**14,035t elemental D-content/year**, and national 34BGD gross wastewater flow ~**1.64Mt elemental D-content/year**. Rounded old whitepaper numbers (~4,780, ~13,900, ~1.63Mt) differ <1%, so executive/economic conclusions unchanged: 0 commercial recovered, isotope separation costs and buyers unknown, do not multiply lab prices by natural isotope inventory.

The v4.2 document remains the original citation bundle, and v4.2a corrects the model acceptance threshold. No claim of programmatic test running or isotope extraction success.