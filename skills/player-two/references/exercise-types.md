# Exercise types

Use these `type` values in the SESSION data. The card game knows how to show each.

| type | She does | Prepares for | Fields beyond the common ones |
| --- | --- | --- | --- |
| `pick` | Picks the right answer of 4 | Multiple choice | `options`, `answer`, `why_wrong` |
| `case` | Reads a two-line case, picks which idea from her course applies | Case studies | `situation`, `options`, `answer`, `why_wrong` |
| `number` | Types the result of one calculation step | Calculation problems | `numbers`, `formula`, `answer` (a number), `unit` |
| `order` | Puts steps in order by tapping them | Procedures, methods | `items` (in the right order) |
| `recall` | Says the answer to herself, flips, swipes "knew it / review" | Definitions, lists | `answer` (the back of the card) |
| `mistake` | Taps the wrong line in a worked solution | Checking her own work | `lines`, `answer` (index of the wrong line, from 0) |

Common fields on every exercise: `type`, `label` (3 to 6 words naming what it tests, shown in her results: "Customer-owned touch point"), `ask`, `why` (one or two sentences), `quote` (word for word from her material), `source` (file name and page), `level` (remember, understand, apply, analyse, evaluate), `difficulty` (1 to 3).

For a `number` exercise, `formula` is plain arithmetic using the names in `numbers`, for example `"(profit - 0.1 * returns)"`. The card game recomputes it and refuses the card if it does not give `answer` within 1%.
