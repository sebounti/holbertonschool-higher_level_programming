document.addEventListener('DOMContentLoaded', function () {
  // Sélectionner l'élément avec l'ID character
  let characterElement = document.getElementById('character');

  // URL de l'API
  let apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  // Utiliser l'API Fetch pour obtenir les données JSON
  fetch(apiUrl)
    .then(function (response) {
      // Vérifier si la réponse est réussie (statut 200)
      if (response.status === 200) {
        // Analyser la réponse JSON
        return response.json();
      } else {
        // Gérer les erreurs de réponse
        throw new Error('Erreur lors de la récupération des données');
      }
    })
    .then(function (data) {
      // Récupérer le nom du personnage depuis les données JSON
      let characterName = data.name;

      // Afficher le nom du personnage dans l'élément character
      characterElement.textContent = characterName;
    })
    .catch(function (error) {
      // Gérer les erreurs
      console.error('Erreur Fetch:', error);
    });
});
