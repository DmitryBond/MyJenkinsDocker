FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir  /etc/letsencrypt/
RUN mkdir  /etc/letsencrypt/live/
RUN mkdir  /etc/letsencrypt/live/example.com/
COPY ./fullchain.pem /etc/letsencrypt/live/msite11.sytes.net/fullchain.pem
COPY ./privkey.pem /etc/letsencrypt/live/msite11.sytes.net/privkey.pem
COPY ./www /var/www/
COPY ./site_conf /etc/nginx/conf.d
COPY ./nginx.conf /etc/nginx/
#COPY nginx.crt /etc/ssl/certs/nginx/nginx.crt
#COPY nginx.key /etc/ssl/certs/nginx/nginx.key
##Volume configuration
VOLUME /var/www
EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
