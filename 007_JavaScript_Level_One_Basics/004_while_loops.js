var x = 0;

while (x<5) {
  console.log("x is currently: " + x);

  if (x===3) {
    console.log("X IS EQUAL TO 3");
    break;
  }
  console.log("x is still less than 5, adding 1 to x");
  x = x+1;

}

var a = 2;

while (a<=10) {
  console.log(a)
  a = a+2
}


var a = 1;

while (a<=10) {
  if (a%2===0) {
    console.log(a)
  }
  a = a+1
}
