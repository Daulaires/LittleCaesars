
// get the globalTimesCounter from the .json tile in webserver\global_spam_count.json
GetGlobalTimesCounter = () => {
    fetch('/get_global_spam_count')
    .then(response => response.json())
    .then(data => {
        globalTimesCounter = data.total_spam_count;
        // update the globalTimesCounter in the html
        document.getElementById("emailSpamCounter").innerHTML = "Total spam count: " + globalTimesCounter;
    });
}

GetGlobalTimesCounter();

