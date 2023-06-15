# commit.sh 371 372

git add "f${1}.py"
git commit -m "feat: create f${1}.py"
cp "__f.py" "f${2}.py"
code "f${2}.py"
