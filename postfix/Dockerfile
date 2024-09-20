
FROM debian:latest

# SMTP build and parameterization

RUN apt-get update && \
    apt-get install -y postfix sasl2-bin && \
    rm -rf /var/lib/apt/lists/*

COPY main.cf /etc/postfix/main.cf
COPY master.cf /etc/postfix/master.cf

# SSL keys

COPY /etc/letsencrypt/live/lycaste.eu/fullchain.pem /etc/ssl/certs/mailcert.pem
COPY /etc/letsencrypt/live/lycaste.eu/privkey.pem /etc/ssl/private/mailkey.pem
RUN chmod 600 /etc/ssl/private/mailkey.pem && \
    chown root:root /etc/ssl/private/mailkey.pem

EXPOSE 25 587

CMD ["postfix", "start-fg"]