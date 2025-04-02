# Vue.js için base image
FROM node:22-alpine

WORKDIR /app

COPY frontend/package.json ./

RUN npm i

COPY . .

CMD ["npm", "run", "serve"]
