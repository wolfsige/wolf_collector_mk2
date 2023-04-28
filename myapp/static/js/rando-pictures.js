const srcArray = ['../static/img/wolf1.jpg', '../static/img/wolf2.jpg', '../static/img/wolf3.jpg', '../static/img/wolf4.jpg', '../static/img/wolf5.jpg', '../static/img/wolf6.jpg', '../static/img/wolf7.jpg']


Array.from(document.querySelectorAll('.random-wolf')).forEach(imgEl => {

  const randomIndex = Math.floor(Math.random()*srcArray.length);
  
  imgEl.src = srcArray[randomIndex];

})