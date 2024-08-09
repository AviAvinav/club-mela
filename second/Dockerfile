FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN echo "d4rkc0de{sh!t_s3cur3d_smh}" > /flag.txt
RUN chmod 644 /flag.txt 
RUN groupadd -r user && useradd -r -g user user
USER user
CMD ["python", "app.py"]
