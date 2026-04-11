const crypto = require('crypto');

// VULNERABLE: MD5 is completely broken for security
const md5Hash = crypto.createHash('md5').update(password).digest('hex');

// VULNERABLE: SHA1 is also weak for password storage
const sha1Hash = crypto.createHash('sha1').update(password).digest('hex');

// VULNERABLE: SHA256 is fast - BAD for passwords (attackers compute billions/sec)
const sha256Hash = crypto.createHash('sha256').update(password).digest('hex');

// SOURCE: https://www.praetorian.com/blog/secure-password-storage-in-go-python-ruby-java-haskell-and-nodejs
