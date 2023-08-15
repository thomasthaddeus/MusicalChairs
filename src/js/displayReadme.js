// displayReadme.js
document.addEventListener("DOMContentLoaded", function() {
    // Define the URL where the README content is hosted
    const README_URL = "https://raw.githubusercontent.com/thomasthaddeus/musical-chairs/main/README.md";

    // Fetch the README content
    fetch(README_URL)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.text();
        })
        .then(data => {
            // Convert markdown to HTML (assuming you have a markdown-to-HTML converter function)
            const htmlContent = markdownToHtml(data);

            // Insert the HTML content into a designated element on the webpage
            document.getElementById("readmeContent").innerHTML = htmlContent;
        })
        .catch(error => {
            console.log("There was a problem with the fetch operation:", error.message);
        });
});

function markdownToHtml(markdown) {
    return marked(markdown);
}
