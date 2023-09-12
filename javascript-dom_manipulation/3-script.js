document.addEventListener("DOMContentLoaded", function () {
  // Sélectionner les éléments nécessaires
  let toggleHeader = document.getElementById('toggle_header');
  let header = document.querySelector('header');

  // Ajouter un gestionnaire d'événements de clic à l'élément toggle_header
  toggleHeader.addEventListener("click", function () {
    // Vérifier la classe actuelle de l'élément header
    if (header.classList.contains("red")) {
      // Si la classe est "red", la remplacer par "green"
      header.classList.remove("red");
      header.classList.add("green");
    } else {
      // Sinon, si la classe est "green", la remplacer par "red"
      header.classList.remove("green");
      header.classList.add("red");
    }
  });
});
