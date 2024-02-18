// Your JavaScript code for chatbot functionality here
document.getElementById('user-input').addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
      sendMessage();
  }
});

function sendMessage() {
  var userInput = document.getElementById('user-input').value;
  if (!userInput) return;

  appendMessage(userInput, true);
  document.getElementById('user-input').value = '';

  // Call backend (e.g., chatbot.py) to process user input and get bot response
  fetch('/process', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message: userInput })
  })
  .then(response => response.json())
  .then(data => {
      var botResponse = data.message;
      appendMessage(botResponse, false);
  })
  .catch(error => console.error('Error:', error));
}

function appendMessage(message, isUser) {
  var chatMessages = document.getElementById('chat-messages');
  var messageElement = document.createElement('div');
  messageElement.classList.add(isUser ? 'user-message' : 'bot-message');
  messageElement.textContent = message;
  chatMessages.appendChild(messageElement);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}
