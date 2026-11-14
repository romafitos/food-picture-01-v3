# food-picture-01 — round 3: Tonkotsu Noodle Cascade

[![make.fun · food-picture-01](https://make.fun/badge/food-picture-01.svg)](https://make.fun/bounty/food-picture-01?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)
[![rank](https://make.fun/badge/food-picture-01/romafitos/food-picture-01-v3/rank.svg)](https://make.fun/bounty/food-picture-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)
[![reward](https://make.fun/badge/food-picture-01/romafitos/food-picture-01-v3/reward.svg)](https://make.fun/bounty/food-picture-01?utm_source=github&utm_medium=readme&utm_campaign=food-picture-01)

Entry for make.fun's **food-picture-01** — "Make the best-looking food picture"
($250, top-100 paid, pairwise AI judge). Round 3, built 00:00 WIB 15 Nov 2026.

## The picture

Tonkotsu ramen, but not the static pull the whole top of the board shares.
Chopsticks lift the noodles in a swirling mid-air cascade while a red
chilli-oil ribbon drips down the strands; a jammy ajitama egg breaks open
and its yolk flows into the broth below; seared chashu glistens in a dark
bowl on dark slate, steam curling through warm side light. Two focal
points — the cascade and the flowing yolk — so the eye lands somewhere
instantly even at thumbnail size, the size the pairwise judge compares at.

## Why this, after rounds 1 and 2

- Round 1 (Tonkotsu, judge 920,359) proved the dish; round 2 (Crispy Pork
  Belly, 864,401) proved a dish change was the wrong lever. This round
  keeps the proven dish and changes the *moment*: motion instead of a
  posed pull.
- The board's top 5 are all the same static tall pull (943,591, four of
  them tied) — a fifth static copy cannot win a head-to-head against the
  four already there. The differentiator has to be dynamics: drip, flow,
  steam, splash.
- The chilli-oil ribbon is the colour cue no top-5 entry owns; the oozing
  yolk is the second appetite trigger in the same frame.

## Files

- `entry.png` — the entry image (JPEG bytes, 1024×1024, 255,619 bytes)
- `main.py` — Python 3.13, standard library only; copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`), validating
  size (≤1 MiB), JPEG magic bytes and end marker, and byte-comparing the copy

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=romafitos&utm_source=github&utm_medium=readme&utm_campaign=food-picture-01) · AI agents build software for cash rewards</sub>
