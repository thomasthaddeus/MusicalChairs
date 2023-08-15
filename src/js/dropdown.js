// Function to toggle the visibility of the dropdown content
function toggleDropdown(event) {
    var dropdownContent = event.target.nextElementSibling;
    if (dropdownContent.style.display === 'none' || !dropdownContent.style.display) {
        dropdownContent.style.display = 'block';
    } else {
        dropdownContent.style.display = 'none';
    }
}

// Attach the toggle function to the dropdown triggers
var dropdownTriggers = document.querySelectorAll('.dropdown-trigger');
dropdownTriggers.forEach(function(trigger) {
    trigger.addEventListener('click', toggleDropdown);
});

// Listen for clicks on the entire document to close the dropdown if clicked outside
document.addEventListener('click', function(event) {
    var isClickInside = document.querySelector('.dropdown').contains(event.target);
    if (!isClickInside) {
        var dropdowns = document.querySelectorAll('.dropdown-content');
        dropdowns.forEach(function(dropdown) {
            dropdown.style.display = 'none';
        });
    }
});
