FROM ollama/ollama:0.1.23
LABEL authors="CasedTheCoder"

WORKDIR /app
RUN apt-get update && apt install -y python3 python3-pip systemctl
COPY main.py .
COPY requirements.txt .
COPY ollama.service .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
RUN pip3 install -r requirements.txt
RUN useradd -r -s /bin/false -m -d /usr/share/ollama ollama
RUN cp ollama.service /etc/systemd/system/ollama.service
RUN systemctl daemon-reload && systemctl enable ollama

ENTRYPOINT ["/app/entrypoint.sh"]