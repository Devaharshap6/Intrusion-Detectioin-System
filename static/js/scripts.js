document.addEventListener("DOMContentLoaded", () => {
    const alertsList = document.getElementById("alerts-list");

    function fetchAlerts() {
        fetch("/alerts")
            .then(response => response.json())
            .then(alerts => {
                alertsList.innerHTML = "";
                alerts.forEach(alert => {
                    const li = document.createElement("li");
                    li.textContent = `Alert: ${alert.alert} | Packet: ${JSON.stringify(alert.packet)}`;
                    alertsList.appendChild(li);
                });
            });
    }

    setInterval(fetchAlerts, 2000); // Fetch alerts every 2 seconds
});
