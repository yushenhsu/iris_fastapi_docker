# 使用 Python 3.9 作為基礎映像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 複製需求文件到容器
COPY ./requirements.txt /app/requirements.txt

# 安裝需求
RUN pip install --no-cache-dir -r /app/requirements.txt

# 複製應用代碼到容器
COPY . /app

# 暴露容器的端口（與 uvicorn 的默認端口相同）
EXPOSE 8000

# 運行 FastAPI 應用的命令
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
