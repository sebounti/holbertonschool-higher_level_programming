document.addEventListener('DOMContentLoaded', function () {
  // Sélectionner l'élément avec l'ID list_movies
  let listMoviesElement = document.getElementById('list_movies');

  // URL de l'API
  let apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

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
      // Récupérer la liste des films depuis les données JSON
      let movies = data.results;

      // Parcourir la liste des films et ajouter chaque titre à la liste HTML
      movies.forEach(function (movie) {
        let title = movie.title;
        let listItem = document.createElement('li');
        listItem.textContent = title;
        listMoviesElement.appendChild(listItem);
      });
    })
    .catch(function (error) {
      // Gérer les erreurs
      console.error('Erreur Fetch:', error);
    });
});
