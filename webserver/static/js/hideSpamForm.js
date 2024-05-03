document.addEventListener('DOMContentLoaded', function() {
    const toggleCreateAccountFormButton = document.getElementById('toggleSpamForm');
    const createAccountForm = document.getElementById('spamForm');

    // Function to update the button text based on the current visibility of the form
    function updateButtonText() {
        if (createAccountForm.style.display === 'none') {
            toggleCreateAccountFormButton.textContent = 'Show Spam Form';
        } else {
            toggleCreateAccountFormButton.textContent = 'Hide Spam Form';
        }
    }

    // Initial call to set the correct text on page load
    updateButtonText();

    toggleCreateAccountFormButton.addEventListener('click', function() {
        if (createAccountForm.style.display === 'none') {
            createAccountForm.style.display = 'block';
        } else {
            createAccountForm.style.display = 'none';
        }
        // Update the button text after toggling the form's visibility
        updateButtonText();
    });
});
