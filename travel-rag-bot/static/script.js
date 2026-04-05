async function sendMessage() {
    let input = document.getElementById("userInput").value.trim();
    if (!input) return;

    let chatbox = document.getElementById("chatbox");
    let sendBtn = document.getElementById("sendBtn");

    chatbox.innerHTML += `<div class="user-msg">${input}</div>`;
    document.getElementById("userInput").value = "";

    const loadingId = "loading-" + Date.now();
    chatbox.innerHTML += `
        <div class="bot-msg loading-dots" id="${loadingId}">
            <span></span><span></span><span></span>
        </div>`;

    sendBtn.disabled = true;
    chatbox.scrollTop = chatbox.scrollHeight;

    try {
        let res = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: input })
        });

        let data = await res.json();

        // ✅ Format the response
        let formatted = formatResponse(data.response);

        document.getElementById(loadingId).outerHTML =
            `<div class="bot-msg">${formatted}</div>`;

    } catch (error) {
        document.getElementById(loadingId).outerHTML =
            `<div class="bot-msg">⚠️ Server error. Please try again.</div>`;
    }

    sendBtn.disabled = false;
    chatbox.scrollTop = chatbox.scrollHeight;
}

// ✅ Format plain text into readable HTML
function formatResponse(text) {
    return text
        // Bold **text**
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        // Bullet points starting with - or *
        .replace(/^[-*]\s+(.+)/gm, '<li>$1</li>')
        // Wrap list items in <ul>
        .replace(/(<li>.*<\/li>)/gs, '<ul>$1</ul>')
        // Numbered lines
        .replace(/^\d+\.\s+(.+)/gm, '<li>$1</li>')
        // Line breaks
        .replace(/\n{2,}/g, '<br><br>')
        .replace(/\n/g, '<br>');
}