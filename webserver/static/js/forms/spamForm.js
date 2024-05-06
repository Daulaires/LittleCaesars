document.getElementById('spamForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const formData = new FormData(this);
    const email = formData.get('email');
    const times = formData.get('times');

    // Construct the URL for the POST request
    const url = '/v1/spam'; // Assuming the Flask app is running on the same domain

    // Prepare the request body
    const requestBody = JSON.stringify({
        email: email,
        times: times
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
                showNotification(email + ' ' + times + ' times', 'Success');
                return response.json();
            } else {
                const text = await response.text();
                showNotification('Error: ' + text, 'Error', document.body);
                throw new Error(text);
            }
        })
});

