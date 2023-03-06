FROM python:3.9
ENV REACT_APP_BASE_URL=https://scenesoiltemp.herokuapp.com/
# ENV FLASK_APP=app
# ENV FLASK_ENV=production
# ENV SQLALCHEMY_ECHO=True
WORKDIR /var/www
COPY . .
COPY /react-app/build/* app/static/
RUN pip install -r ./app/requirements.txt
CMD gunicorn app:app
