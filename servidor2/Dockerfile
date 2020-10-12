FROM node:latest

RUN mkdir -p /usr/src/app
WORKDIR /urc/src/app
COPY package.json /usr/src/app/

RUN npm install

ADD  src /usc/src/app/src
ADD public /usr/src/app/public
COPY . .
CMD ["npm", "start"]