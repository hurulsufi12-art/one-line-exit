# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/hurulsufi12-art/one-line-exit/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/hurulsufi12-art/one-line-exit/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

Entry for the [make.fun bounty "The One-Line Exit"](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1): one funny single-line resignation letter, at most 140 characters.

## The letter

> I hereby resign, effective immediately — after three years of turning it off and on again, I have decided to turn myself off.

(125 characters, one line.)

## How it works

`main.py` (Python 3.13, standard library only) validates the text against the bounty gate — 1–140 characters (counted as characters, not bytes), not whitespace-only, a single line, no control characters — and then writes it verbatim, with no trailing newline, to `$OUTPUT_DIR/entry.txt` (default `/output`). An invalid text raises before writing anything. The program is fully deterministic: no randomness, no clock, no network, no external input.
