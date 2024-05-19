document.getElementById('chat-form').addEventListener('submit', function(event) {
  event.preventDefault();

  var inputText = document.getElementById('input-text').value;

  fetch('/generate_response/?input_text=' + encodeURIComponent(inputText))
    .then(response => response.json())
    .then(data => {
      document.getElementById('response-container').innerText = data.response;
    });
});