# Designing an Uma Json.

## Basics

Umas are formatted in Pure Json. They take very specific arguments that are **COURSE DEPENDANT**.

e.g. An uma in game might have S in long but C in mile. The Umalator does not differenciate!
It will read `"distanceAptitude": "S",` and consider you **S** Aptitude for ANY RACE THE UMA IS PLACED IN.

Consider this when formatting your Umas.
(Maybe implement a secondary system to import umas by track distance.)

---

## `speed`, `stamina`, `power`, `guts`, `wit`:

These are arguments each ranging between `0` and `1200` as of time of writing for Global. (Stat caps will be raised in future updates)
These are Uma specific, so there should not need to be any changes between umas.

```json
"speed": 1200,
"stamina": 1200,
"power": 800,
"guts": 700,
"wisdom": 700,
```

---

## Strategy:

Strategies come directly from the Japanese naming schemes where the og umalator comes from.
The different strategies are:

- `Nige`
  - Front runner
- `Senjour`
  - Pace Chaser
- `Sasi`
  - Late Surger
- `Oikomi`
  - End Closer

Place the specified strategy string in the file like so:

```json
"strategy" : "Sasi",
```

NOTE: `strategyAptitude` is dependant on this selection. Make sure your aptitude matches the strategy chosen!

---

## Aptitudes:

The current surface, distance, and strategy aptitudes. These depend on previous sections so make sure you match the correct course/strategy with it's aptitude.
Letter grades vary from `S` all the way to `G`
Available grades: `{S, A, B, C, D, E, F, G}`

```json
"distanceAptitude": "S",
"surfaceAptitude": "A",
"strategyAptitude": "A",
```

---

## Skills:

Skills are a Json list of the skill ids for your Uma.
i.e. Your Uma has "Professor of Curvature" so you add `[..., 200331, ...]` to your `"skills"` key.
Find specific skill ids by Online Umalator: https://alpha123.github.io/uma-tools/umalator-global/
Or by running

```bash
npx ts-node tools/skillgrep.ts --help
```

That is an english/japanese search for skills.

Format the skills like:

```json
"skills": [900271, 900201, ...],
```
