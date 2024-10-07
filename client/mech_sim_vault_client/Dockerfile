FROM node:22-alpine3.19 AS build

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY public/ ./public
COPY src/ ./src 

RUN npm run build 


FROM nginx:alpine

COPY --from=build /usr/src/app/build /usr/share/nginx/html 

COPY nginx.conf /etc/nginx/conf.d/default.conf 

EXPOSE 3000

# CMD ["nginx", "-g", "daemon off;"]
CMD ["nginx", "-g", "daemon off;"]



