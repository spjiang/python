## 不指定版本默认使用最新版本
FROM ubuntu
MAINTAINER spjiang <spjiang@aliyun.com>
## 更改配置源
RUN mv /etc/apt/sources.list /etc/apt/sources-bak.list
ADD $PWD/sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y openssh-server


