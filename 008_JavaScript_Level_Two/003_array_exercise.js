roster = [];
console.log(roster);


function addName(){
  var add = prompt("Add student name: ");
  roster.push(add);
}


function remName(){
  var remove = prompt("Remove student name: ");
  index = roster.indexOf(remove);
  roster.splice(index, 1);
}


function disNames(){
  console.log(roster);
}

var request = ""
while(request !== "quit"){
  request = prompt("Choose an action - add / remove / display / quit");

  if(request==="add"){
    addName();
  }

  else if(request==="remove"){
    remName();
  }

  else if(request==="display"){
    disNames()
  }

  else{
    alert("Not recognized!")
  }

}
