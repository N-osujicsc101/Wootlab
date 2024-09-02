document.getElementById("chatbot-icon").addEventListener("click", function() {
    var popup = document.getElementById("chatbot-popup");
    popup.style.display = popup.style.display === "block" ? "none" : "block";
});

document.getElementById("close-chatbot").addEventListener("click", function() {
    var popup = document.getElementById("chatbot-popup");
    popup.style.display = "none";
});

document.getElementById("chat-form").addEventListener("submit", function(event) {
    event.preventDefault();
    var userInput = document.getElementById("user_input").value;
    
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'user_input=' + encodeURIComponent(userInput)
    })
    .then(response => response.text())
    .then(html => {
        document.getElementById("chatbot-content").innerHTML = html;
    });
});
