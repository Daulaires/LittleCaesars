document.getElementById('createAccountForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const formData = new FormData(this);
    const email = formData.get('email');
    const password = formData.get('password');

    // Construct the URL for the POST request
    const url = '/create_account'; // Assuming the Flask app endpoint for account creation

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
   .then(response => response.json()) // Parse the response as JSON
   .then(data => {
        if (data.status === 'success') {
            alert(data.message); // Show a success message
        } else {
            alert('An error occurred. Please try again.'); // Show an error message
        }
    })
   .catch(error => {
        alert('An error occurred. Please try again.'); // Show an error message
    });
});