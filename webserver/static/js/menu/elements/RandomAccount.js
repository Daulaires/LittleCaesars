document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('RandomAccount');
    const body = document.body;

    toggleButton.addEventListener('click', function () {
        // Construct the URL for the GET request
        const url = '/v1/create_account_with_random_data';
        // Make the GET request
        fetch(url, {
            method: 'GET'
        })
            .then(async response => {
                if (response.ok) {
                    showNotification('Account: ' + await response.text(), 'Success', body);
                    return response.json();
                } else {
                    const text = await response.text();
                    showNotification('Error: ' + text, 'Error', body);
                    throw new Error(text);
                }
            })
    });
});