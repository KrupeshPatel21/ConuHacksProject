var video = document.getElementById("myVideo");
var btn = document.getElementById("myBtn");

function myFunction() {
    if (video.paused) {
        video.play();
        btn.innerHTML = "Pause";
    } else {
        video.pause();
        btn.innerHTML = "Play";
    }
}


function updateChart() {
    // Get the selected weather option
    var selectedWeather = document.getElementById("weather-select").value;

    // Update the background based on the selected weather
    updateBackground(selectedWeather);

    // Implement the rest of your chart update logic here
}

function updateBackground(weather) {
    var backgroundContainer = document.getElementById("weather-animation");

    // Set background image based on the selected weather
    switch (weather) {
        case "sunny":
            backgroundContainer.style.backgroundImage = "url('path/to/sunny-background.jpg')";
            break;
        case "rainy":
            backgroundContainer.style.backgroundImage = "url('path/to/rainy-background.jpg')";
            break;
        case "cloudy":
            backgroundContainer.style.backgroundImage = "url('path/to/cloudy-background.jpg')";
            break;
        case "snowy":
            backgroundContainer.style.backgroundImage = "url('path/to/snowy-background.jpg')";
            break;
        default:
            backgroundContainer.style.backgroundImage = "url('path/to/default-background.jpg')";
            break;
    }
}
