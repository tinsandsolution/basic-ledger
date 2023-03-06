FROM python:3.9 as base
ENV REACT_APP_BASE_URL=https://localhost/

# ENV FLASK_APP=app
# ENV FLASK_ENV=production
# ENV SQLALCHEMY_ECHO=True
WORKDIR /var/www
# copy the backend
COPY backend/ backend/
# install server dependencies
RUN pip install -r backend/requirements.txt

EXPOSE 8000

# starting the server
# CMD ["python", "backend/manage.py", "runserver"]
CMD [ "gunicorn", "app.wsgi:application", "-b", "0.0.0.0:8000", "--reload"]

# some useful commands:
# docker build -t scenesoiltemp .
# docker run -p 8000:8000 scenesoiltemp -name scenesoiltemp
# docker run -p 5000:5000 -d scenesoiltemp
# docker ps
# docker stop scenesoiltemp
# run the container with DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
# docker run -p 80:80 - -e DATABASE_URL=postgres://sxtwzmpjrxqnll:10d082f58a6ac668fe0fa8eea80bf0ce8a71f93a84663f87538038a19af8a5d1@ec2-34-197-84-74.compute-1.amazonaws.com:5432/db1nn93oj31pld -d scenesoiltemp
# view the log of the container
# docker logs <container id>
