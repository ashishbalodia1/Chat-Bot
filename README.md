# Chat-Bot

A simple, customizable chatbot widget that can be easily integrated into any website.

## Features

- 🎨 Clean and modern UI
- 📱 Responsive design (mobile-friendly)
- 🎯 Easy to integrate
- 💬 Interactive chat interface
- ⚡ Lightweight and fast
- 🔧 Customizable responses

## Demo

Open `index.html` in your browser to see the chatbot in action!

## Quick Start

### Basic Integration

Add the following files to your website:

1. `chatbot.css` - Chatbot styles
2. `chatbot.js` - Chatbot functionality

Then include them in your HTML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Website</title>
    <link rel="stylesheet" href="chatbot.css">
</head>
<body>
    <!-- Your website content -->
    
    <!-- Include chatbot at the end of body -->
    <script src="chatbot.js"></script>
</body>
</html>
```

That's it! The chatbot will automatically appear as a floating button in the bottom-right corner of your page.

## Customization

### Modifying Responses

Edit the `responses` object in `chatbot.js` to customize the chatbot's replies:

```javascript
const responses = {
    'hello': 'Hello! How can I help you today?',
    'help': 'I\'m here to help! You can ask me about our services.',
    // Add your own keywords and responses
    'default': 'I\'m not sure I understand. Could you please rephrase?'
};
```

### Styling

Modify `chatbot.css` to change the appearance:

- Change colors by updating the gradient values
- Adjust sizes by modifying width/height properties
- Customize positioning by changing the bottom/right values

### Widget Position

By default, the chatbot appears in the bottom-right corner. To change this, edit the CSS:

```css
#chatbot-toggle {
    bottom: 20px;  /* Distance from bottom */
    right: 20px;   /* Distance from right */
}
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

MIT License - see [LICENSE](LICENSE) file for details

## Author

Ashish Balodia

## Contributing

Feel free to submit issues and enhancement requests!
