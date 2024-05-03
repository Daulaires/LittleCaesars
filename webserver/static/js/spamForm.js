document.getElementById('spamForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const formData = new FormData(this);
    const email = formData.get('email');
    const times = formData.get('times');

    // Construct the URL for the POST request
    const url = '/send_spam'; // Assuming the Flask app is running on the same domain

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
    .then(response => response.json()) // Parse the response as JSON
    .then(data => {
        // Use the showNotification function to display a success message
        showNotification(data.status === 'success' ? data.message : 'Please wait for the previous request to complete.');
    })
    .catch(error => {
        // Use the showNotification function to display an error message
        showNotification('Please wait for the previous request to complete.');
    });
});
    
