#!/usr/bin/env python3
"""Check a practice session before the student sees it.

Usage: python3 check_session.py session.json course1.pdf [course2.txt ...]

Keeps only exercises that pass every check and writes them to session.checked.json.
Prints one line per dropped exercise and why. Standard library only; reads PDFs
with `pdftotext` if it is installed, otherwise pass .txt files.
"""
import json, re, subprocess, sys, unicodedata

def norm(s):
    s = unicodedata.normalize("NFKC", str(s))          # joined letters such as "ﬁ" become "fi"
    s = re.sub(r"-\s*\n\s*", "", s)                    # words broken by a hyphen at a line end
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "")
    return re.sub(r"\s+", " ", s).strip().lower()

def read(path):
    if path.lower().endswith(".pdf"):
        try:
            return subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True, check=True).stdout
        except Exception:
            sys.exit(f"Cannot read {path}: install pdftotext or pass a .txt export.")
    return open(path, encoding="utf-8", errors="ignore").read()

def calc(formula, values):
    tokens = re.findall(r"\d+(?:\.\d+)?|[A-Za-z_]\w*|[-+*/()]", str(formula))
    if "".join(tokens) != re.sub(r"\s", "", str(formula)):
        raise ValueError("only + - * / ( ), numbers and names are allowed")
    pos = 0
    def primary():
        nonlocal pos
        t = tokens[pos]; pos += 1
        if t == "(":
            v = expr(); pos += 1; return v
        if t == "-":
            return -primary()
        if re.match(r"\d", t):
            return float(t)
        if t in values:
            return float(values[t])
        raise ValueError(f"unknown name {t}")
    def term():
        nonlocal pos
        v = primary()
        while pos < len(tokens) and tokens[pos] in "*/":
            op = tokens[pos]; pos += 1; r = primary(); v = v * r if op == "*" else v / r
        return v
    def expr():
        nonlocal pos
        v = term()
        while pos < len(tokens) and tokens[pos] in "+-":
            op = tokens[pos]; pos += 1; r = term(); v = v + r if op == "+" else v - r
        return v
    return expr()

def problems(e, text):
    p = []
    if not e.get("ask"): p.append("no question")
    if not e.get("quote"): p.append("no quote")
    elif text and norm(e["quote"]) not in text: p.append("quote not found word for word in the course files")
    t = e.get("type")
    if t in ("pick", "case"):
        o = e.get("options") or []
        if len(o) != 4 or len(set(o)) != 4: p.append("needs 4 different options")
        if e.get("answer") not in o: p.append("answer is not one of the options")
    if t == "number":
        try:
            v = calc(e.get("formula", ""), e.get("numbers") or {})
            a = float(e.get("answer"))
            if abs(v - a) > max(0.5, abs(a) * 0.01): p.append(f"formula gives {round(v, 2)}, not {a}")
        except Exception as x:
            p.append(f"formula does not compute ({x})")
    if t == "order" and len(e.get("items") or []) < 2: p.append("needs at least 2 steps")
    if t == "mistake":
        lines, a = e.get("lines") or [], e.get("answer")
        if not isinstance(a, int) or not 0 <= a < len(lines): p.append("answer is not a line number")
    return p

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    session = json.load(open(sys.argv[1], encoding="utf-8"))
    text = norm(" ".join(read(f) for f in sys.argv[2:])) if len(sys.argv) > 2 else ""
    kept = []
    for i, e in enumerate(session.get("exercises", []), 1):
        p = problems(e, text)
        if p: print(f"Dropped exercise {i} ({e.get('label') or e.get('ask', '')[:50]}): {'; '.join(p)}")
        else: kept.append(e)
    session["exercises"] = kept
    out = re.sub(r"\.json$", "", sys.argv[1]) + ".checked.json"
    json.dump(session, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    note = "" if text else " (quotes NOT checked: no course files given)"
    print(f"Kept {len(kept)} exercises -> {out}{note}")

if __name__ == "__main__":
    main()
