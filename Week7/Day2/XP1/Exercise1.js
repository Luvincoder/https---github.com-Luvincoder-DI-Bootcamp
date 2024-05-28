    
    const h1Element = document.querySelector('h1');
    console.log(h1Element.textContent);

    
    const article = document.getElementById('chocolateArticle');
    const paragraphs = article.getElementsByTagName('p');
    const lastParagraph = paragraphs[paragraphs.length - 1];
    article.removeChild(lastParagraph);

    
    const h2Element = document.querySelector('h2');
    h2Element.addEventListener('click', () => {
        h2Element.style.backgroundColor = 'red';
    });

    
    const h3Element = document.querySelector('h3');
    h3Element.addEventListener('click', () => {
        h3Element.style.display = 'none';
    });

    
    const boldButton = document.getElementById('boldButton');
    boldButton.addEventListener('click', () => {
        const allParagraphs = document.querySelectorAll('p');
        allParagraphs.forEach(paragraph => {
            paragraph.style.fontWeight = 'bold';
        });
    });

    
    h1Element.addEventListener('mouseenter', () => {
        const randomSize = Math.floor(Math.random() * 101); 
        h1Element.style.fontSize = randomSize + 'px';
    });

    
    const secondParagraph = paragraphs[1];
    secondParagraph.addEventListener('mouseenter', () => {
        secondParagraph.style.transition = 'opacity 0.5s';
        secondParagraph.style.opacity = 0;
    });
    secondParagraph.addEventListener('mouseleave', () => {
        secondParagraph.style.opacity = 1;
    });

// ---------------------------------------------------------

    document.addEventListener('DOMContentLoaded', function() {
        
        const userForm = document.getElementById('userForm');
        console.log(userForm);
    
        
        const firstNameInput = document.getElementById('fname');
        const lastNameInput = document.getElementById('lname');
        console.log(firstNameInput, lastNameInput);
    
        
        const firstNameByName = document.getElementsByName('firstname')[0];
        const lastNameByName = document.getElementsByName('lastname')[0];
        console.log(firstNameByName, lastNameByName);
    
        
        userForm.addEventListener('submit', function(event) {
        event.preventDefault(); 
    
    
        const firstNameValue = firstNameInput.value.trim();
        const lastNameValue = lastNameInput.value.trim();
    
        
        if (firstNameValue !== '' && lastNameValue !== '') {
            
            const firstNameLi = document.createElement('li');
            firstNameLi.textContent = firstNameValue;
            
            const lastNameLi = document.createElement('li');
            lastNameLi.textContent = lastNameValue;
    
            
            const usersAnswerList = document.querySelector('.usersAnswer');
            usersAnswerList.innerHTML = ''; 
            usersAnswerList.appendChild(firstNameLi);
            usersAnswerList.appendChild(lastNameLi);
        } else {
            alert('Please enter both first name and last name.');
        }
        });
    });

    let allBoldItems = [];

function getBoldItems() {
  // Collect all the bold items inside the paragraph
const paragraph = document.querySelector('p');
allBoldItems = Array.from(paragraph.querySelectorAll('strong'));
}

function highlight() {
  // Change the color of all bold text to blue
allBoldItems.forEach(item => {
    item.style.color = 'blue';
});
}

function returnItemsToDefault() {
  // Change the color of all bold text back to black
allBoldItems.forEach(item => {
    item.style.color = 'black'; });
}

document.addEventListener('DOMContentLoaded', function() {
  // Retrieve the form and console.log it
const userForm = document.getElementById('userForm');
console.log(userForm);

  // Retrieve the inputs by their id and console.log them
const firstNameInput = document.getElementById('fname');
const lastNameInput = document.getElementById('lname');
console.log(firstNameInput, lastNameInput);

  // Retrieve the inputs by their name attribute and console.log them
const firstNameByName = document.getElementsByName('firstname')[0];
const lastNameByName = document.getElementsByName('lastname')[0];
console.log(firstNameByName, lastNameByName);


userForm.addEventListener('submit', function(event) {
    event.preventDefault();

    
    const firstNameValue = firstNameInput.value.trim();
    const lastNameValue = lastNameInput.value.trim();

    
    if (firstNameValue !== '' && lastNameValue !== '') {
    
    const firstNameLi = document.createElement('li');
    firstNameLi.textContent = firstNameValue;
    
    const lastNameLi = document.createElement('li');
    lastNameLi.textContent = lastNameValue;

    const usersAnswerList = document.querySelector('.usersAnswer');
    usersAnswerList.innerHTML = ''; 
    usersAnswerList.appendChild(firstNameLi);
    usersAnswerList.appendChild(lastNameLi);
    } else {
    alert('Please enter both first name and last name.');
    }
});


getBoldItems();


const paragraph = document.querySelector('p');
paragraph.addEventListener('mouseover', highlight);
paragraph.addEventListener('mouseout', returnItemsToDefault);
});


document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the form and input elements
    const form = document.getElementById('MyForm');
    const radiusInput = document.getElementById('radius');
    const volumeInput = document.getElementById('volume');

    // Add submit event listener to the form
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        // Get the radius value and calculate the volume
        const radius = parseFloat(radiusInput.value);
        if (!isNaN(radius) && radius > 0) {
            const volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
            volumeInput.value = volume.toFixed(2); // Display the volume in the volume input field
        } else {
            alert('Please enter a valid radius');
        }
    });
});