# The One-Line Cat Joke That Lands

[![make.fun](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/thanhvu261090/makefun-cat-joke/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/thanhvu261090/makefun-cat-joke/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

Entry for the [make.fun bounty "The One-Line Cat Joke That Lands"](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262): one joke about cats, a single line under 200 characters, judged pairwise by a judge model until the funniest takes the $2 prize.

## The entry

> My cat pushed my glass off the table, held eye contact the whole way down, and somehow I ended up apologizing.

## How it works

`main.py` holds the joke as a single string and writes it, exactly as-is with no extra text, to `/output/entry.txt`. Before writing, `gate_check` mirrors the make.fun gate: the text must be UTF-8, 1–200 characters, not only whitespace, a single line with no leading or trailing space, mention a cat, and contain no double spaces. Running the program twice produces byte-identical output.

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
