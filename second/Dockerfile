FROM python
RUN pip install flask
RUN pip3 cache purge
RUN echo "d4rkc0de{sh!t_s3cur3d_smh}" > /flag.txt
RUN chmod 644 /flag.txt
RUN groupadd -r user && useradd -r -g user user
USER user
WORKDIR /app
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
EXPOSE 5000