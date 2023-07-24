fetch('/predict', {
    method: 'POST',
    body: new FormData(event.target)
})
.then(response => response.text())
.then(data => {
    document.getElementById('prediction').textContent = data;
    document.getElementById('prediction').style.display = 'block';
});
