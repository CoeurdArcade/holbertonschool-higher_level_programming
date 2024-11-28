const redHeaderButton = document.getElementById('red_header');

redHeaderButton.addEventListener('click', function() {
	const headerElement = document.querySelector('header');
	headerElement.style.color = '#FF0000';
});
