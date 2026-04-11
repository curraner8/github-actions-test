// VULNERABLE: Math.random() uses java.util.Random (weak PRNG)
String generatePasswordResetToken() {
    return Long.toHexString(Double.doubleToLongBits(Math.random()));
}

// SOURCE:  https://owasp.org/www-community/vulnerabilities/Insecure_Randomness
