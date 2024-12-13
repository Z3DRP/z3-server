package main

import (
	"log"
	"net/http"
)

func main() {
	fs := http.FileServer(http.Dir("./dist"))

	http.Handle("/", fs)

	log.Println("Starting portfolio server..")
	if err := http.ListenAndServe(":3000", nil); err != nil {
		log.Fatal(err)
	}
}
