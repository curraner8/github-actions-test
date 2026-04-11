const AdminJS = require("adminjs");
const AdminJSExpress = require("@adminjs/express");
const express = require("express");

const app = express();
const adminJs = new AdminJS({
  databases: [],
  rootPath: "/admin", // VULNERABLE: Admin panel exposed without auth
});

// VULNERABLE: No authentication middleware applied
const router = AdminJSExpress.buildRouter(adminJs);
app.use(adminJs.options.rootPath, router);
app.listen(8080);

// SOURCE: https://adminjs-docs.web.app/adminjs-expressjs_src_index.ts.html
