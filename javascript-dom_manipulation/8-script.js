document.addEventListener("DOMContentLoaded", function() {
	const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

	fetch(url)
		.then(response => response.json())
		.then(data => {
			const helloDiv = document.getElementById('hello');
			helloDiv.textContent = data.hello;
		})
		.catch(error => {
			console.error('Error fetching the greeting:', error);
		});
});
