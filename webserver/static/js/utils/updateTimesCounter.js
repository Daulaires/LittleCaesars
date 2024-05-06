GetGlobalTimesCounter = function() {
    fetch('/v1/get_global_spam_count')
        .then(response => response.json())
        .then(data => {
            globalTimesCounter = data.total_spam_count;
            // update the globalTimesCounter in the html
            showNotification('Spam count: ' + globalTimesCounter, 'Success');
        });

}

GetGlobalTimesCounter();

