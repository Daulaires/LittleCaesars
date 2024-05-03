document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('themeToggle');
    const body = document.body;

    // Function to update the button text based on the current mode
    function updateButtonText() {
        if (body.classList.contains('dark-mode')) {
            toggleButton.textContent = 'Toggle Light Mode';
        } else {
            toggleButton.textContent = 'Toggle Dark Mode';
        }
    }

    // Initial call to set the correct text on page load
    updateButtonText();

    toggleButton.addEventListener('click', function() {
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
