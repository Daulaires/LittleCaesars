document.addEventListener('DOMContentLoaded', function () {
    const toggleCreateAccountFormButton = document.getElementById('toggleCreateAccountForm');
    const createAccountFormElement = document.getElementById('createAccountForm');

    // Function to update the button text based on the current visibility of the form
    function updateButtonText() {
        if (createAccountFormElement.style.display === 'none') {
            toggleCreateAccountFormButton.textContent = 'Show Create Account';
        } else {
            toggleCreateAccountFormButton.textContent = 'Hide Create Account';
        }
    }

    // Initial call to set the correct text on page load
    updateButtonText();

    toggleCreateAccountFormButton.addEventListener('click', function () {
        if (createAccountFormElement.style.display === 'none') {
            // remove hide
            createAccountFormElement.classList.remove('hide');
            createAccountFormElement.style.display = 'block';
        } else {
            setTimeout(function () {
                createAccountFormElement.classList.add('hide');
            }, 500);
            setTimeout(function () {
                createAccountFormElement.style.display = 'none';
            }, 1000);
        }
        // Update the button text after toggling the form's visibility
        setTimeout(function () {
            updateButtonText();
        }, 1000);
    });
});
