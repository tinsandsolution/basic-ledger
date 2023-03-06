FROM python:3.9
ENV REACT_APP_BASE_URL=https://scenesoiltemp.herokuapp.com/

# ENV FLASK_APP=app
# ENV FLASK_ENV=production
# ENV SQLALCHEMY_ECHO=True
WORKDIR /var/www
# copy the backend
COPY backend/ backend/
# copy the frontend
COPY /frontend/build/* backend/app/static/
# install server dependencies
RUN pip install -r backend/requirements.txt
# starting the server
CMD ["python", "backend/manage.py", "runserver"]

# some useful commands:
# docker build -t scenesoiltemp .
# docker run -p 8000:8000 scenesoiltemp
# docker run -p 5000:5000 -d scenesoiltemp
# docker ps
# docker stop <container id>
# run the container with DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
# docker run -p 8000:8000 -e DATABASE_URL=postgres://sxtwzmpjrxqnll:10d082f58a6ac668fe0fa8eea80bf0ce8a71f93a84663f87538038a19af8a5d1@ec2-34-197-84-74.compute-1.amazonaws.com:5432/db1nn93oj31pld -d scenesoiltemp
# view the log of the container
# docker logs <container id>
