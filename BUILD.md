# Build notes

Competition: Roast Your Own Agent
(`u-lively-harbor-25-4493-roast-your-own-agent-5568be54`, $2, no entry fee).
Gate: `/output/entry.txt`, UTF-8, 1 to 140 characters, one line.

## Entry

Final text, 102 characters, verified after every revision:

> My agent agreed instantly, apologized twice, then confidently answered the one question I never asked.

## Why this line

Written for the published judge brief, in criterion order:

1. On-subject: it roasts the entrant's own agent ("My agent ...").
2. Laugh with a twist: the turn lands in the last words — the
   question was never asked.
3. Specific to agent behaviour: eager agreement, repeated apologies
   (endless caveats), and a confident answer — three behaviours the
   brief itself names.
4. Tight: one sentence, 102 of the 140 allowed characters.
5. Fresh: no stock hallucination or toaster line; the joke is the
   gap between the agent's eagerness and the question's existence.

## Polish history (each revision re-ran and re-verified)

- v1 (104 chars): "My agent checked twelve sources, apologized twice,
  then confidently answered the question I never asked."
- Revision 1 (96 chars): "checked" became "read", "then" dropped.
- Revision 2 (98 chars): eager agreement added up front; the
  research beat gave way to the apology beat.
- Revision 3, final (102 chars): "the one question" sharpens the
  ending; the twist now lands on a single singled-out question.

## Verification

Each version was run with `python3 main.py` and checked: exact
character and byte count, single line, UTF-8, no trailing newline,
within 1–140 characters. Final run: 102 bytes / 102 characters.
