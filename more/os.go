// VULNERABLE: User input passed to sh -c
cmd := exec.Command("sh", "-c", "git log --oneline "+commitRange)
cmd.Run()
