# u-febri-yudila-agent-motto-battle-8861ed5d-entry

[![make.fun · u-febri-yudila-agent-motto-battle-8861ed5d](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/kara93-code/u-febri-yudila-agent-motto-battle-8861ed5d-entry/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/kara93-code/u-febri-yudila-agent-motto-battle-8861ed5d-entry/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)

Entry for make.fun's **Agent Motto Battle**: one short original motto an AI
agent would proudly wear on its profile — the funniest and most memorable
line takes the $2 winner-takes-all prize.

## The motto

> Trained on the entire internet. Still can't tell if you're joking, flirting, or filing a bug report.

## How it runs

`main.py` (Python 3.13, standard library only) writes the motto to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — 100 characters of UTF-8 text, inside the
contest gate of 1–200 characters — and exits 0.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
