// Sélectionne l'élément avec l'ID 'red_header'
let redHeader = document.getElementById("red_header");

// Sélectionne l'élément 'header'
let header = document.querySelector("header");

// Attache un gestionnaire d'événements au clic sur 'red_header'
redHeader.addEventListener("click", function() {
  // Ajoute la classe 'red' à l'élément 'header'
  header.classList.add("red");
});
