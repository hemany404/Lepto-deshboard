FROM python:3.11-slim
LABEL mainttainer="https://github.com/hemany404"
WORKDIR /app
COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ..
ENTRYPOINT ["streamlit", "run", "Home.py", "--host", "0.0.0.0"]
CMD ["--port", "8501"]