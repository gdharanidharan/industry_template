echo [$(date)]: 'START'
echo [$(date)]: 'Creating conda env with version 3.8'
conda create --prefix ./env python=3.8 -y
echo [$(date)]: 'Activate env'
source activate ./env
echo [$(date)]: 'Install dev requirements'
pip install -r requirements_dev.txt
echo [$(date)]: 'END'
