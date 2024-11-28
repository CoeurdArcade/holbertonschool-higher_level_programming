document.addEventListener('DOMContentLoaded', function() {
	const btnTranslate = document.getElementById('btn_translate');
	btnTranslate.addEventListener('click', function() {
		const languageCode = document.getElementById('language_code').value;
		const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

		fetch(url)
			.then(response => reponse.json())
			.then(data => {
				const helloDiv = document.getElementById('hello');
				helloDiv.textContent = data.hello;
			})
			.catch(error => {
				console.error('Error fetching the greeting:', error);
			});
	});
});
