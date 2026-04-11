package main

import (
    "net/http"
)

func redirectHandler(w http.ResponseWriter, r *http.Request) {
    nextURL := r.URL.Query().Get("next")
    // VULNERABLE: net/http does NOT automatically sanitize headers
    // Attacker input: "https://example.com\r\nX-Injected: evil"
    w.Header().Set("Location", nextURL)
    w.WriteHeader(http.StatusFound)
}

func searchHandler(w http.ResponseWriter, r *http.Request) {
    query := r.URL.Query().Get("q")
    // VULNERABLE: User input directly in custom header
    w.Header().Set("X-Search-Result", query)
    w.WriteHeader(http.StatusOK)
}

// SOURCE: PHP.cn - Go HTTP Header Injection Defens
