FROM python:3.9-slim
SHELL ["/bin/bash", "-c"]
WORKDIR /var/app/
RUN <<EOF
apt update
apt install cups python3-dev libcups2-dev build-essential libpq-dev -y
lpadmin -p hp-casa -E -v ipp://192.168.100.10/ipp/print -m everywhere
EOF
COPY src/ .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5000", "server:app"]
