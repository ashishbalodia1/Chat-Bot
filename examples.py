"""
Example usage of City Guardian AI Assistant
Demonstrates various features and capabilities
"""

from city_guardian_bot import CityGuardianBot
from api_client import MockAPIClient


def run_examples():
    """Run example interactions with the bot"""
    
    # Initialize bot with mock API client
    api_client = MockAPIClient()
    bot = CityGuardianBot(api_client=api_client)
    
    print("=" * 70)
    print("City Guardian AI Assistant - Example Interactions")
    print("=" * 70)
    print()
    
    # Example 1: Complaint Status (Hindi)
    print("Example 1: Complaint Status Query (Hindi)")
    print("-" * 70)
    user_input = "Meri complaint ID CG-2025-00045 ki status batao"
    print(f"User: {user_input}")
    response = bot.process_message(user_input)
    print(f"Bot: {response}")
    print()
    
    # Example 2: Complaint Status (English)
    print("Example 2: Complaint Status Query (English)")
    print("-" * 70)
    user_input = "What is the status of complaint CG-2025-12345?"
    print(f"User: {user_input}")
    response = bot.process_message(user_input)
    print(f"Bot: {response}")
    print()
    
    # Example 3: Environmental Data (Hindi)
    print("Example 3: Environmental Data Query (Hindi)")
    print("-" * 70)
    user_input = "Zone 3 ka AQI kaisa hai?"
    print(f"User: {user_input}")
    response = bot.process_message(user_input)
    print(f"Bot: {response}")
    print()
    
    # Example 4: Environmental Data (English)
    print("Example 4: Environmental Data Query (English)")
    print("-" * 70)
    user_input = "What is the air quality in Zone 2?"
    print(f"User: {user_input}")
    response = bot.process_message(user_input)
    print(f"Bot: {response}")
    print()
    
    # Example 5: Complaint Registration Attempt (Hindi)
    print("Example 5: Complaint Registration Attempt (Hindi)")
    print("-" * 70)
    user_input = "Main nayi shikayat darj karna chahta hoon"
    print(f"User: {user_input}")
    response = bot.process_message(user_input)
    print(f"Bot: {response}")
    print()
    
    # Example 6: Complaint Registration Attempt (English)
    print("Example 6: Complaint Registration Attempt (English)")
    print("-" * 70)
    user_input = "I want to register a new complaint"
    print(f"User: {user_input}")
    response = bot.process_message(user_input)
    print(f"Bot: {response}")
    print()
    
    # Example 7: Zone Achievements (Hindi)
    print("Example 7: Zone Achievements Query (Hindi)")
    print("-" * 70)
    user_input = "Sabse achhe zones kaun se hain?"
    print(f"User: {user_input}")
    response = bot.process_message(user_input)
    print(f"Bot: {response}")
    print()
    
    # Example 8: Zone Achievements (English)
    print("Example 8: Zone Achievements Query (English)")
    print("-" * 70)
    user_input = "Show me top performing zones"
    print(f"User: {user_input}")
    response = bot.process_message(user_input)
    print(f"Bot: {response}")
    print()
    
    # Example 9: Policy Information (Hindi)
    print("Example 9: Policy Information Query (Hindi)")
    print("-" * 70)
    user_input = "Water connection kaise milega?"
    print(f"User: {user_input}")
    response = bot.process_message(user_input)
    print(f"Bot: {response}")
    print()
    
    # Example 10: Unknown Intent (English)
    print("Example 10: General Greeting (English)")
    print("-" * 70)
    user_input = "Hello, what can you do?"
    print(f"User: {user_input}")
    response = bot.process_message(user_input)
    print(f"Bot: {response}")
    print()
    
    print("=" * 70)
    print("Examples completed!")
    print("=" * 70)


def interactive_mode():
    """Run bot in interactive mode"""
    
    print("\n" + "=" * 70)
    print("City Guardian AI Assistant - Interactive Mode")
    print("=" * 70)
    print("\nCommands:")
    print("  - Type your message in Hindi or English")
    print("  - Type 'examples' to see example queries")
    print("  - Type 'quit' or 'exit' to end session")
    print()
    
    # Initialize bot
    api_client = MockAPIClient()
    bot = CityGuardianBot(api_client=api_client)
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            print("\nBot: Thank you for using City Guardian! Dhanyavaad!")
            break
        
        if user_input.lower() == 'examples':
            print("\nExample queries you can try:")
            print("  - Meri complaint ID CG-2025-00045 ki status batao")
            print("  - What is the AQI in Zone 3?")
            print("  - Show me top performing zones")
            print("  - Zone 2 ka environmental data chahiye")
            print("  - I want to register a complaint")
            print()
            continue
        
        response = bot.process_message(user_input)
        print(f"\nBot: {response}\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        interactive_mode()
    else:
        run_examples()
        print("\nRun with --interactive flag for interactive mode:")
        print("  python examples.py --interactive")
