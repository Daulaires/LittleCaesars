document.getElementById('createAccountForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(this);
    const email = formData.get('email');
    const password = formData.get('password');
    const url = '/v1/create';
    const requestBody = JSON.stringify({ email: email, password: password });
    const postHeaders = { 'Content-Type': 'application/json' };
    fetch(url, { method: 'POST', headers: postHeaders, body: requestBody }).then(async response => {
        if (response.ok) {
            showNotification('Account created for ' + email, 'Success');
            return response.json();
        } else {
            const text = await response.text();
            showNotification('Error: ' + text, 'Error');
            throw new Error(text);
        }
    });
});