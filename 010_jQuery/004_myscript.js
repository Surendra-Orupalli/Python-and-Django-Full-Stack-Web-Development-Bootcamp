$('input').eq(0).keypress(function(){
  if(event.which === 13){
    $('h3').toggleClass('turnBlue')
  }
})
