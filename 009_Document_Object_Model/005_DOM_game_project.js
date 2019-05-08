var restart = document.querySelector("#b");
var boxes = document.querySelectorAll("td");

function cleanBoard(){
for (var i = 0; i < boxes.length; i++) {
  boxes[i].textContent = '';
}
}

restart.addEventListener('click',cleanBoard)

function putMark(){
  if(this.textContent === ''){
    this.textContent = 'X';
  }
  else if(this.textContent === 'X'){
    this.textContent = 'O';
  }
  else {
    this.textContent = '';
  }
};


for (var i = 0; i < boxes.length; i++) {
  boxes[i].addEventListener('click', putMark);
}
