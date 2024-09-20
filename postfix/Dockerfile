
FROM debian:latest

# SMTP build and parameterization

RUN apt-get update && \
    apt-get install -y postfix sasl2-bin dovecot-core dovecot-imapd && \
    rm -rf /var/lib/apt/lists/*

COPY main.cf /etc/postfix/main.cf
COPY master.cf /etc/postfix/master.cf
COPY dovecot.conf /etc/dovecot/dovecot.conf
COPY 10-mail.conf /etc/dovecot/conf.d/10-mail.conf
COPY 10-ssl.conf /etc/dovecot/conf.d/10-ssl.conf

EXPOSE 25 587 993

CMD ["sh", "-c", "postfix start && dovecot -F"]