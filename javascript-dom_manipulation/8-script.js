document.addEventListener('DOMContentLoaded', function () {
  // Sélectionner l'élément avec l'ID hello
  let helloElement = document.getElementById('hello');

  // URL de l'API
  let apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Utiliser l'API Fetch pour obtenir les données texte
  fetch(apiUrl)
    .then(function (response) {
      // Vérifier si la réponse est réussie (statut 200)
      if (response.status === 200) {
        // Obtenir le texte de la réponse
        return response.text();
      } else {
        // Gérer les erreurs de réponse
        throw new Error('Erreur lors de la récupération des données');
      }
    })
    .then(function (text) {
      // Afficher le texte de la réponse dans l'élément avec l'ID hello
      helloElement.textContent = text;
    })
    .catch(function (error) {
      // Gérer les erreurs
      console.error('Erreur Fetch:', error);
    });
});
