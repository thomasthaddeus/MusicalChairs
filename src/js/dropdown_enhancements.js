document.addEventListener('click', function(event) {
    var isClickInside = document.querySelector('.dropdown').contains(event.target);
    if (!isClickInside) {
        var dropdowns = document.querySelectorAll('.dropdown-content');
        dropdowns.forEach(function(dropdown) {
            dropdown.style.display = 'none';
        });
    }
});
