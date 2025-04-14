#!/usr/bin/env bash

echo "deploying math87-site"
cd /home/george/Prof-VC/classes/2025-Sp-Math087/
git add .
read -p "Commit message: " msg
git commit -m "$msg"
git push origin main
