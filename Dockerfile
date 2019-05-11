#base image
FROM sudeepgumaste/python-flask

#installing additional dependencies
RUN pip3 install pillow

#changing work dir
WORKDIR /usr/cleanApp

#copy the project
COPY . .

#open debug port
EXPOSE 5000

#execute on startup
ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]