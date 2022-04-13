path=$(pwd)/.venv
python3 -m venv $path
echo "venv successfully created in $path"
pip install -r requirements.txt
echo "Installed pip dependencies:"
echo $(pip list)