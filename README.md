[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/c/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/DinishKawaii/news-image-20261125/rank.svg)](https://make.fun/c/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/DinishKawaii/news-image-20261125/reward.svg)](https://make.fun/c/news-image-20261125)

# The World Today — Wednesday 25 November 2026

One image that sums up the world's news of Wednesday 25 November 2026:
a dense 1024x1024 newspaper page with 35 stories across 6 continents
plus space — three big illustrated stories, a UTC timeline of the
morning as reported, a world map with numbered pins, a numbers column,
and a numbered list of stories 4–35.

## The three big stories

1. **Pakistan's first astronaut reaches Tiangong** — China's Shenzhou-24
   launched at 00:18 UTC from Jiuquan and docked at 03:56 UTC.
   Muhammad Zeeshan Ali is the first Pakistani in orbit and the first
   foreigner aboard the Tiangong space station. (Reuters, Xinhua, BBC)
2. **Six tankers hit by mines in the Strait** — Tehran says six tankers
   hit mines in 24 hours; the claim is unconfirmed. The US naval
   blockade holds and Brent trades near $91. (Reuters, Al Jazeera)
3. **US set to unveil new tariffs** — findings of the Section 301 probe
   into alleged excess industrial capacity in 16 trading partners,
   including China and the EU, are due; Asian stocks slid on the news.
   (Reuters)

## The morning as reported (BBC World, UTC)

00:18 Shenzhou-24 lifts off — 00:56 Russia's own figures show ~500,000
war deaths — 01:40 Thomas Markle indicted in the US — 02:59 Huawei
found guilty of stealing trade secrets — 03:44 US attorney general
dodges questions about the Nvidia investigation — 04:49 Kilmar Abrego
Garcia leaves the US for Spain — 07:04 Real Madrid 5-1 PSV (UCL wrap).

## Stories 4–35

4. Putin vows revenge for Ukraine refinery strikes
5. Kyiv claims Baltic cargo-ship drone strike
6. Ukraine: sea drones sank Russian corvette off Libya
7. Magyar meets Zelensky, first Hungary PM visit since 2015
8. Norway pledges at least $7bn to Ukraine in 2027
9. Russian strike on Zaporizhzhia flats: 2 dead, 40+ hurt
10. Gaza: Israeli strike kills Hamas security chief
11. Gaza death toll reaches 74,746; 9 killed in a day
12. Houthis hit Riyadh PIF tower; 11 people injured
13. Houthis threaten Jeddah, Saudi Red Sea ports
14. Saudi-led coalition orders civilians out of Hodeidah
15. WHO pulls staff from DR Congo hospital in Ebola zone
16. DR Congo plane missing; rebels claim shoot-down
17. Sahel rebels turn cheap FPV drones on Mali army
18. China probes Politburo member Chen Jining
19. Russia sends home Chinese suspect in $2.3bn case
20. Australia inflation 3.8%; rate pressure grows
21. Asia stocks slide: Seoul -5.3%, Taipei -5.1%
22. Bitcoin $59,258; ether $1,661 as crypto slips
23. US core PCE data due before Thanksgiving
24. Nvidia shares fall ~7% as Huang returns as CEO
25. COP31 fallout: focus shifts to COP32 in Addis Ababa
26. Myanmar tops world landmine toll: 1,891 hurt in 2025
27. 30 miners trapped in flooded Bogor gold mine
28. Cikande candy-factory fire toll rises to 26
29. Real Madrid 5-1 PSV; Arsenal 1-1 Dortmund
30. Senegal reinstated as 2025 Africa Cup winners
31. Sarkozy and Carla Bruni ordered to face trial
32. Eisenkot seals first coalition pact in Israel
33. Solomon Islands swaps China pact for Australia
34. NATO chief vows defence vs space threat
35. Trump pardons turkeys Freedom and Feathers

## The day in numbers

500,000 Russian war deaths (Moscow's own figures) — 74,746 Gaza death
toll — 30 miners trapped in Bogor — 11 hurt in the Riyadh tower strike
— 5-1 Real Madrid beat PSV — ~$91 Brent crude a barrel.

Map pins: 1 Jiuquan, 2 Hormuz, 3 Riyadh, 4 Gaza, 5 Kyiv, 6 Washington,
7 Bogor, 8 Ituri (DR Congo).

## Date check

COP31 ended on 22 November, so only its 25 November fallout is counted
here. Miley Cyrus married on 21 November, not today. The Champions
League scores are from Tuesday night, first reported Wednesday 25
November UTC. Iran's claim that six tankers hit mines is reported as a
claim, not confirmed.

Sources: Reuters, BBC, Xinhua, UEFA, Carbon Brief, Kyiv Independent,
Al Jazeera.

## How it works

`main.py` copies the `entry.png` beside it to `$MAKEFUN_OUTPUT_DIR/entry.png`
(or `/output/entry.png`). It uses only the Python 3.13 standard library —
no network, no dependencies — and checks the copy: same bytes as the source,
a real 1024x1024 PNG, within the 1 MiB limit. The image itself was drawn
for this entry with Pillow and the DejaVu fonts — see `draw_image.py` in
this repository, which regenerates `entry.png`; the program the grader
runs needs no Pillow.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is deterministic: running it twice gives the same bytes.
