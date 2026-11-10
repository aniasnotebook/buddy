# Exercise templates

Buddy has 10 templates. Claude picks one and fills its fields; it never invents a layout. Every card also has `quote` (one sentence copied word for word from her course, 30 words max) and `page`. A card whose quote isn't found in her files is dropped.

| type | She does | Prepares for | Fields |
| --- | --- | --- | --- |
| `pick` | Picks the right answer of 4 | Multiple choice | `situation`?, `ask`, `options` (4), `answer`, `why`, `trap` |
| `case` | Reads a two-line case, makes 2 or 3 decisions in a row | Case studies | `situation`, `steps` [{`ask`, `options`, `answer`}] |
| `sort` | Puts each item in its box | Categories, typologies | `ask`, `buckets` (2-4), `items` [{`text`, `bucket`}] |
| `order` | Taps the steps in order | Procedures, methods | `ask`, `items` (in the right order) |
| `build` | Builds an answer from blocks, avoiding the traps | Essays, definitions | `ask`, `items` (in order), `traps` (2) |
| `flash` | Says the answer to herself, flips, "Je savais" or "À revoir" | Definitions | `front`, `back` |
| `mistake` | Taps the wrong line in a student's answer | Checking her own work | `ask`, `lines`, `answer` (index of the wrong line, from 0) |
| `number` | Types the result of a calculation | Calculation problems | `situation`, `ask`, `numbers`, `formula`, `answer`, `unit`, `steps` |
| `speed` | Matches terms and definitions against the clock | Vocabulary | `ask`, `pairs` [[term, definition]] |
| `explain` | Writes (or dictates) an answer, Claude grades it against the key ideas | Essays, oral | `ask`, `model`, `keys` (2-4) |

For a `number` card, `formula` is plain arithmetic using the names in `numbers`, for example `"(profit - 0.1 * returns)"`. The app recomputes it and drops the card if it does not give `answer` within 1%.

In the card-game fallback (`references/card-game.html`, coding agents), only `pick`, `case`, `number`, `order`, `recall` (= `flash`) and `mistake` are drawn.
