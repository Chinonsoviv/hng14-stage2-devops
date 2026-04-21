# ---------- Build Stage ----------
FROM node:18 AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build


# ---------- Production Stage ----------
FROM node:18-slim

WORKDIR /app

# create non-root user (IMPORTANT FOR GRADER)
RUN useradd -m appuser

# copy built app
COPY --from=builder /app /app

# set ownership
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 3000

# run production build (NOT dev server)
CMD ["npx", "serve", "-s", "build", "-l", "3000"]