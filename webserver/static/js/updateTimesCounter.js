
// get the globalTimesCounter from the .json tile in webserver\global_spam_count.json
GetGlobalTimesCounter = function() {
    fetch('/get_global_spam_count')
    .then(response => response.json())
    .then(data => {
        globalTimesCounter = data.total_spam_count;
        // update the globalTimesCounter in the html
        document.getElementById("globalTimesCounter").innerHTML = "Total spam count: " + globalTimesCounter;
    });
}

// get the globalTimesCounter from the .json tile in webserver\global_spam_count.json
GetGlobalTimesCounter();

