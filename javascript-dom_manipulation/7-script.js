document.addEventListener('DOMContentLoaded', function () {
	const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

	fetch(url)
		.then(response => response.json())
		.then(data => {
			const listMovies = document.getElementById('list_movies');

			data.results.forEach(movie => {
				const movieItem = document.createElement('li');
				movieItem.textContent = movie.title;
				listMovies.appendChild(movieItem);
			});
		})
		.catch(error => {
			console.error('Error fetching movies:', error);
		});
});
