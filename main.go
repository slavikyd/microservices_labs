package main

import (
	"log"
	"net/http"

	"lab1/handlers"

	"github.com/gorilla/mux"
)

func main() {
	router := mux.NewRouter()
	handlers.SetupRouter(router)

	log.Println("Server is running on :8080")
	if err := http.ListenAndServe(":8080", router); err != nil {
		log.Fatalf("Error starting server: %v", err)
	}
}
