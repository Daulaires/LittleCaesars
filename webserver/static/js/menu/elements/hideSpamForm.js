document.addEventListener('DOMContentLoaded', function () {

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

    toggleCreateAccountFormButton.addEventListener('click', function () {
        if (createAccountForm.style.display === 'none') {
            // remove hide
            createAccountForm.classList.remove('hide');
            createAccountForm.style.display = 'block';
        } else {
            setTimeout(function () {
                createAccountForm.classList.add('hide');
            }, 500);
            setTimeout(function () {
                createAccountForm.style.display = 'none';
            }, 1000);
        }
        // Update the button text after toggling the form's visibility
        setTimeout(function () {
            updateButtonText();
        }, 1000);
    });

});
