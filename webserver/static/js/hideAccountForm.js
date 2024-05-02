document.addEventListener('DOMContentLoaded', function() {
    const toggleCreateAccountFormButton = document.getElementById('toggleCreateAccountForm');
    const createAccountForm = document.getElementById('createAccountForm');

    toggleCreateAccountFormButton.addEventListener('click', function() {
        if (createAccountForm.style.display === 'none') {
            createAccountForm.style.display = 'block';
        } else {
            createAccountForm.style.display = 'none';
        }
    });
});
