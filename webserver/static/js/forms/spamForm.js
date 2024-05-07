// Function to handle form submission
function handleSubmit(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const formData = new FormData(this);
    const email = formData.get('email');
    const times = formData.get('times');

    const requestBody = createRequestBody(email, times);
    const url = '/v1/spam';

    sendPostRequest(url, requestBody)
        .then(async response => {
            if (response.ok) {
                showNotification(email + ' ' + times + ' times', 'Success');
                return response.json();
            } else {
                const text = await response.text();
                showNotification('Error: ' + text, 'Error', document.body);
                throw new Error(text);
            }
        });
}

// Function to create the request body
function createRequestBody(email, times) {
    return JSON.stringify({
        email: email,
        times: times
    });
}

// Function to send the POST request
function sendPostRequest(url, requestBody) {
    const postHeaders = {
        'Content-Type': 'application/json'
    };

    const fullUrl = 'http://127.0.0.1:999' + url; // Replace 'example.com' with your website's domain

    return fetch(fullUrl, {
        method: 'POST',
        headers: postHeaders,
        body: requestBody
    });
}

// Attach the event listener to the form
document.getElementById('spamForm').addEventListener('submit', handleSubmit);
