/**
 * This was made to test the functionality of the website https://www.littlecaesars.com/en-us/
 * This was made for educational purposes only.
 * Author: @Daulaires / https://www.github.com/Daulaires/LittleCaesarsEmailSpammer
 * Date: 2024-05-02
 */

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
