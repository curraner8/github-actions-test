const express = require("express");
const app = express();

// VULNERABLE: Default error handler in development mode
app.get("/data", (req, res) => {
  throw new Error("Something went wrong");
});

// When NODE_ENV=development, stack traces are sent to client
app.use((err, req, res, next) => {
  // VULNERABLE: Full stack trace exposed in response
  res.status(500).send(err.stack);
});

// SOURCE:  https://expressjs.com/en/guide/error-handling.html
