# Quick Start Guide - City Guardian AI Chatbot

## For City Guardian Website Integration

### Step 1: Host the Files

Upload these files to your web server or CDN:
- `chatbot.css` (6.2 KB)
- `chatbot.js` (11 KB)

**Recommended hosting locations:**
- Your website's `/assets/` or `/static/` directory
- GitHub Pages: `https://yourusername.github.io/Chat-Bot/`
- CDN services: Cloudflare, AWS CloudFront, etc.

### Step 2: Add to Your Website

Add this code to your City Guardian website, just before the closing `</body>` tag:

```html
<!-- City Guardian Chatbot Widget -->
<link rel="stylesheet" href="YOUR_URL_HERE/chatbot.css">

<div id="chatbot-container" class="chatbot-container">
    <div id="chatbot-button" class="chatbot-button">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 2H4C2.9 2 2 2.9 2 4V22L6 18H20C21.1 18 22 17.1 22 16V4C22 2.9 21.1 2 20 2ZM20 16H6L4 18V4H20V16Z" fill="white"/>
            <path d="M7 9H9V11H7V9ZM11 9H13V11H11V9ZM15 9H17V11H15V9Z" fill="white"/>
        </svg>
    </div>
    
    <div id="chatbot-window" class="chatbot-window hidden">
        <div class="chatbot-header">
            <div class="chatbot-header-content">
                <div class="chatbot-avatar">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM12 5C13.66 5 15 6.34 15 8C15 9.66 13.66 11 12 11C10.34 11 9 9.66 9 8C9 6.34 10.34 5 12 5ZM12 19.2C9.5 19.2 7.29 17.92 6 15.98C6.03 13.99 10 12.9 12 12.9C13.99 12.9 17.97 13.99 18 15.98C16.71 17.92 14.5 19.2 12 19.2Z" fill="white"/>
                    </svg>
                </div>
                <div>
                    <h3 class="chatbot-title">City Guardian Assistant</h3>
                    <p class="chatbot-status">Online</p>
                </div>
            </div>
            <button id="chatbot-close" class="chatbot-close-btn">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M15 5L5 15M5 5L15 15" stroke="white" stroke-width="2" stroke-linecap="round"/>
                </svg>
            </button>
        </div>
        
        <div id="chatbot-messages" class="chatbot-messages">
            <div class="message bot-message">
                <div class="message-content">
                    <p>Hello! 👋 I'm the City Guardian Assistant. How can I help you today?</p>
                    <div class="quick-replies">
                        <button class="quick-reply" data-message="What is City Guardian?">What is City Guardian?</button>
                        <button class="quick-reply" data-message="How do I report an issue?">Report an issue</button>
                        <button class="quick-reply" data-message="Contact information">Contact info</button>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="chatbot-input-container">
            <input 
                type="text" 
                id="chatbot-input" 
                class="chatbot-input" 
                placeholder="Type your message..."
                autocomplete="off"
            >
            <button id="chatbot-send" class="chatbot-send-btn">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M2 10L18 2L10 18L8 11L2 10Z" fill="currentColor"/>
                </svg>
            </button>
        </div>
    </div>
</div>

<script src="YOUR_URL_HERE/chatbot.js"></script>
```

Replace `YOUR_URL_HERE` with your actual file hosting location.

### Step 3: Test

1. Open your City Guardian website
2. Look for the purple chat button in the bottom-right corner
3. Click it to open the chatbot
4. Try asking questions like:
   - "What is City Guardian?"
   - "How do I report a pothole?"
   - "Contact information"

### Step 4: Customize (Optional)

#### Change Colors
Edit `chatbot.js` - Line 2-5:
```javascript
const CHATBOT_CONFIG = {
    name: 'City Guardian Assistant',
    primaryColor: '#667eea',      // Your primary color
    secondaryColor: '#764ba2',    // Your secondary color
    responseDelay: 1000,
};
```

Also update the CSS gradients in `chatbot.css` (search for `linear-gradient`).

#### Add/Edit Responses
Edit the `knowledgeBase` object in `chatbot.js` to add new topics or modify existing responses.

## Troubleshooting

**Chatbot button not appearing?**
- Check browser console for errors
- Verify file paths are correct
- Ensure CSS and JS files are loaded

**Chatbot not responding?**
- Check browser console for JavaScript errors
- Verify the chatbot.js file is loaded correctly

**Styling looks wrong?**
- Verify chatbot.css is loaded
- Check for CSS conflicts with your site's styles

## Support

For issues or questions:
- Check the README.md file
- Review the test.html file for usage examples
- Open an issue on GitHub

---

**Developed for City Guardian**
Version 1.0.0
