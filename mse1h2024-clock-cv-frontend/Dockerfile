# этап сборки (build stage)
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY mse1h2024-clock-cv-frontend/package*.json ./
RUN npm install
COPY mse1h2024-clock-cv-frontend/ .
RUN npm run build

# этап production (production-stage)
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]