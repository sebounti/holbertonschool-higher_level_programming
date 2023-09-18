//document.addEventListener('DOMContentLoaded', function () {
  // Sélectionner l'élément avec l'ID update_header
 // let updateHeader = document.getElementById('update_header');

  // Sélectionner l'élément de l'en-tête
  //let headerElement = document.querySelector('header');

  // Ajouter un gestionnaire d'événements de clic à l'élément update_header
  //updateHeader.addEventListener('click', function () {
    // Mettre à jour le texte de l'élément de l'en-tête
  //  headerElement.textContent = 'New Header!!!';
  //});
//});
$('#update_header').click(function () {
  $('header').text('New Header!!!');
});
