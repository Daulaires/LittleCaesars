document.addEventListener('DOMContentLoaded', function () {
    const RandomAccountButton = document.getElementById('RandomAccount');
    const randomAccountBody = document.body;

    RandomAccountButton.addEventListener('click', function () {
        // Construct the URL for the GET request
        const url = '/v1/create_account_with_random_data';
        // Make the GET request
        fetch(url, {
            method: 'GET'
        })
            .then(async response => {
                if (response.ok) {
                    // Assuming the response is JSON, use response.json()
                    const data = await response.json();
                    showNotification('Account: ' + JSON.stringify(data), 'Success', randomAccountBody);
                    return data;
                } else {
                    const text = await response.text();
                    showNotification('Error: ' + text, 'Error', randomAccountBody);
                    throw new Error(text);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showNotification('Error: ' + error.message, 'Error', randomAccountBody);
            });
    });
});
