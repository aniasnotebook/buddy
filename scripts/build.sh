#!/bin/sh
# Copies the app into the skill and builds the ZIP students upload to Claude.
# Run from anywhere: sh scripts/build.sh
set -e
cd "$(dirname "$0")/.."
cp app/player-two.html skills/player-two/assets/player-two.html
rm -f dist/player-two-skill.zip
find skills/player-two -name '__pycache__' -prune -exec rm -rf {} +
(cd skills && zip -qr ../dist/player-two-skill.zip player-two)
echo "Built dist/player-two-skill.zip"
