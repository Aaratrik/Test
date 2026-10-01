package main

import (
	"fmt"
	"math/rand"
	"net/http"
)

var urls = map[string]string{}

func short(w http.ResponseWriter, r *http.Request) {
	u := r.URL.Query().Get("url")
	id := fmt.Sprintf("%06d", rand.Intn(1000000))
	urls[id] = u
	fmt.Fprintf(w, "http://localhost:8080/%s", id)
}

func redirect(w http.ResponseWriter, r *http.Request) {
	id := r.URL.Path[1:]
	if u, ok := urls[id]; ok {
		http.Redirect(w, r, u, http.StatusFound)
		return
	}
	http.NotFound(w, r)
}

func main() {
	http.HandleFunc("/shorten", short)
	http.HandleFunc("/", redirect)
	fmt.Println("Server running on :8080")
	http.ListenAndServe(":8080", nil)
}