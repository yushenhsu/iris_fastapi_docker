#!/usr/bin/env python
# coding: utf-8

# In[1]:


# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. 初始化 FastAPI 應用
app = FastAPI()

# 2. 加載訓練好的模型
model = joblib.load('iris_model.pkl')

# 3. 定義數據模式
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 4. 定義預測端點
@app.post("/predict/")
async def predict(iris: IrisData):
    data = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]])
    prediction = model.predict(data)
    predicted_class = int(prediction[0])
    return {"predicted_class": predicted_class}

