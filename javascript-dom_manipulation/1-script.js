// Sélectionne l'élément avec l'ID 'red_header'
let redHeader = document.getElementById("red_header");

//Sélectionne l'élément 'header'
let header = document.querySelector("header");

//Attache un gestionnaire d'événements au clic sur 'red_header'
redHeader.addEventListener("click", function() {
   //Modifie la couleur du texte du 'header' en rouge (#FF0000)
  header.style.color = "#FF0000";
});

//$('header').css('color', '#FF0000');
