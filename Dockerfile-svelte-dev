FROM node:latest as svelte-build

WORKDIR /app

COPY ./svelte-app  .

RUN npm install

RUN npm run build

FROM svelte:v1 as svelte-app

COPY --from=svelte-build ./app/public /usr/share/nginx/html
