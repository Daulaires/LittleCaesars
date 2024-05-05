// when the button id RandomAccount is pressed then generate a random account by making a post request to the create_account_with_random_data

document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('RandomAccount');
    const body = document.body;

    toggleButton.addEventListener('click', function () {
            // Construct the URL for the GET request
            const url = '/create_account_with_random_data';
            // Create a new XMLHttpRequest object
            const request = new XMLHttpRequest();
            // Configure it: GET-request for the URL /article/.../load
            request.open('GET', url, true);
            // Send the request over the network
            request.send();
            // This will be called after the response is received
            request.onload = function () {
                if (request.status === 200) {
                    // If the request was successful, update the page
                    showNotification('Account created');
                } else {
                    // If the request was unsuccessful, log the error
                    showNotification('Account creation failed');
                }
            };
    });
});