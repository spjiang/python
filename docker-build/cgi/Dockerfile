FROM ubuntu:16.04
MAINTAINER spjiang <spjiang@aliyun.com>

RUN apt-get update
RUN apt-get -y install apache2
RUN apt-get -y install python
RUN apt-get -y install python-pil python-matplotlib python-scipy python-sklearn
RUN apt-get install -y vim

#load apache cgi module
RUN a2enmod cgi
RUN service apache2 restart

#enable cgi in the website root
#second block to allow .htaccess
RUN echo "                       \n \
<Directory /var/www/html>        \n \
   AllowOverride None              \n \
   Options +ExecCGI     \n \
   Order allow,deny  \n \
   Allow from all      \n \
   AddHandler cgi-script  .cgi .py \n \
</Directory>                     \n \
" >> /etc/apache2/apache2.conf
ADD ./ /var/www/html
RUN chmod -R u+rwx,g+x,o+x /var/www/html

RUN ln -sf /usr/bin/python /usr/local/bin/python
EXPOSE 80
CMD /usr/sbin/apache2ctl -D FOREGROUND
