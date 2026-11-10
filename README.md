# Buddy

Turns a student's own course files into 5-minute study games inside her Claude: one folder per course, games built for her exam, every answer proved by a sentence from her course, and mistakes that come back until she gets them right.

No server, no account: her Claude does the AI work on her own plan, and her courses and scores stay in her browser.

## Install

**Claude (app or claude.ai)**

Each student installs her own Buddy, in one message, from the landing page (https://aniasnotebook.github.io/study-engine/) or this link. It starts a Claude conversation with the message already written; she sends it, and her Claude creates her own copy of the app in her account.

https://claude.ai/new?q=Ouvre%20Buddy%20%3A%20cr%C3%A9e%20un%20artifact%20HTML%20dont%20le%20contenu%20est%20exactement%20ce%20fichier%2C%20copi%C3%A9%20en%20entier%2C%20sans%20rien%20changer%20ni%20raccourcir.%20Titre%20%3A%20Buddy.%20Puis%20propose-moi%20de%20connecter%20Google%20Drive%20pour%20retrouver%20mes%20cours.%20https%3A%2F%2Fraw.githubusercontent.com%2Faniasnotebook%2Fstudy-engine%2Fmain%2Fapp%2Fbuddy.html

Backup: download [`dist/buddy-skill.zip`](dist/buddy-skill.zip), upload it in Claude under Customize › Skills (code execution on), then say **Ouvre Buddy** in a new conversation.

**Coding agents (Claude Code, Codex, Gemini CLI, Cursor)**

```
npx skills add aniasnotebook/study-engine
```

Then ask your agent: "Buddy: quiz me on <course folder>". The agent runs one checked session and writes it as a card game page.

**ChatGPT and Gemini chat apps:** not yet. Their pages can't call the AI the way Claude's can.

## How it works

1. Her Claude creates the app (`app/buddy.html`) as an artifact in her own conversation. It runs on her account.
2. She adds a course: PDF (pdf.js), slides (.pptx) and Word (.docx) (JSZip), text, photos and scanned PDFs (read by her Claude). Anything else gets a plain message asking for a PDF. Past exams are spotted by name and set the style of the questions.
3. To build a game, the app sends the 10 exercise templates, her exam (format, date), the game she chose and her course text to her Claude, and asks for cards as JSON.
4. The app keeps only cards whose quote is found word for word in her files and whose answer checks out (calculations are recomputed), then shows each with its page.
5. Her games are saved in "Mes jeux" (replay, rename, delete). The "Partie du jour" is a free mix of her games, her mistakes first.

## Repository

| Path | What it is |
|---|---|
| `app/buddy.html` | The app: the single source of truth |
| `skills/buddy/` | The skill: instructions, learning and game rules, the 10 templates, quote checker, and a copy of the app in `assets/` |
| `docs/index.html` | The landing page, served by GitHub Pages at https://aniasnotebook.github.io/study-engine/ |
| `scripts/build.sh` | Copies the app into the skill and builds `dist/buddy-skill.zip` |
| `dist/buddy-skill.zip` | What students upload to Claude |

After changing the app, run `sh scripts/build.sh` and commit the new ZIP.

## Known limits

- Claude only for the app. Plan usage limits apply to each game built.
- The app is about 70 KB: her Claude has to copy it exactly when installing. Not yet tested on a free account.
- Scans and photos need Claude with images; only the first 12 pages of a scan are read.
- Courses and scores are kept in one browser. Clearing site data erases them.
