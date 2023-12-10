FROM node:20.7.0-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install -g npm@10.2.5
RUN npm ic
COPY . .
RUN npm run build
FROM nginx:stable
COPY --from=build /app/dist/frontend /usr/share/nginx/html
EXPOSE 4200