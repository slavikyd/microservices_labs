package handlers

import (
	"encoding/json"
	"math/rand"
	"net/http"
	"time"

	"github.com/gorilla/mux"
)

type Phone struct {
	Number string `json:"number"`
}

type Contact struct {
	ID         int       `json:"id"`
	Username   string    `json:"username"`
	GivenName  string    `json:"given_name"`
	FamilyName string    `json:"family_name"`
	Phone      *Phone    `json:"phone"`
	Email      string    `json:"email"`
	Birthdate  time.Time `json:"birthdate"`
}

type Group struct {
	ID          int    `json:"id"`
	Title       string `json:"title"`
	Description string `json:"description"`
	Contacts    []int  `json:"contacts"`
}

func SetupRouter(router *mux.Router) {
	router.HandleFunc("/api/v1/contact", getContacts).Methods("GET")
	router.HandleFunc("/api/v1/contact", createContact).Methods("POST")
	router.HandleFunc("/api/v1/contact", updateContact).Methods("PUT")
	router.HandleFunc("/api/v1/contact", deleteContact).Methods("DELETE")
	router.HandleFunc("/api/v1/group", getGroups).Methods("GET")
	router.HandleFunc("/api/v1/group", createGroup).Methods("POST")
	router.HandleFunc("/api/v1/group", updateGroup).Methods("PUT")
	router.HandleFunc("/api/v1/group", deleteGroup).Methods("DELETE")
}

func getContacts(w http.ResponseWriter, r *http.Request) {
	contact := Contact{
		ID:         rand.Intn(1000),
		Username:   "testuser",
		GivenName:  "Test",
		FamilyName: "User",
		Phone:      &Phone{Number: "+1234567890"},
		Email:      "test@example.com",
		Birthdate:  time.Now(),
	}

	w.Header().Set("Content-Type", "application/json")
	if err := json.NewEncoder(w).Encode(contact); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func createContact(w http.ResponseWriter, r *http.Request) {
	var contact Contact
	if err := json.NewDecoder(r.Body).Decode(&contact); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(contact)
}

func updateContact(w http.ResponseWriter, r *http.Request) {
	var contact Contact
	if err := json.NewDecoder(r.Body).Decode(&contact); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(contact)
}

func deleteContact(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusNoContent)
}

func getGroups(w http.ResponseWriter, r *http.Request) {
	group := Group{
		ID:          rand.Intn(1000),
		Title:       "Sample Group",
		Description: "This is a sample group",
		Contacts:    []int{rand.Intn(1000), rand.Intn(1000), rand.Intn(1000)},
	}

	w.Header().Set("Content-Type", "application/json")
	if err := json.NewEncoder(w).Encode(group); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func createGroup(w http.ResponseWriter, r *http.Request) {
	var group Group
	if err := json.NewDecoder(r.Body).Decode(&group); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	group.ID = rand.Intn(1000)

	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(group)
}

func updateGroup(w http.ResponseWriter, r *http.Request) {
	var group Group
	if err := json.NewDecoder(r.Body).Decode(&group); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(group)
}

func deleteGroup(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusNoContent)
}
