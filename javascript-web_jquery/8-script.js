$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const movies = data.results;
    const ulElement = $('#list_movies');

    movies.forEach(function (movie) {
      $('<li>' + movie.title + '</li>').appendTo(ulElement);
    });
  });
});
