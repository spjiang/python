FROM ubuntu:16.04
MAINTAINER spjiang <spjiang@aliyun.com>

RUN apt-get update
RUN apt-get -y install apache2
RUN apt-get -y install python
RUN apt-get -y install python-pil python-pip python-matplotlib python-scipy python-sklearn
RUN apt-get install -y vim
RUN apt-get install -y install wget
RUN apt-get install -y install unzip
RUN apt-get install -y libmysqlclient-dev
#安装mysql
RUN wget https://files.pythonhosted.org/packages/a5/e9/51b544da85a36a68debe7a7091f068d802fc515a3a202652828c73453cad/MySQL-python-1.2.5.zip && \
    pip install six && \
    unzip MySQL-python-1.2.5.zip && \
    cd MySQL-python-1.2.5 && \
    python setup.py build && \
    python setup.py install










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
