FROM node:22-alpine AS build

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm run build

FROM nginx:alpine

# Copy nginx config to handle SPA routing
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy built application
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 5000

CMD ["nginx", "-g", "daemon off;"]