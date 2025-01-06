# Build Stage
FROM node:23-bookworm-slim

RUN <<EOF
apk update
apk add git
git clone -q https://github.com/docker-in-practice/todo.git
EOF

# Move to the working directory
WORKDIR /todo
RUN npm install > /dev/null

# Runtime Stage
FROM node:
EXPOSE 8000

# Command to run when the image is run
CMD ["npm", "start"]
