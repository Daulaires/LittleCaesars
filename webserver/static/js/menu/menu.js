document.addEventListener('DOMContentLoaded', function () {
    const menuToggleButton = document.getElementById('menuToggle');
    const menuContainer = document.getElementById('menu');

    // Function to update the button text based on the current visibility of the menu
    function updateButtonText() {
        if (menuContainer.style.display === 'none') {
            menuToggleButton.textContent = 'Show Menu';
        } else {
            menuToggleButton.textContent = 'Hide Menu';
        }
    }

    // Function to show the menu
    function showMenu() {
        setTimeout(function () {
            menuContainer.classList.remove('hide');
            menuContainer.classList.add('show');
            menuContainer.style.display = 'block';
        }, 100);
    }

    // Function to hide the menu
    function hideMenu() {
        setTimeout(function () {
            menuContainer.classList.add('hide');
        }, 500);
        setTimeout(function () {
            menuContainer.style.display = 'none';
        }, 1000);
    }

    // Function to handle the menu toggle button click event
    function handleMenuToggle() {
        if (menuContainer.style.display === 'none') {
            showMenu();
        } else {
            hideMenu();
        }
        // Update the button text after toggling the form's visibility
        setTimeout(function () {
            updateButtonText();
        }, 1000);
    }

    // Initial call to set the correct text on page load
    updateButtonText();

    // Add event listener to the menu toggle button
    menuToggleButton.addEventListener('click', handleMenuToggle);
});
