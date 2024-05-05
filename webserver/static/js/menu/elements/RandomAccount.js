// when the button id RandomAccount is pressed then generate a random account by making a post request to the create_account_with_random_data

document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('RandomAccount');
    const body = document.body;

    toggleButton.addEventListener('click', function () {
            // Construct the URL for the GET request
            const url = '/v1/create_account_with_random_data';
            // Make the GET request
            fetch(url, {
                method: 'GET'
            })
                .then(response => response.json()) // Parse the response as JSON
                .then(data => showNotification(data.status === 'success' ? data.message : 'An error occurred. Please try again.'))
                .catch(error => showNotification('An error occurred. Please try again.'));
    });
});