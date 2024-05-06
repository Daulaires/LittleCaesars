updateData = function() {
    fetch('/v1/get_accounts_created_count')
        .then(response => response.json())
        .then(data => {
            accountsCreated = data.total_accounts_created;
            // update the accountsCreated in the html
            showNotification('Accounts created: ' + accountsCreated, 'Success');
        });
}

updateData();