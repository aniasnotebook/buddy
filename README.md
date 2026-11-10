# Player Two

Turns a student's own course files into a study app inside her Claude: one folder per course, exercises built for her exam, every answer proved by a sentence from her course, and mistakes that come back until she gets them right.

Working name. No server, no account: her Claude does the AI work on her own plan, and her courses and scores stay in her browser.

## Install

**Claude (app or claude.ai)**

Open the app: https://claude.ai/artifact/QGYa5c8WPtBdMXFxmQjc2m . It runs inside Claude, on the student's own account. Nothing to install. She adds a course (PDF or text), taps "Créer ma partie", and plays.

To open it from any conversation instead, upload [`dist/player-two-skill.zip`](dist/player-two-skill.zip) under Settings › Capabilities › Skills (code execution on), then say **Ouvre Player Two**.

**Coding agents (Claude Code, Codex, Gemini CLI, Cursor)**

```
npx skills add aniasnotebook/study-engine
```

Then ask your agent: "Player Two: quiz me on <course folder>". The agent runs one checked session and writes it as a card game page.

**ChatGPT and Gemini chat apps:** not yet. Their pages can't call the AI the way Claude's can.

## How it works

1. The app is one HTML page published in Claude. Opened by a signed-in student, it can ask Claude on her account.
2. The app reads her PDF in the browser (pdf.js) and keeps the text, page by page, in browser storage.
3. To build a game, the app sends the engine rules, her settings (exam format, date, time, way of learning) and her course text to her Claude, and asks for cards as JSON.
4. The app keeps only cards whose quote is found word for word in her file, then shows each with its page.
5. A missed card comes back at the end of the game, then waits in "Revoir mes erreurs".

## Repository

| Path | What it is |
|---|---|
| `app/player-two.html` | The app: the single source of truth |
| `skills/player-two/` | The skill: instructions, learning and game rules, card types, quote checker, and a copy of the app in `assets/` |
| `landing/index.html` | The shareable landing page (static) |
| `scripts/build.sh` | Copies the app into the skill and builds `dist/player-two-skill.zip` |
| `dist/player-two-skill.zip` | What students upload to Claude |

After changing the app, run `sh scripts/build.sh` and commit the new ZIP.

## Known limits

- Claude only for the app. Free-plan usage limits apply to each game built.
- Scanned PDFs (photos of pages) can't be read; they need a PDF with text.
- Courses and scores are kept in one browser. Clearing site data erases them.
- Google Drive: open the file in the chat, or download it and add it in the app.
