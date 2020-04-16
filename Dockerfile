FROM python:3.8.2-slim
RUN pip install sklearn==0.22.2 keras==2.3.1 numpy==1.18.2
ENV MODEL_PATH /app/generated.py
ENV USER_DATA_PATH /app/data
