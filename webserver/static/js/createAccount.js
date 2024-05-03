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
        const notificationContainer = document.getElementById('notificationContainer');
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = data.status === 'success' ? data.message : 'An error occurred. Please try again.';
        notificationContainer.appendChild(notification);
        notification.classList.add('show');

        setTimeout(() => {
            notification.classList.add('fadeOut'); // Trigger the fade-out animation
        }, 5000);
        // Automatically hide the notification after 3 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            notificationContainer.removeChild(notification);
        }, 10000);
    })
    .catch(error => {
        const notificationContainer = document.getElementById('notificationContainer');
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = 'An error occurred. Please try again.';
        notificationContainer.appendChild(notification);
        notification.classList.add('hide');

        setTimeout(() => {
            notification.classList.add('fadeOut'); // Trigger the fade-out animation
        }, 5000);
        // Automatically hide the notification after 3 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            notificationContainer.removeChild(notification);
        }, 10000);
    });
});
