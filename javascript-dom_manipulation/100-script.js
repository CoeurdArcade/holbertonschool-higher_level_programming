const addButton = document.querySelector('#add_item');
const removeButton = document.querySelector('#remove_item');
const clearButton = document.querySelector('#clear_list');

addButton.addEventListener('click', () => addLI());
removeButton.addEventListener('click', () => removeLI());
clearButton.addEventListener('click', () => clearLI());

function addLI () {
  const element = document.querySelector('.my_list');
  const newLI = document.createElement('LI');
  const text = document.createTextNode('Item');

  newLI.appendChild(text);
  element.appendChild(newLI);
}

function removeLI () {
  const element = document.querySelector('.my_list');
  element.removeChild(element.lastChild);
}

function clearLI () {
  const element = document.querySelector('.my_list');
  while (element.hasChildNodes()) {
    element.removeChild(element.lastChild);
  }
}
