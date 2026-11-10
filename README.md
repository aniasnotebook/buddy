# Player Two

Turns a student's own course files into a study app inside her Claude: one folder per course, exercises built for her exam, every answer proved by a sentence from her course, and mistakes that come back until she gets them right.

Working name. No server, no account: her Claude does the AI work on her own plan, and her courses and scores stay in her browser.

## Install

**Claude (app or claude.ai)**

Each student installs her own Player Two, in one message. Open this link: it starts a Claude conversation with the message already written; send it. Her Claude reads the app from this repo and creates her own copy, in her account.

https://claude.ai/new?q=Ouvre%20Player%20Two%20%3A%20cr%C3%A9e%20un%20artifact%20HTML%20dont%20le%20contenu%20est%20exactement%20ce%20fichier%2C%20copi%C3%A9%20en%20entier%2C%20sans%20rien%20changer%20ni%20raccourcir.%20Titre%20%3A%20Player%20Two.%20https%3A//raw.githubusercontent.com/aniasnotebook/study-engine/main/app/player-two.html

Backup: download [`dist/player-two-skill.zip`](dist/player-two-skill.zip), upload it in Claude under Customize › Skills (code execution on), then say **Ouvre Player Two** in a new conversation.

She adds a course (PDF or text, from her phone's file picker, Google Drive included), taps "Créer ma partie", and plays.

**Coding agents (Claude Code, Codex, Gemini CLI, Cursor)**

```
npx skills add aniasnotebook/study-engine
```

Then ask your agent: "Player Two: quiz me on <course folder>". The agent runs one checked session and writes it as a card game page.

**ChatGPT and Gemini chat apps:** not yet. Their pages can't call the AI the way Claude's can.

## How it works

1. The skill has her Claude create the app (`assets/player-two.html`) as an artifact in her own conversation. It runs on her account.
2. The app reads her PDF in the browser (pdf.js) and keeps the text, page by page, in browser storage.
3. To build a game, the app sends the engine rules, her settings (exam format, date, time, way of learning) and her course text to her Claude, and asks for cards as JSON.
4. The app keeps only cards whose quote is found word for word in her file, then shows each with its page.
5. A missed card comes back at the end of the game, then waits in "Revoir mes erreurs".

## Repository

| Path | What it is |
|---|---|
| `app/player-two.html` | The app: the single source of truth |
| `skills/player-two/` | The skill: instructions, learning and game rules, card types, quote checker, and a copy of the app in `assets/` |
| `docs/index.html` | The landing page, served by GitHub Pages at https://aniasnotebook.github.io/study-engine/ |
| `scripts/build.sh` | Copies the app into the skill and builds `dist/player-two-skill.zip` |
| `dist/player-two-skill.zip` | What students upload to Claude |

After changing the app, run `sh scripts/build.sh` and commit the new ZIP.

## Known limits

- Claude only for the app. Free-plan usage limits apply to each game built.
- Scanned PDFs (photos of pages) can't be read; they need a PDF with text.
- Courses and scores are kept in one browser. Clearing site data erases them.
- Google Drive: open the file in the chat, or download it and add it in the app.
