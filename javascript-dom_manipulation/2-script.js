const redHeaderButton = document.getElementById('red_header');

redHeaderButton.addEventListener('click', function() {
	const headerElement = document.querySelector('header');
	headerElement.classList.add('red');
});
