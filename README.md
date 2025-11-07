# City Guardian AI Chatbot

An intelligent, responsive AI chatbot specifically designed for the City Guardian platform. This chatbot helps users navigate the platform, report issues, track their submissions, and get instant answers to common questions about civic engagement.

![Chatbot Preview](https://img.shields.io/badge/Status-Active-success)
![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Features

- **💬 Intelligent Conversations**: AI-powered responses to user queries about City Guardian
- **🎨 Modern UI/UX**: Beautiful, responsive design that works on all devices
- **⚡ Quick Replies**: Pre-defined quick reply buttons for common questions
- **📱 Mobile Responsive**: Optimized for mobile, tablet, and desktop
- **🔧 Easy Integration**: Simple embed code for any website
- **🎯 Context-Aware**: Understands user intent and provides relevant information
- **⌨️ Real-time Typing**: Shows typing indicator for natural conversation flow
- **🎨 Customizable**: Easy to customize colors, branding, and responses

## 🚀 Quick Start

### Demo
Open `chatbot.html` in your browser to see a live demo of the chatbot.

### Integration into City Guardian Website

#### Option 1: Direct Integration (Recommended)

1. **Add the CSS file** to your HTML `<head>`:
```html
<link rel="stylesheet" href="chatbot.css">
```

2. **Add the chatbot HTML** before the closing `</body>` tag:
```html
<!-- Copy the chatbot HTML from embed.html -->
```

3. **Add the JavaScript** file before the closing `</body>` tag:
```html
<script src="chatbot.js"></script>
```

#### Option 2: CDN Integration (For Production)

Once deployed to a CDN or web hosting, use:

```html
<!-- Add to <head> -->
<link rel="stylesheet" href="https://your-cdn-url/chatbot.css">

<!-- Add before </body> -->
<div id="chatbot-container" class="chatbot-container">
    <!-- Chatbot HTML from embed.html -->
</div>
<script src="https://your-cdn-url/chatbot.js"></script>
```

#### Option 3: Using the Embed File

Simply copy the contents of `embed.html` and paste it into your website before the closing `</body>` tag.

## 📁 File Structure

```
Chat-Bot/
├── chatbot.html       # Demo page showcasing the chatbot
├── chatbot.css        # All styles for the chatbot widget
├── chatbot.js         # Chatbot logic and AI responses
├── embed.html         # Ready-to-embed code snippet
└── README.md          # This file
```

## 🎯 Chatbot Capabilities

The City Guardian AI Chatbot can help users with:

### 1. **Platform Information**
- Explain what City Guardian is
- Describe platform features and capabilities
- Share platform benefits

### 2. **Reporting Issues**
- Guide users through the issue reporting process
- Explain different types of issues that can be reported
- Help with photo uploads and location marking

### 3. **Tracking Reports**
- Explain how to track submitted reports
- Describe different report statuses
- Help find specific reports

### 4. **Account Management**
- Guide through signup/login process
- Explain profile setup
- Help with account-related questions

### 5. **Contact & Support**
- Provide contact information
- Share support hours
- Direct to appropriate resources

### 6. **Privacy & Security**
- Answer privacy-related questions
- Explain data handling
- Address security concerns

## 🛠️ Customization

### Changing Colors

Edit the `CHATBOT_CONFIG` object in `chatbot.js`:

```javascript
const CHATBOT_CONFIG = {
    name: 'City Guardian Assistant',
    primaryColor: '#667eea',      // Change this
    secondaryColor: '#764ba2',    // Change this
    responseDelay: 1000,
};
```

Update the CSS gradients in `chatbot.css`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Adding New Responses

Edit the `knowledgeBase` object in `chatbot.js`:

```javascript
const knowledgeBase = {
    // Add new category
    newCategory: {
        keywords: ['keyword1', 'keyword2'],
        responses: [
            "Your response here",
            "Alternative response"
        ]
    }
};
```

### Changing Chatbot Name

Update in three places:
1. `CHATBOT_CONFIG.name` in `chatbot.js`
2. `.chatbot-title` text in HTML files
3. Update responses in `knowledgeBase`

## 💡 Usage Examples

### Example Conversations

**User**: "What is City Guardian?"
**Bot**: Provides detailed information about the platform

**User**: "How do I report an issue?"
**Bot**: Gives step-by-step instructions for reporting

**User**: "Contact information"
**Bot**: Shares contact details and support hours

## 🎨 UI Components

### Chatbot Button
- Fixed position in bottom-right corner
- Smooth hover animations
- Gradient background matching brand colors

### Chat Window
- Responsive design (380px width on desktop)
- Smooth open/close animations
- Scrollable message area
- Typing indicators

### Messages
- User messages: Right-aligned with gradient background
- Bot messages: Left-aligned with white background
- Quick reply buttons for common actions
- Smooth fade-in animations

## 📱 Responsive Design

The chatbot is fully responsive:
- **Desktop**: 380px width, fixed position
- **Tablet**: Adapts to screen size
- **Mobile**: Full-width overlay, optimized touch targets

## 🔧 Technical Details

### Technologies Used
- Pure JavaScript (ES6+)
- CSS3 with animations
- HTML5
- No external dependencies

### Browser Support
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

### Performance
- Lightweight (~22KB total)
- Fast load time
- Minimal DOM manipulation
- Efficient event handling

## 🚦 Testing

1. Open `chatbot.html` in a browser
2. Click the chat button in the bottom-right
3. Try these test queries:
   - "What is City Guardian?"
   - "How do I report an issue?"
   - "Contact information"
   - "Tell me about features"
   - "Help with my account"

## 📝 Future Enhancements

Potential improvements:
- [ ] Backend API integration for dynamic responses
- [ ] Machine learning for better intent recognition
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] File upload capability
- [ ] Integration with City Guardian database
- [ ] Analytics and conversation tracking
- [ ] Admin dashboard for managing responses
- [ ] Sentiment analysis
- [ ] Proactive chat triggers

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created for City Guardian Platform
Website: https://cityguardian-frontend.vercel.app/

## 📞 Support

For questions or support regarding this chatbot:
- Open an issue on GitHub
- Contact: support@cityguardian.com

## 🙏 Acknowledgments

- Designed for the City Guardian civic engagement platform
- Built with modern web technologies
- Inspired by best practices in conversational UI

---

**Note**: This chatbot uses predefined responses and pattern matching. For production use with real AI capabilities, consider integrating with services like OpenAI GPT, Dialogflow, or similar AI platforms.
