
FROM debian:latest

# SMTP build and parameterization

RUN apt-get update && \
    apt-get install -y postfix sasl2-bin && \
    rm -rf /var/lib/apt/lists/*

COPY main.cf /etc/postfix/main.cf
COPY master.cf /etc/postfix/master.cf

EXPOSE 25 587

CMD ["postfix", "start-fg"]