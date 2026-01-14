function doAction() {
  fetch("/action", { method: "POST" })
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").textContent =
        JSON.stringify(data, null, 2);
    });
}

function sell() {
  fetch("/sell", { method: "POST" })
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").textContent =
        JSON.stringify(data, null, 2);
    });
}