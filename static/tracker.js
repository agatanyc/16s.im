//Track how long the user stays on the given page.
//Ping the server every 10 seconds. 

var timeSpent = 0;
function ping(url) {

  var http = new XMLHttpRequest();
  console.log(url);
  timeSpent += 10;
  // update the page every 10 seconds
  var timeSpentDiv = document.getElementById('time-spent');
  http.onreadystatechange = function() {
      if (http.readyState === XMLHttpRequest.DONE) {
          timeSpentDiv.innerHTML = timeSpent;
      }
  }
  http.open("GET", url, /*async*/true);
  http.send();
}

function track(trackingUrl) {
  setInterval(function(){ 
      ping(trackingUrl);
  }, 10000);
}

function sendTimeSpent() {
    http = new XMLHttpRequest();
    http.open("GET", url + "?leaving=True&timeSpent=" + timeSpent, true);
    http.send();
}

// function called when the user exits
window.onbeforeunload = sendTimeSpent;
