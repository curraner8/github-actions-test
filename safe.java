func pingHandler(ip string) {
    cmd := exec.Command("ping", "-c", "4", ip) // Safe
    cmd.Run()
}
