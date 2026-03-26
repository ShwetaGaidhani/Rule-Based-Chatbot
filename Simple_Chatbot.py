"""
Test Suite and Examples for Rule-Based Chatbot
Demonstrates various conversation scenarios and features
"""

from Chatbot import RuleBasedChatbot


def print_separator(title=""):
    """Print a decorative separator."""
    if title:
        print(f"\n{'='*80}")
        print(f"  {title}")
        print(f"{'='*80}\n")
    else:
        print(f"{'─'*80}\n")


def test_conversation(chatbot, user_input):
    """Test a single conversation exchange."""
    response, intent = chatbot.chat(user_input)
    print(f"You: {user_input}")
    print(f"Bot: {response}")
    print(f"[Intent Detected: {intent}]")
    print()


def demo_greetings():
    """Demonstrate greeting intents."""
    print_separator("DEMO 1: Greeting Intents")
    
    chatbot = RuleBasedChatbot()
    
    greetings = [
        "Hello!",
        "Hi there",
        "Good morning",
        "Hey",
        "What's up?",
        "How are you?"
    ]
    
    for greeting in greetings:
        test_conversation(chatbot, greeting)
    
    return chatbot


def demo_knowledge_base():
    """Demonstrate knowledge base queries."""
    print_separator("DEMO 2: Knowledge Base Queries")
    
    chatbot = RuleBasedChatbot()
    
    queries = [
        "What is Python?",
        "Tell me about JavaScript",
        "Explain AI",
        "What is machine learning?",
        "Tell me about databases",
        "What is Git?",
        "Explain cloud computing"
    ]
    
    for query in queries:
        test_conversation(chatbot, query)
        print_separator()
    
    return chatbot


def demo_small_talk():
    """Demonstrate small talk capabilities."""
    print_separator("DEMO 3: Small Talk & Personality")
    
    chatbot = RuleBasedChatbot()
    
    small_talk = [
        "Tell me a joke",
        "You're awesome!",
        "Thanks for your help",
        "Who are you?",
        "What can you do?",
        "Are you a bot?",
        "Goodbye!"
    ]
    
    for message in small_talk:
        test_conversation(chatbot, message)
    
    return chatbot


def demo_learning_intent():
    """Demonstrate learning guidance."""
    print_separator("DEMO 4: Learning & Education")
    
    chatbot = RuleBasedChatbot()
    
    learning_queries = [
        "I want to learn programming",
        "How do I start?",
        "What is Python?",
        "Best way to learn?",
        "Help me get started"
    ]
    
    for query in learning_queries:
        test_conversation(chatbot, query)
    
    return chatbot


def demo_full_conversation():
    """Demonstrate a realistic full conversation."""
    print_separator("DEMO 5: Full Realistic Conversation")
    
    chatbot = RuleBasedChatbot()
    
    conversation = [
        "Hi!",
        "What can you help me with?",
        "I want to learn programming",
        "What is Python?",
        "Is it good for beginners?",
        "Tell me about AI",
        "What is machine learning?",
        "That's helpful, thanks!",
        "Tell me a joke",
        "Haha, you're funny!",
        "Bye!"
    ]
    
    for message in conversation:
        test_conversation(chatbot, message)
    
    return chatbot


def demo_conversation_logging():
    """Demonstrate conversation history and logging."""
    print_separator("DEMO 6: Conversation Logging & Statistics")
    
    chatbot = RuleBasedChatbot()
    
    # Have a conversation
    messages = [
        "Hello!",
        "What is Python?",
        "Tell me about AI",
        "Thanks!",
        "Tell me a joke",
        "Goodbye!"
    ]
    
    print("Having a conversation...\n")
    for msg in messages:
        chatbot.chat(msg)
    
    # Display history
    print_separator("Conversation History")
    history = chatbot.get_history()
    for entry in history:
        role = entry['role'].upper()
        message = entry['message'][:50] + "..." if len(entry['message']) > 50 else entry['message']
        intent = f" [{entry['intent']}]" if 'intent' in entry else ""
        print(f"{role}: {message}{intent}")
    
    # Display statistics
    print_separator("Statistics")
    stats = chatbot.get_stats()
    print(f"Total Messages: {stats['total_messages']}")
    print(f"User Messages: {stats['user_messages']}")
    print(f"Bot Messages: {stats['bot_messages']}")
    print(f"Unique Intents: {stats['total_intents']}")
    print(f"\nIntent Breakdown:")
    for intent, count in sorted(stats['intent_counts'].items(), key=lambda x: x[1], reverse=True):
        print(f"  • {intent}: {count}")
    
    # Export examples
    print_separator("Exporting Conversation")
    chatbot.export_history('demo_chat_history.txt')
    chatbot.export_history_json('demo_chat_history.json')
    
    return chatbot


def demo_unknown_handling():
    """Demonstrate handling of unknown inputs."""
    print_separator("DEMO 7: Handling Unknown Inputs")
    
    chatbot = RuleBasedChatbot()
    
    unknown_inputs = [
        "asdfghjkl",
        "What's the weather in Mars?",
        "Can you fly?",
        "Random gibberish xyz123",
        "Tell me about quantum mechanics"
    ]
    
    for message in unknown_inputs:
        test_conversation(chatbot, message)
    
    return chatbot


def demo_pattern_variations():
    """Demonstrate pattern matching variations."""
    print_separator("DEMO 8: Pattern Matching Variations")
    
    chatbot = RuleBasedChatbot()
    
    # Same intent, different phrasings
    print("Different ways to greet:")
    greetings = ["hi", "HI", "Hi!", "hello", "HELLO!", "Hey there", "good morning"]
    for g in greetings:
        response, intent = chatbot.chat(g)
        print(f"  '{g}' → Intent: {intent}")
    
    print("\nDifferent ways to ask for help:")
    help_requests = ["help", "Help me", "what can you do", "I need assistance"]
    for h in help_requests:
        response, intent = chatbot.chat(h)
        print(f"  '{h}' → Intent: {intent}")
    
    print("\nDifferent ways to ask about Python:")
    python_queries = ["What is Python?", "tell me about python", "explain python", "python"]
    for p in python_queries:
        response, intent = chatbot.chat(p)
        print(f"  '{p}' → Intent: {intent}")
    
    print()
    return chatbot


def demo_all_intents():
    """Test all available intents."""
    print_separator("DEMO 9: All Intent Categories")
    
    chatbot = RuleBasedChatbot()
    
    intent_examples = {
        'Greeting': 'Hello!',
        'Farewell': 'Goodbye',
        'Help': 'What can you do?',
        'Thanks': 'Thank you!',
        'About Bot': 'Who are you?',
        'Joke': 'Tell me a joke',
        'Compliment': 'You\'re awesome',
        'Mood': 'How are you?',
        'Learning': 'I want to learn',
        'Time': 'What time is it?',
        'Weather': 'How\'s the weather?',
        'Knowledge (Python)': 'What is Python?',
        'Knowledge (AI)': 'Tell me about AI'
    }
    
    for intent_name, example in intent_examples.items():
        print(f"{intent_name}:")
        response, detected_intent = chatbot.chat(example)
        print(f"  Input: {example}")
        print(f"  Detected: {detected_intent}")
        print()
    
    return chatbot


def demo_export_formats():
    """Demonstrate different export formats."""
    print_separator("DEMO 10: Export Formats")
    
    chatbot = RuleBasedChatbot()
    
    # Build conversation
    conversation = [
        "Hi!",
        "What is Python?",
        "Tell me a joke",
        "Thanks!",
        "Bye"
    ]
    
    for msg in conversation:
        chatbot.chat(msg)
    
    # Export in different formats
    print("Exporting conversation history...\n")
    
    # Text format
    chatbot.export_history('example_export.txt')
    print("\n✓ Text format exported")
    
    # JSON format
    chatbot.export_history_json('example_export.json')
    print("✓ JSON format exported")
    
    # Display sample from text export
    print_separator("Sample from TXT Export")
    with open('example_export.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()[:20]  # First 20 lines
        print(''.join(lines))
    
    # Display sample from JSON export
    print_separator("Sample from JSON Export")
    with open('example_export.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()[:15]  # First 15 lines
        print(''.join(lines))
    
    return chatbot


def run_all_demos():
    """Run all demonstration scenarios."""
    print("\n" + "="*80)
    print("  RULE-BASED CHATBOT - COMPREHENSIVE DEMO SUITE")
    print("="*80)
    print("\nThis demo showcases all features of the TechBot AI chatbot.")
    print("Each demo focuses on a specific capability or feature.\n")
    input("Press Enter to start the demos...")
    
    demos = [
        ("Greeting Intents", demo_greetings),
        ("Knowledge Base Queries", demo_knowledge_base),
        ("Small Talk & Personality", demo_small_talk),
        ("Learning & Education", demo_learning_intent),
        ("Full Realistic Conversation", demo_full_conversation),
        ("Conversation Logging & Statistics", demo_conversation_logging),
        ("Handling Unknown Inputs", demo_unknown_handling),
        ("Pattern Matching Variations", demo_pattern_variations),
        ("All Intent Categories", demo_all_intents),
        ("Export Formats", demo_export_formats)
    ]
    
    for i, (name, demo_func) in enumerate(demos, 1):
        print(f"\n{'#'*80}")
        print(f"  DEMO {i}/{len(demos)}: {name}")
        print(f"{'#'*80}\n")
        
        try:
            demo_func()
        except Exception as e:
            print(f"\n❌ Error in demo: {e}")
        
        if i < len(demos):
            input("\nPress Enter to continue to next demo...")
    
    print_separator("ALL DEMOS COMPLETED")
    print("✅ All demos have been executed successfully!")
    print("📁 Check the generated files:")
    print("   • demo_chat_history.txt")
    print("   • demo_chat_history.json")
    print("   • example_export.txt")
    print("   • example_export.json")
    print("\nThank you for exploring TechBot AI!")


def run_quick_test():
    """Run a quick test of core functionality."""
    print_separator("QUICK FUNCTIONALITY TEST")
    
    chatbot = RuleBasedChatbot()
    
    test_cases = [
        ("Greeting", "Hello!"),
        ("Knowledge", "What is Python?"),
        ("Help", "What can you do?"),
        ("Joke", "Tell me a joke"),
        ("Farewell", "Goodbye")
    ]
    
    print("Running quick tests...\n")
    
    for test_name, user_input in test_cases:
        response, intent = chatbot.chat(user_input)
        status = "✓" if intent != 'unknown' else "✗"
        print(f"{status} {test_name}: Intent '{intent}' detected")
    
    stats = chatbot.get_stats()
    print(f"\n✅ All tests completed!")
    print(f"   Messages: {stats['total_messages']}")
    print(f"   Intents: {stats['total_intents']}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--quick':
            run_quick_test()
        elif sys.argv[1] == '--all':
            run_all_demos()
        else:
            print("Usage:")
            print("  python test_chatbot.py --quick   # Quick functionality test")
            print("  python test_chatbot.py --all     # Run all demos")
    else:
        # Default: run all demos
        run_all_demos()
