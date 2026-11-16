# Closer Brain skills

Seven skills for the Evolv Closer Brain project:

| Skill | Expert | Covers |
|---|---|---|
| `jeremy-miner-discovery` | Jeremy Miner | Discovery (NEPQ) |
| `hormozi-offer-and-price` | Alex Hormozi | Offer and price |
| `belfort-tone-and-control` | Jordan Belfort | Tone and keeping control |
| `daniel-g-closing` | Daniel G | Closing |
| `chris-voss-objections` | Chris Voss | Objections |
| `owen-santos-call-review` | Owen Santos | Call reviews, including batch mode |
| `evolv-closer-brain` | All six | Combined call flow, master scorecard, 120-call batch review |

Each skill was built from about 20 scraped sources: top YouTube videos, podcast appearances and most-viewed social posts. The sources are listed in each skill's `references/sources.md`.

## Install
- **Claude account (works in every chat):** Settings → Capabilities → Skills → upload each `.skill` file from `_packaged/`.
- **Closer Brain Project:** upload `evolv-closer-brain/SKILL.md` and the files in `evolv-closer-brain/references/experts/` to the Project knowledge. Then add this line to the Project instructions: *"Use the Evolv Closer Brain skill and the expert playbooks in knowledge for every call prep, live coaching question and call review. Pull all Evolv product, pricing and claim details from the Evolv knowledge files."*

`evolv-closer-brain` has every expert's full method bundled inside it, so on its own it is enough for the Project.

## EVOLV product knowledge
Every skill has `references/evolv/`, generated from the EVOLV Source Brain:
- `evolv-knowledge.md`: pricing rules, goal → protocol matrix, catalogue with prices and doses, how to describe each compound, updates, links
- `evolv-protocol-cheatsheet.md`: phase-by-phase dosing and pen dosing
- `evolv-sales-process.md`: consultation intake, investment summary process, discount policy

## Refreshing after you update the Source Brain
In a Claude Code session on this repo, say: **"Refresh the Closer Brain skills from the Source Brain."** Claude will:
1. Read `governed.json` and `library.json` from the Source Brain artifact (https://claude.ai/artifact/XGwvgGnpVUwv5h8MQreyUz) into a scratch folder.
2. Run `closer-brain-skills/tools/refresh.sh <that folder>`. This rebuilds `references/evolv/` in all 7 skills, re-bundles the combined skill and repackages `_packaged/*.skill`.
3. Commit, push and send you the new `.skill` files. You then click **Save skill** on each card to replace the old version, and re-upload `evolv-closer-brain` files to the Project knowledge.
