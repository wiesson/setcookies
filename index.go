package IndexHandler

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"strconv"
	"time"
)

// addCookie will apply a new cookie to the response of a http
// request, with the key/value this method is passed.
func addCookie(w http.ResponseWriter, name string, value string) {
	expire := time.Now().AddDate(0, 1, 0)
	cookie := http.Cookie{
		Name:    name,
		Value:   value,
		Expires: expire,
		Secure:  true,
	}
	http.SetCookie(w, &cookie)
}

func IndexHandler(w http.ResponseWriter, req *http.Request) {
	visits := 0
	lastVisit := ""

	for _, cookie := range req.Cookies() {
		if cookie.Name == "visits" {
			val, err := strconv.Atoi(cookie.Value)
			if err != nil {
				visits = 0
				continue
			}

			visits = val + 1
		}

		if cookie.Name == "last_visit" {
			lastVisit = cookie.Value
		}
		log.Println("Cookie: ", cookie.Name, cookie.Value)
	}

	addCookie(w, "last_visit", time.Now().Format(time.RFC3339))
	addCookie(w, "visits", strconv.Itoa(visits))

	responseStr := fmt.Sprintf("Hello, you have visited this page %d times.", visits)

	if lastVisit != "" {
		responseStr = responseStr + fmt.Sprintf(" Your last visit was on %s.", lastVisit)
	}

	io.WriteString(w, responseStr)
}

func main() {
	http.HandleFunc("/", IndexHandler)
	http.ListenAndServe(":8080", nil)
}
