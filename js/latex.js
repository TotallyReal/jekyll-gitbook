// Function to fetch the text file
fetch('../pages/preamble.sty')
    .then(response => response.text())
    .then(data => {
        // Create a new div element
        var divElement = document.createElement('div');

        // Set the id and style attributes of the div
        divElement.id = 'hiddenDiv';
        divElement.style.display = 'none';

        // Set the innerHTML of the div to the content of the text file
        divElement.innerHTML  = data;

        // Append the div to the body of the HTML document
        document.body.appendChild(divElement);
    })
    .catch(error => {
        console.error('Error fetching text file:', error);
    });