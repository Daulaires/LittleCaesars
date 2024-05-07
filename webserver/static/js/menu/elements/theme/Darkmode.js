document.addEventListener('DOMContentLoaded', function () {
    const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const toggleButton = document.getElementById('themeToggle');
    const body = document.body;
    // Function to update the button text based on the current mode
    function updateButtonText() {
            // Set the initial theme based on the user's preference
        if (prefersDarkMode) {
            // remove the light-mode class if it exists
            body.classList.remove('light-mode');
            body.classList.add('dark-mode');
        } else {
            // remove the dark-mode class if it exists
            body.classList.remove('dark-mode');
            body.classList.add('light-mode');
        }
        if (body.classList.contains('dark-mode')) {
            toggleButton.textContent = 'Light Mode';
        } else {
            toggleButton.textContent = 'Dark Mode';
        }
    }

    // Initial call to set the correct text on page load
    updateButtonText();

    toggleButton.addEventListener('click', function () {
        if (body.classList.contains('dark-mode')) {
            body.classList.remove('dark-mode');
            body.classList.add('light-mode');
        } else {
            body.classList.remove('light-mode');
            body.classList.add('dark-mode');
        }
        // Update the button text after toggling the mode
        updateButtonText();
    });
});
