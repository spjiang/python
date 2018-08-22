FROM ubuntu:16.04
MAINTAINER spjiang <spjiang@aliyun.com>

RUN apt-get update
RUN apt-get -y install httpd
RUN apt-get -y install python
RUN apt-get -y install python-pil python-matplotlib python-scipy python-sklearn

#load apache cgi module
RUN a2enmod cgi
RUN service apache2 restart

#enable cgi in the website root
#second block to allow .htaccess
RUN echo "                       \n \
<Directory /var/www/html>        \n \
   Options +ExecCGI              \n \
   Order allow,deny     \n \
   AddHandler cgi-script .cgi .pl .py \n \
   DirectoryIndex index.py       \n \
</Directory>                     \n \
" >> /etc/apache2/apache2.conf

RUN chmod -R u+rwx,g+x,o+x /var/www/html

RUN ln -sf /usr/bin/python /usr/local/bin/python
EXPOSE 80
CMD /etc/init.d/httpd restart