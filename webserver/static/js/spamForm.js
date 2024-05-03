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
        const notificationContainer = document.getElementById('notificationContainer');
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = data.status === 'success' ? data.message : 'An error occurred. Please try again.';
        notificationContainer.appendChild(notification);
        notification.classList.add('show');

        // Automatically hide the notification after 3 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            notificationContainer.removeChild(notification);
        }, 3000);
    })
    .catch(error => {
        const notificationContainer = document.getElementById('notificationContainer');
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = 'An error occurred. Please try again.';
        notificationContainer.appendChild(notification);
        notification.classList.add('show');

        // Automatically hide the notification after 3 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            notificationContainer.removeChild(notification);
        }, 3000);
    });
});
