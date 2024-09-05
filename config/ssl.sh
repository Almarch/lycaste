# https://gist.github.com/taoyuan/39d9bc24bafc8cc45663683eae36eb1a

openssl genrsa -out cert.key 2048
openssl req -new -key cert.key -out cert.csr
openssl x509 -req -days 3650 -in cert.csr -signkey cert.key -out cert.crt

sudo mkdir /etc/nginx/ssl
sudo mv cert.crt /etc/nginx/ssl/lycaste.eu.crt
sudo mv cert.key /etc/nginx/ssl/lycaste.eu.key