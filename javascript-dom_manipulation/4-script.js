document.addEventListener('DOMContentLoaded', function () {
  // Sélectionner l'élément avec l'ID add_item
  let addItem = document.getElementById('add_item');

  // Sélectionner la liste ul avec la classe my_list
  let myList = document.querySelector('.my_list');

  // Ajouter un gestionnaire d'événements de clic à l'élément add_item
  addItem.addEventListener('click', function () {
    // Créer un nouvel élément li
    let newItem = document.createElement('li');

    // Définir le texte de l'élément li
    newItem.textContent = 'Item';

    // Ajouter l'élément li à la liste ul
    myList.appendChild(newItem);
  });
});
