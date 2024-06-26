document.addEventListener('DOMContentLoaded', function () {

    const toggleSpamFormButton = document.getElementById('toggleSpamForm');
    const SpamFormElement = document.getElementById('spamForm');

    // Function to update the button text based on the current visibility of the form
    function updateButtonText() {
        if (SpamFormElement.style.display === 'none') {
            toggleSpamFormButton.textContent = 'Show Spam Form';
        } else {
            toggleSpamFormButton.textContent = 'Hide Spam Form';
        }
    }

    // Initial call to set the correct text on page load
    updateButtonText();

    toggleSpamFormButton.addEventListener('click', function () {
        if (SpamFormElement.style.display === 'none') {
            // remove hide
            SpamFormElement.classList.remove('hide');
            SpamFormElement.style.display = 'block';
        } else {
            setTimeout(function () {
                SpamFormElement.classList.add('hide');
            }, 500);
            setTimeout(function () {
                SpamFormElement.style.display = 'none';
            }, 1000);
        }
        // Update the button text after toggling the form's visibility
        setTimeout(function () {
            updateButtonText();
        }, 1000);
    });

});
