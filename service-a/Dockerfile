FROM python:3.9
WORKDIR /app
RUN pip install flask requests
COPY app.py .
COPY registry.json .
CMD ["python", "app.py"]
