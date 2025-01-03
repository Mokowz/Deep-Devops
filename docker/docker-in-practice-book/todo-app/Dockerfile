FROM node

LABEL org.opencontainers.image.authors="ronniemokaya30@gmail.com"

RUN git clone -q https://github.com/docker-in-practice/todo.git

# Move to the working directory
WORKDIR /todo

ARG CACHEBUST=no
RUN npm install > /dev/null

EXPOSE 8000

# Command to run when the image is run
CMD ["npm", "start"]