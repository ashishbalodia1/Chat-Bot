// Chatbot Configuration
const CHATBOT_CONFIG = {
    name: 'City Guardian Assistant',
    primaryColor: '#667eea',
    secondaryColor: '#764ba2',
    responseDelay: 1000, // milliseconds
};

// Knowledge Base for City Guardian
const knowledgeBase = {
    greetings: [
        "Hello! 👋 I'm the City Guardian Assistant. How can I help you today?",
        "Hi there! Welcome to City Guardian. What can I assist you with?",
        "Greetings! I'm here to help you with City Guardian. What would you like to know?"
    ],
    
    about: {
        keywords: ['what is', 'about', 'city guardian', 'tell me about', 'info'],
        responses: [
            "City Guardian is a comprehensive platform designed to help citizens report and track issues in their community. We make it easy to report problems like potholes, broken streetlights, graffiti, and other civic concerns. Our platform connects residents with local authorities to improve the quality of life in your city.",
            "City Guardian empowers citizens to be active participants in maintaining and improving their communities. Through our platform, you can report issues, track their resolution status, and stay informed about what's happening in your neighborhood."
        ]
    },
    
    features: {
        keywords: ['features', 'what can', 'capabilities', 'do'],
        responses: [
            "City Guardian offers several key features:\n\n✅ Report civic issues with photos and location\n✅ Track the status of your reports\n✅ View a map of issues in your area\n✅ Get notifications on report updates\n✅ Browse community issues and solutions\n✅ Connect with local authorities\n\nWhat would you like to know more about?"
        ]
    },
    
    report: {
        keywords: ['report', 'issue', 'problem', 'complaint', 'submit'],
        responses: [
            "To report an issue:\n\n1. Click on 'Report Issue' button\n2. Select the type of issue (pothole, streetlight, graffiti, etc.)\n3. Add a description and photos if available\n4. Mark the location on the map\n5. Submit your report\n\nYou'll receive a tracking number to monitor the status of your report. Would you like help with anything specific?"
        ]
    },
    
    track: {
        keywords: ['track', 'status', 'check', 'follow up', 'update'],
        responses: [
            "You can track your reports in several ways:\n\n• Go to 'My Reports' section in your dashboard\n• Use your tracking number to search\n• Enable notifications to get real-time updates\n• Check the status: Submitted → Under Review → In Progress → Resolved\n\nDo you have a specific report you'd like to track?"
        ]
    },
    
    contact: {
        keywords: ['contact', 'support', 'help', 'email', 'phone'],
        responses: [
            "You can reach City Guardian support through:\n\n📧 Email: support@cityguardian.com\n📱 Phone: +1 (555) 123-4567\n🕐 Hours: Monday-Friday, 9 AM - 6 PM\n💬 Live Chat: Available on our website\n\nIs there anything else I can help you with?"
        ]
    },
    
    account: {
        keywords: ['account', 'signup', 'register', 'login', 'sign in', 'profile'],
        responses: [
            "Managing your account is easy:\n\n• Sign up with your email or social media\n• Create a secure password\n• Verify your email address\n• Complete your profile with location details\n\nHaving an account lets you track reports, save favorite locations, and receive personalized updates. Need help with account setup?"
        ]
    },
    
    privacy: {
        keywords: ['privacy', 'data', 'security', 'safe', 'anonymous'],
        responses: [
            "Your privacy and security are our top priorities:\n\n🔒 All data is encrypted and secure\n🔒 You can report anonymously if preferred\n🔒 We never share personal information without consent\n🔒 Full transparency in how we handle data\n\nYou can review our complete Privacy Policy on the website. Any other concerns?"
        ]
    },
    
    default: [
        "I'm not sure I understand. Could you rephrase that? I can help you with:\n• Information about City Guardian\n• How to report issues\n• Tracking your reports\n• Contact information\n• Account management",
        "I'm here to help! I can assist you with reporting issues, tracking reports, learning about our features, or answering general questions about City Guardian. What would you like to know?",
        "That's a great question! While I may not have a specific answer, I can help you with:\n• Reporting community issues\n• Checking report status\n• Platform features\n• Contact information\n\nWhat interests you most?"
    ]
};

class CityGuardianChatbot {
    constructor() {
        this.isOpen = false;
        this.messageHistory = [];
        this.initializeElements();
        this.attachEventListeners();
    }

    initializeElements() {
        this.chatbotButton = document.getElementById('chatbot-button');
        this.chatbotWindow = document.getElementById('chatbot-window');
        this.chatbotClose = document.getElementById('chatbot-close');
        this.chatbotMessages = document.getElementById('chatbot-messages');
        this.chatbotInput = document.getElementById('chatbot-input');
        this.chatbotSend = document.getElementById('chatbot-send');
    }

    attachEventListeners() {
        // Toggle chatbot window
        this.chatbotButton.addEventListener('click', () => this.toggleChat());
        this.chatbotClose.addEventListener('click', () => this.toggleChat());

        // Send message
        this.chatbotSend.addEventListener('click', () => this.sendMessage());
        this.chatbotInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });

        // Quick replies
        this.chatbotMessages.addEventListener('click', (e) => {
            if (e.target.classList.contains('quick-reply')) {
                const message = e.target.getAttribute('data-message');
                this.handleQuickReply(message);
            }
        });
    }

    toggleChat() {
        this.isOpen = !this.isOpen;
        this.chatbotWindow.classList.toggle('hidden');
        
        if (this.isOpen) {
            this.chatbotInput.focus();
        }
    }

    sendMessage() {
        const message = this.chatbotInput.value.trim();
        
        if (!message) return;

        // Add user message
        this.addMessage(message, 'user');
        this.chatbotInput.value = '';

        // Show typing indicator
        this.showTypingIndicator();

        // Generate and show bot response
        setTimeout(() => {
            this.hideTypingIndicator();
            const response = this.generateResponse(message);
            this.addMessage(response, 'bot');
        }, CHATBOT_CONFIG.responseDelay);
    }

    handleQuickReply(message) {
        // Remove quick replies
        const quickRepliesContainer = document.querySelector('.quick-replies');
        if (quickRepliesContainer) {
            quickRepliesContainer.remove();
        }

        // Add user message
        this.addMessage(message, 'user');

        // Show typing indicator
        this.showTypingIndicator();

        // Generate and show bot response
        setTimeout(() => {
            this.hideTypingIndicator();
            const response = this.generateResponse(message);
            this.addMessage(response, 'bot');
        }, CHATBOT_CONFIG.responseDelay);
    }

    addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        
        const messageParagraph = document.createElement('p');
        messageParagraph.textContent = text;
        
        messageContent.appendChild(messageParagraph);
        messageDiv.appendChild(messageContent);
        
        this.chatbotMessages.appendChild(messageDiv);
        this.scrollToBottom();

        // Store in history
        this.messageHistory.push({ text, sender, timestamp: new Date() });
    }

    showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message';
        typingDiv.id = 'typing-indicator';
        
        const typingContent = document.createElement('div');
        typingContent.className = 'message-content';
        
        const typingIndicator = document.createElement('div');
        typingIndicator.className = 'typing-indicator';
        typingIndicator.innerHTML = `
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        `;
        
        typingContent.appendChild(typingIndicator);
        typingDiv.appendChild(typingContent);
        
        this.chatbotMessages.appendChild(typingDiv);
        this.scrollToBottom();
    }

    hideTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    generateResponse(userMessage) {
        const lowerMessage = userMessage.toLowerCase();

        // Check for greetings
        if (this.matchKeywords(lowerMessage, ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon'])) {
            return this.getRandomResponse(knowledgeBase.greetings);
        }

        // Check knowledge base categories
        for (const [category, data] of Object.entries(knowledgeBase)) {
            if (category === 'greetings' || category === 'default') continue;
            
            if (this.matchKeywords(lowerMessage, data.keywords)) {
                return this.getRandomResponse(data.responses);
            }
        }

        // Check for thanks
        if (this.matchKeywords(lowerMessage, ['thank', 'thanks', 'appreciate'])) {
            return "You're welcome! Is there anything else I can help you with regarding City Guardian?";
        }

        // Check for goodbye
        if (this.matchKeywords(lowerMessage, ['bye', 'goodbye', 'see you', 'later'])) {
            return "Goodbye! Feel free to reach out anytime you need assistance with City Guardian. Have a great day! 👋";
        }

        // Default response
        return this.getRandomResponse(knowledgeBase.default);
    }

    matchKeywords(message, keywords) {
        return keywords.some(keyword => message.includes(keyword));
    }

    getRandomResponse(responses) {
        return responses[Math.floor(Math.random() * responses.length)];
    }

    scrollToBottom() {
        this.chatbotMessages.scrollTop = this.chatbotMessages.scrollHeight;
    }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new CityGuardianChatbot();
});

// Export for integration
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CityGuardianChatbot;
}
