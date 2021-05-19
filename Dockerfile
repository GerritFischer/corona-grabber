FROM python:3
ADD main.py /
RUN pip install beautifulsoup4
RUN pip install webdriver_manager
RUN pip install selenium

RUN apt-get -y update
RUN apt-get -y install chromium-driver
RUN apt-get -y install libxml2-dev libxslt-dev python-dev libxslt1-dev zlib1g-dev python3-dev
RUN apt-get -y install python-lxml python3-lxml
RUN apt-get -y upgrade

RUN pip3 install lxml


CMD [ "python", "./main.py" ]


