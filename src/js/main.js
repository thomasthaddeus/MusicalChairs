// --------------------- myModal.js ---------------------
function initializeModal() {
    const modal = document.getElementById('myModal');
    const openBtn = document.getElementById('openModal');
    const closeBtn = document.getElementById('closeModal');

    openBtn.addEventListener('click', () => {
        modal.style.display = 'block';
    });

    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });
}

// --------------------- accordion.js ----------------------------
function initializeAccordion() {
    const accordions = document.querySelectorAll('.accordion');

    accordions.forEach(accordion => {
        accordion.addEventListener('click', function() {
            this.classList.toggle('active');
            const content = this.nextElementSibling;
            if (content.style.display === 'block') {
                content.style.display = 'none';
            } else {
                content.style.display = 'block';
            }
        });
    });
}

// --------------------- displayReadme.js ---------------------
function displayReadme() {
    const README_URL = "https://raw.githubusercontent.com/thomasthaddeus/musical-chairs/main/README.md";

    fetch(README_URL)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.text();
        })
        .then(data => {
            const htmlContent = markdownToHtml(data);
            document.getElementById("readmeContent").innerHTML = htmlContent;
        })
        .catch(error => {
            console.log("There was a problem with the fetch operation:", error.message);
        });
}

function markdownToHtml(markdown) {
    return marked.parse(markdown);
}

// --------------------- dropdown.js ---------------------
function initializeDropdown() {
    var dropdownTriggers = document.querySelectorAll('.dropdown-trigger');
    dropdownTriggers.forEach(function(trigger) {
        trigger.addEventListener('click', toggleDropdown);
    });

    document.addEventListener('click', function(event) {
        var isClickInside = document.querySelector('.dropdown').contains(event.target);
        if (!isClickInside) {
            var dropdowns = document.querySelectorAll('.dropdown-content');
            dropdowns.forEach(function(dropdown) {
                dropdown.style.display = 'none';
            });
        }
    });
}

function toggleDropdown(event) {
    var dropdownContent = event.target.nextElementSibling;
    if (dropdownContent.style.display === 'none' || !dropdownContent.style.display) {
        dropdownContent.style.display = 'block';
    } else {
        dropdownContent.style.display = 'none';
    }
}

// --------------------- fetch.js ---------------------
function fetchReadme() {
    fetch('https://raw.githubusercontent.com/thomasthaddeus/musical-chairs/main/README.md')
        .then(response => response.text())
        .then(data => {
            const readmeContent = document.getElementById('readmeContent');
            readmeContent.innerHTML = data;
        })
        .catch(error => {
            console.error('Error fetching README:', error);
        });
}

// --------------------- smooth_scrolling.js ---------------------
function initializeSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
}

// Initialize all functions when the document is loaded
document.addEventListener("DOMContentLoaded", function() {
    initializeModal();
    initializeAccordion();
    displayReadme();
    initializeDropdown();
    fetchReadme();
    initializeSmoothScrolling();
});
