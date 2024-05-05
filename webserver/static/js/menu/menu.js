document.addEventListener('DOMContentLoaded', function () {
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

    menuToggleButton.addEventListener('click', function () {
        if (menu.style.display === 'none') {
            setTimeout(function () {
                menu.classList.remove('hide');
                menu.classList.add('show');
                menu.style.display = 'block';
            }, 100);
        } else {
            setTimeout(function () {
                menu.classList.add('hide');
            }, 500);
            setTimeout(function () {
                menu.style.display = 'none';
            }, 1000);
        }
        // Update the button text after toggling the form's visibility
        setTimeout(function () {
            updateButtonText();
        }, 1000);
    });

});
