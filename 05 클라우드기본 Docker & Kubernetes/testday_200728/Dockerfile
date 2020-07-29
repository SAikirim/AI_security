FROM ubuntu
RUN apt-get -y update && apt-get -y upgrade
RUN  apt-get -y install nginx
#ADD index.html /usr/share/nginx/html/index.html
ADD index.html /var/www/html/index.html
EXPOSE 80
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
ENTRYPOINT ["nginx"]
#CMD [ "-g", "daemon off;"]
