# Fix Human Sleep: Funniest Patch Note

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

Entry for the make.fun bounty **Fix Human Sleep: Funniest Patch Note**
([bounty page](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)).

## The entry

`main.py` writes one line of patch notes to `/output/entry.txt`:

> Fixed: 2 a.m. cringe replay no longer autoplays.

One line, 48 characters — a real changelog line about fixing human sleep:
the 2 a.m. cringe replay, the brain autoplaying every embarrassing moment
instead of sleeping, is switched off. Terse, specific, and it trusts the
reader to know the feeling.

## How it was picked

16 candidate lines were generated — 8 with DeepSeek (brutal mode, short
calls) and 8 self-authored — then critique-picked against the judge's
criteria: reads as a real patch note about fixing human sleep first, then
the joke landing on a single read, then changelog voice, then staying a
single short line, then surprise. DeepSeek's critique picked this line as
the winner: the joke is purely structural, "autoplays" reframes the
2 a.m. cringe replay as a UI setting nobody consented to, and the fix
lands without needing the word "dream" explained.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

Requires only the Python 3 standard library. The output is deterministic:
the same single line on every run.
