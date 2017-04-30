#!/bin/bash
# export PYENV_VIRTUALENV_DISABLE_PROMPT=1

eval "$(pyenv init -)"

eval "$(pyenv virtualenv-init -)"
export PATH="$HOME/.pyenv/bin:$PATH"
# echo $PATH

pyenv activate sharingan
echo "$(python --version)"
export FLASK_APP=/Users/wanchang/Downloads/bitbucket/sharingan
echo $FLASK_APP
cd /Users/wanchang/Downloads/bitbucket/sharingan

mysql.server start
# the way to invoke it:   . /Users/wanchang/Downloads/bitbucket/abel.sh