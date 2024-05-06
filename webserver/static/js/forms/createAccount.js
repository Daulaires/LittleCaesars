document.getElementById('createAccountForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const formData = new FormData(this);
    const email = formData.get('email');
    const password = formData.get('password');

    // Construct the URL for the POST request
    const url = '/v1/create'; // Assuming the Flask app endpoint for account creation

    // Prepare the request body
    const requestBody = JSON.stringify({
        email: email,
        password: password // Include 'password' if it's relevant for account creation
    });

    // Set the request headers
    const headers = {
        'Content-Type': 'application/json'
    };

    // Send the POST request to the Flask app
    fetch(url, {
        method: 'POST',
        headers: headers,
        body: requestBody
    })
        .then(async response => {
            if (response.ok) {
                showNotification('Account created for ' + email, 'Success');
                return response.json();
            } else {
                const text = await response.text();
                showNotification('Error: ' + text, 'Error');
                throw new Error(text);
            }
        })
});

