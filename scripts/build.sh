#!/bin/sh
# Copies the app into the skill and builds the ZIP students upload to Claude.
# Run from anywhere: sh scripts/build.sh
set -e
cd "$(dirname "$0")/.."
cp app/buddy.html skills/buddy/assets/buddy.html
mkdir -p dist
rm -f dist/buddy-skill.zip
find skills/buddy -name '__pycache__' -prune -exec rm -rf {} +
(cd skills && zip -qr ../dist/buddy-skill.zip buddy)
echo "Built dist/buddy-skill.zip"
