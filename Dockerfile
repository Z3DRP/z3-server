FROM golang:1.23.0-alpine AS build

WORKDIR /app

COPY cmd/main.go .
COPY dist ./dist

RUN GOOS=linux GOARCH=amd64 go build -o server main.go

FROM alpine:latest

WORKDIR /app

COPY --from=build /app/server .
COPY --from=build /app/dist ./dist

RUN chmod +x /app/server

EXPOSE 3000

CMD ["./server"]
