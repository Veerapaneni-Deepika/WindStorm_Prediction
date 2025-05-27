function predictStorm() {
  const humidity = parseFloat(document.getElementById('humidity').value);
  const pressure = parseFloat(document.getElementById('pressure').value);
  const temperature = parseFloat(document.getElementById('temperature').value);

  let resultText = "";

  // Simple heuristic logic to simulate prediction
  if (humidity > 70 && pressure < 1000 && temperature > 25) {
    resultText = "⚠️ High Risk of Windstorm";
  } else if (humidity > 50 && pressure < 1010) {
    resultText = "⚠️ Moderate Risk of Windstorm";
  } else {
    resultText = "✅ No Windstorm Expected";
  }

  document.getElementById("result").innerText = resultText;
}
