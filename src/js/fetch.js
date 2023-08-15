// Fetch the README content
fetch('https://apparellnstuff.me/musical-chairs/README.md')
    .then(response => response.text())
    .then(data => {
        // Get the placeholder element
        const readmeContent = document.getElementById('readmeContent');

        // Insert the README content into the placeholder
        readmeContent.innerHTML = data;
    })
    .catch(error => {
        console.error('Error fetching README:', error);
    });
