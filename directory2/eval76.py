function onCaptchaResult(result) {
    eval(result); // Direct execution of attacker-controlled input
}

# SOURCE:  https://github.com/pyload/pyload/security/advisories/GHSA-8w3f-4r8f-pf53
