document.addEventListener('DOMContentLoaded', function() {
    const menuToggleButton = document.getElementById('menuToggle');
    const menu = document.getElementById('menu');

    // Function to update the button text based on the current visibility of the menu
    function updateButtonText() {
        if (menu.style.display === 'none') {
            menuToggleButton.textContent = 'Show Menu';
        } else {
            menuToggleButton.textContent = 'Hide Menu';
        }
    }

    // Initial call to set the correct text on page load
    updateButtonText();
    
    menuToggleButton.addEventListener('click', function() {
        if (menu.style.display === 'none') {
            menu.style.display = 'block';
        } else {
            menu.style.display = 'none';
        }
        // Update the button text after toggling the menu's visibility
        updateButtonText();
    });

});
