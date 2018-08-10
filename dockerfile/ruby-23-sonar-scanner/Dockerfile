FROM ruby:2.3
LABEL maintainer "Nguyen Manh Dung <dungnm@nal.vn>"

ENV SONAR_VERSION 3.2.0.1227
ENV SONAR_SCANNER_PACKAGE sonar-scanner-cli-${SONAR_VERSION}-linux
ENV SONAR_SCANNER_URL https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/${SONAR_SCANNER_PACKAGE}.zip
ENV SONAR_SCANNER_TMP sonar-scanner-${SONAR_VERSION}-linux

RUN apt-get update && \
  apt-get -y install unzip nodejs git

RUN wget -O /tmp/sonar-scanner.zip ${SONAR_SCANNER_URL}

RUN unzip /tmp/sonar-scanner.zip -d /tmp && \
  mv /tmp/${SONAR_SCANNER_TMP} /opt/sonar-scanner

RUN rm -f /tmp/sonar-scanner.zip

RUN ln -s /opt/sonar-scanner/bin/sonar-scanner /usr/bin/sonar-scanner
