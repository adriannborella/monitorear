FROM python:3.9

ENV PYTHONUNBUFFERED 1

ENV HOME=/home/app
ENV APP_HOME=$HOME/web

RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/uploads

ADD back/requirements/base.txt $APP_HOME
ADD back/requirements/local.txt $APP_HOME

RUN pip install -U pip
RUN pip install -r $APP_HOME/local.txt


WORKDIR $APP_HOME


CMD ["bash"]