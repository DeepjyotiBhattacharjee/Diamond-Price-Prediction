# this is my end to end project

# first initialize git


```
git init
```

```
git add <filename> 
or 
git add .
```

```
git commit -m "message"
```

```
git pull
```

```
python setup.py install
```

# or add -e . in requirements.txt file and  run : 
```
pip install -r requirements.txt

```

# dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/DeepjyotiBhattacharjee/Diamond-Price-Prediction.mlflow 
MLFLOW_TRACKING_USERNAME=DeepjyotiBhattacharjee 
MLFLOW_TRACKING_PASSWORD=b4bf0c4be7b2ef14165b6d36816954d13e813a2b 
python script.py

Run this to export as env variables

```
export MLFLOW_TRACKING_URI=https://dagshub.com/DeepjyotiBhattacharjee/Diamond-Price-Prediction.mlflow 
export MLFLOW_TRACKING_USERNAME=DeepjyotiBhattacharjee 
export MLFLOW_TRACKING_PASSWORD=b4bf0c4be7b2ef14165b6d36816954d13e813a2b 
```