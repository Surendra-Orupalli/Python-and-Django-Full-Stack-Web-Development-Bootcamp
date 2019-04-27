var fname = prompt("Please enter your first name: ")
var lname = prompt("Please enter your last name: ")
var age = prompt("Please enter your age: ")
var ht = prompt("Please enter your height: ")
var pname = prompt("Please enter your pet name: ")
alert("Thank you so much for the information!")

if (fname[0]===lname[0] && age>20 && age<30 && ht>170 && pname[pname.length-1]==="y") {
  console.log("Welcome to the SpyWorld!");
} else {
  console.log("There is nothing you get here!");
}
