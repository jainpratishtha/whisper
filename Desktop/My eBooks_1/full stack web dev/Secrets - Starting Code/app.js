//jshint esversion:6
require("dotenv").config();
const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const ejs = require("ejs");
const encrypt= require("mongoose-encryption");

// const _ = require('lodash');

const app = express();

// console.log(process.env.SECRET);

app.set("view engine", "ejs"); //view engine will use ejs as we are templating
app.use(bodyParser.urlencoded({
  extended: true
})); //bpdy parser tp parse our request
app.use(express.static("public"));

mongoose.connect("mongodb://localhost:27017/userDB", {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

const userSchema = new mongoose.Schema({
  email: String,
  password: String
});


//plugins are used to extend the functionalities of the mongoose schema
userSchema.plugin(encrypt,{secret:process.env.SECRET, encryptedFields:["password"]});//uses AES encryption method
// This adds _ct and _ac fields to the schema, as well as pre 'init' and pre 'save' middleware,
// and encrypt, decrypt, sign, and authenticate instance methods
//mongoose will encryot when the save command will run and will decrypt when find command is run
const User = mongoose.model("User", userSchema);

app.get("/", function(req, res) {
  res.render("home");
});

app.route("/login").get(function(req, res) {
    res.render("login");
  })
  .post(function(req, res) {
    const username = req.body.username;
    const password = req.body.password;
    User.findOne({
      email: username
    }, function(err, found) {
      if (err) {
        console.log(err);
      } else if (found) {
        if (found.password === password) {
          res.render("secrets");
        } else {
          res.render("username or password incorrect");
        }
      } else {
        res.render("username or password incorrect");
      }
    });
  });
app.route("/register").get(function(req, res) {
    res.render("register");
  })
  .post(function(req, res) {
    const newuser = new User({
      email: req.body.username,
      password: req.body.password
    });
    newuser.save(function(err) {
      if (err) {
        console.log(err);
      } else {
        res.render("secrets");
      }
    });
  });
app.listen("3000", function() {
  console.log("server has started on port 3000");

});
