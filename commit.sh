# commit.sh 371 372

git add "g${1}.py"
git commit -m "feat: create g${1}.py"
cp "__g.py" "g${2}.py"
code "g${2}.py"
