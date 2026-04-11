// Go equivalent pattern - debug flag enables privileged operations
var debug bool = false

func promoteRoot() {
    if debug {
        // Grant root/admin privileges for debugging
        // This should never be reachable in production
    }
}

func handleRequest(input string) {
    if strings.Contains(input, "-debug") {
        debug = true
        if strings.Contains(input, ":root") {
            promoteRoot()
        }
    }
}

// SOURCE:  https://samate.nist.gov/SARD/test-cases/2098/versions/1.0.0/files/src/main/java/LeftOverDebugCode_489.java
