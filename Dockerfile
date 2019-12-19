FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY /src/server.py /src/server.py

EXPOSE  80

CMD ["python", "/src/server.py", "-p 80"]