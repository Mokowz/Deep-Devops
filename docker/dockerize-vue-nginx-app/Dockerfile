FROM node:23-alpine

WORKDIR /vue/app

# Copy the package.json files
COPY package*.json ./

# Install dependencies
RUN npm install 

COPY dist/ ./dist/

EXPOSE 3000

CMD ["npx", "serve", "dist", "-n"]