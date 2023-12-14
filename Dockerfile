# 使用Python镜像
FROM python:3.8-slim

# 工作目录设置
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# 复制所有文件到工作目录
COPY . /app

# 暴露端口
EXPOSE 8501

# 启动应用
CMD ["streamlit", "run", "app.py"]