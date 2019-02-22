#Setup base structure
FROM python:2.7
COPY . /tucan

#Setup netrc config
COPY ./.netrc /root/.netrc
RUN chmod 400 /root/.netrc

#Install python dependency
RUN pip2 install mechanize
RUN pip2 install lxml

#Install tucan app
RUN pip2 install -e /tucan

#Install mail
RUN apt-get update
RUN apt-get install -y mailutils
RUN apt-get install -y ssmtp

#Setup mail
COPY ./mail/ssmtp.conf /etc/ssmtp/ssmtp.conf
COPY ./mail/revaliases /etc/ssmtp/revaliases

#Exec Tucan on container execution
CMD tucan -m username@gmail.com
