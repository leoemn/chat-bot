const sendButton = document.getElementById('send');
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');

function sendMessage() {
    const userMessage = userInput.value;

    chatBox.innerHTML += `<div> User: ${userMessage}</div>`

    fetch('http://127.0.0.1:5000/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({userMessage: userMessage}),
    })
    .then(response => response.json())
    .then(data =>{
        const responseMessage = data.responseMessage;
        chatBox.innerHTML += `<div>Bot: ${responseMessage}</div>`;
    });

    userInput.value = '';
}


sendButton.addEventListener('click', sendMessage);

userInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});