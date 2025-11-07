// Chatbot Widget JavaScript

(function() {
    'use strict';

    // Create chatbot HTML structure
    const chatbotHTML = `
        <button id="chatbot-toggle" aria-label="Toggle chat">
            <svg viewBox="0 0 24 24">
                <path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/>
            </svg>
        </button>
        <div id="chatbot-container">
            <div class="chatbot-header">
                <h3>Chat Support</h3>
                <button class="chatbot-close" aria-label="Close chat">&times;</button>
            </div>
            <div id="chatbot-messages"></div>
            <div class="chatbot-input-area">
                <input type="text" id="chatbot-input" placeholder="Type your message..." />
                <button id="chatbot-send" aria-label="Send message">
                    <svg viewBox="0 0 24 24">
                        <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
                    </svg>
                </button>
            </div>
        </div>
    `;

    // Insert chatbot into DOM when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initChatbot);
    } else {
        initChatbot();
    }

    function initChatbot() {
        // Add chatbot to body
        const container = document.createElement('div');
        container.innerHTML = chatbotHTML;
        document.body.appendChild(container);

        // Get elements
        const toggle = document.getElementById('chatbot-toggle');
        const chatContainer = document.getElementById('chatbot-container');
        const closeBtn = document.querySelector('.chatbot-close');
        const input = document.getElementById('chatbot-input');
        const sendBtn = document.getElementById('chatbot-send');
        const messagesContainer = document.getElementById('chatbot-messages');

        // Chatbot responses
        const responses = {
            'hello': 'Hello! How can I help you today?',
            'hi': 'Hi there! What can I do for you?',
            'help': 'I\'m here to help! You can ask me about our services, pricing, or general questions.',
            'how are you': 'I\'m doing great, thank you for asking! How can I assist you?',
            'bye': 'Goodbye! Have a great day!',
            'thanks': 'You\'re welcome! Is there anything else I can help you with?',
            'thank you': 'You\'re welcome! Feel free to ask if you need anything else.',
            'price': 'Our pricing varies depending on your needs. Please contact our sales team for detailed information.',
            'contact': 'You can reach us at support@example.com or call us at +1-234-567-8900.',
            'hours': 'We\'re available Monday to Friday, 9 AM to 6 PM EST.',
            'services': 'We offer a wide range of services including web development, consulting, and support. What would you like to know more about?',
            'default': 'I\'m not sure I understand. Could you please rephrase your question or type "help" for assistance?'
        };

        // Toggle chatbot
        toggle.addEventListener('click', () => {
            chatContainer.classList.toggle('active');
            if (chatContainer.classList.contains('active')) {
                input.focus();
                // Show welcome message if no messages yet
                if (messagesContainer.children.length === 0) {
                    addMessage('Hello! I\'m your virtual assistant. How can I help you today?', 'bot');
                }
            }
        });

        // Close chatbot
        closeBtn.addEventListener('click', () => {
            chatContainer.classList.remove('active');
        });

        // Send message on button click
        sendBtn.addEventListener('click', sendMessage);

        // Send message on Enter key
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });

        function sendMessage() {
            const message = input.value.trim();
            if (message === '') return;

            // Add user message
            addMessage(message, 'user');
            input.value = '';

            // Generate bot response after a short delay
            setTimeout(() => {
                const response = getBotResponse(message);
                addMessage(response, 'bot');
            }, 500);
        }

        function addMessage(text, sender) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}`;
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.textContent = text;
            
            messageDiv.appendChild(contentDiv);
            messagesContainer.appendChild(messageDiv);
            
            // Scroll to bottom
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }

        function getBotResponse(userMessage) {
            const message = userMessage.toLowerCase().trim();
            
            // Check for keyword matches
            for (const [key, response] of Object.entries(responses)) {
                if (key !== 'default' && message.includes(key)) {
                    return response;
                }
            }
            
            return responses.default;
        }
    }
})();
