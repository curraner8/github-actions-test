// User input determines which module gets loaded
const moduleName = req.query.module;
const maliciousModule = require(moduleName); // DANGEROUS

// SOURCE:  https://raven.io/blog/why-static-analysis-falls-short-in-dynamic-programming-languages
