FROM python:3.9
ENV REACT_APP_BASE_URL=https://scenesoiltemp.herokuapp.com/
# ENV FLASK_APP=app
# ENV FLASK_ENV=production
# ENV SQLALCHEMY_ECHO=True
WORKDIR /var/www
COPY . .
COPY /frontend/build/* /backend/app/static/
RUN ls
RUN pip install -r backend/requirements.txt
CMD gunicorn backend/app.wsgi:application
