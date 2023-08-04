function getWeather() {
  const location = document.getElementById("location").value;

  fetch(`/weather?location=${location}`)
    .then((response) => response.json())
    .then((data) => {
      const weatherInfo = document.getElementById("weather-info");
      weatherInfo.innerHTML = `
        <h2>Weather Information for ${data.name}</h2>
        <p>Current Weather: ${data.weather[0].description}</p>
        <p>Temperature: ${data.main.temp} °C</p>
        <p>Humidity: ${data.main.humidity}%</p>
      `;
    })
    .catch((error) => {
      console.error("Error fetching weather data:", error);
    });
}
