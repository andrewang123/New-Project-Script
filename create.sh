#!/bin/bash

cd /Users/andrewang/Documents/Software_Projects/Scripts
python create.py $1

cd /Users/andrewang/Documents/Software_Projects
mkdir $1
cd $1

git init
git remote add origin https://github.com/andrewang123/$1.git
touch README.md
git add .
git commit -m "Initial commit"
git push -u origin master

