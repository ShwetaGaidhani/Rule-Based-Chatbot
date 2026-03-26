"""
Rule-Based Chatbot with Pattern Matching
Features: Multiple intents, knowledge base, conversation history, and logging
"""

import re
import random
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import json


class RuleBasedChatbot:
    """A rule-based chatbot using pattern matching for intent recognition."""
    
    def __init__(self):
        self.conversation_history: List[Dict] = []
        self.intent_counts: Dict[str, int] = {}
        self.knowledge_base = self._initialize_knowledge_base()
        self.patterns = self._initialize_patterns()
        
    def _initialize_knowledge_base(self) -> Dict:
        """Initialize the domain knowledge base."""
        return {
            # Programming Languages
            'python': {
                'definition': 'Python is a high-level, interpreted programming language known for its simplicity and readability. Created by Guido van Rossum in 1991.',
                'features': ['Easy to learn', 'Versatile', 'Large standard library', 'Great for AI/ML'],
                'uses': 'Web development, Data Science, AI/ML, Automation, Scripting',
                'difficulty': 'Beginner-friendly'
            },
            'javascript': {
                'definition': 'JavaScript is a dynamic programming language primarily used for web development. It runs in browsers and on servers (Node.js).',
                'features': ['Event-driven', 'Asynchronous', 'Prototype-based', 'Multi-paradigm'],
                'uses': 'Web development, Mobile apps, Game development, Server-side',
                'difficulty': 'Beginner to Intermediate'
            },
            'java': {
                'definition': 'Java is a class-based, object-oriented programming language designed to have few implementation dependencies.',
                'features': ['Platform independent', 'Object-oriented', 'Secure', 'Robust'],
                'uses': 'Enterprise applications, Android apps, Web servers, Big data',
                'difficulty': 'Intermediate'
            },
            'c++': {
                'definition': 'C++ is a general-purpose programming language created as an extension of C with object-oriented features.',
                'features': ['High performance', 'Low-level control', 'Object-oriented', 'Generic programming'],
                'uses': 'System software, Game development, Real-time systems, Embedded systems',
                'difficulty': 'Advanced'
            },
            'ruby': {
                'definition': 'Ruby is a dynamic, object-oriented programming language focused on simplicity and productivity.',
                'features': ['Elegant syntax', 'Fully object-oriented', 'Dynamic typing', 'Garbage collection'],
                'uses': 'Web development (Rails), Scripting, Automation',
                'difficulty': 'Beginner-friendly'
            },
            
            # Technologies
            'ai': {
                'definition': 'Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems.',
                'subfields': ['Machine Learning', 'Deep Learning', 'Natural Language Processing', 'Computer Vision'],
                'applications': 'Virtual assistants, Self-driving cars, Medical diagnosis, Recommendation systems',
                'history': 'Term coined in 1956 at Dartmouth Conference'
            },
            'machine learning': {
                'definition': 'Machine Learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed.',
                'types': ['Supervised Learning', 'Unsupervised Learning', 'Reinforcement Learning'],
                'algorithms': 'Neural Networks, Decision Trees, SVM, Random Forests, K-Means',
                'applications': 'Image recognition, Spam detection, Recommendation systems'
            },
            'api': {
                'definition': 'API (Application Programming Interface) is a set of protocols and tools for building software applications.',
                'types': ['REST API', 'SOAP API', 'GraphQL', 'WebSocket'],
                'purpose': 'Enables communication between different software systems',
                'example': 'Twitter API, Google Maps API, Weather API'
            },
            'database': {
                'definition': 'A database is an organized collection of structured data stored electronically.',
                'types': {
                    'SQL': 'MySQL, PostgreSQL, SQLite, Oracle',
                    'NoSQL': 'MongoDB, Redis, Cassandra, CouchDB'
                },
                'uses': 'Data storage, Data retrieval, Data management, Analytics',
                'operations': 'CRUD - Create, Read, Update, Delete'
            },
            'git': {
                'definition': 'Git is a distributed version control system for tracking changes in source code during software development.',
                'features': ['Branching', 'Merging', 'Distributed', 'Fast', 'Data integrity'],
                'commands': 'git add, git commit, git push, git pull, git merge, git branch',
                'platforms': 'GitHub, GitLab, Bitbucket',
                'creator': 'Linus Torvalds (2005)'
            },
            'cloud computing': {
                'definition': 'Cloud computing is the delivery of computing services over the internet (the cloud).',
                'services': ['IaaS (Infrastructure)', 'PaaS (Platform)', 'SaaS (Software)'],
                'providers': 'AWS, Google Cloud, Microsoft Azure, IBM Cloud',
                'benefits': 'Scalability, Cost-effective, Accessibility, Reliability'
            },
            'algorithm': {
                'definition': 'An algorithm is a step-by-step procedure or formula for solving a problem or completing a task.',
                'characteristics': ['Finite', 'Well-defined', 'Effective', 'Independent'],
                'types': 'Sorting, Searching, Graph algorithms, Dynamic programming',
                'examples': 'Binary Search, Quick Sort, Dijkstra\'s Algorithm, BFS/DFS'
            },
            'react': {
                'definition': 'React is a JavaScript library for building user interfaces, particularly single-page applications.',
                'features': ['Component-based', 'Virtual DOM', 'JSX syntax', 'Unidirectional data flow'],
                'uses': 'Web applications, Mobile apps (React Native)',
                'created_by': 'Facebook (now Meta) in 2013'
            }
        }
    
    def _initialize_patterns(self) -> Dict:
        """Initialize intent patterns and responses."""
        return {
            'greeting': {
                'patterns': [
                    r'^(hi|hello|hey|greetings|good\s+(morning|afternoon|evening)|howdy|sup|yo)\b',
                    r'^(what\'s up|whats up|how are you|how do you do)',
                ],
                'responses': [
                    "Hello! 👋 How can I help you today?",
                    "Hi there! I'm TechBot, ready to assist you!",
                    "Hey! Great to see you! What can I do for you?",
                    "Greetings! How may I be of service?",
                    "Hello! Ask me anything about technology and programming!",
                ]
            },
            
            'farewell': {
                'patterns': [
                    r'^(bye|goodbye|see you|farewell|take care|later|exit|quit)\b',
                    r'^(good night|gn|have a good day|catch you later)',
                ],
                'responses': [
                    "Goodbye! Feel free to come back anytime! 👋",
                    "See you later! Happy coding! 💻",
                    "Take care! Don't hesitate to return if you need help!",
                    "Bye! It was great chatting with you!",
                    "Farewell! Keep learning and building great things! 🚀",
                ]
            },
            
            'help': {
                'patterns': [
                    r'^(help|assist|support|guide|what can you do|your capabilities)\b',
                    r'^(how do you work|how to use|instructions|commands)',
                    r'^(i need help|can you help)',
                ],
                'responses': [
                    """I can help you with:
• Programming languages (Python, JavaScript, Java, C++, Ruby, React)
• Tech concepts (AI, ML, APIs, Databases, Git, Cloud Computing)
• Algorithms and data structures
• General tech questions
• Small talk and jokes!

Just ask me anything!""",
                    """Here's what I can do:
✓ Explain programming concepts
✓ Discuss technologies
✓ Answer tech questions
✓ Have friendly conversations

Try asking: 'What is Python?' or 'Tell me about AI'""",
                ]
            },
            
            'thanks': {
                'patterns': [
                    r'^(thanks|thank you|thx|appreciate|grateful)\b',
                    r'^(thanks a lot|many thanks|thanks so much)',
                ],
                'responses': [
                    "You're welcome! Happy to help! 😊",
                    "My pleasure! Feel free to ask more questions!",
                    "Glad I could help! Anything else?",
                    "You're very welcome! That's what I'm here for!",
                    "No problem at all! Keep the questions coming!",
                ]
            },
            
            'about_bot': {
                'patterns': [
                    r'^(who are you|what are you|your name|introduce yourself)\b',
                    r'^(tell me about yourself|what is your purpose)',
                    r'^(are you (a )?bot|are you (an )?ai)',
                ],
                'responses': [
                    "I'm TechBot, a rule-based AI assistant! 🤖 I use pattern matching to understand your questions and provide helpful responses about technology and programming.",
                    "I'm an AI chatbot specialized in technology topics. I'm built using rule-based pattern matching and have a knowledge base of programming and tech concepts!",
                    "Call me TechBot! I'm here to answer your tech questions, explain programming concepts, and have friendly conversations. I'm powered by pattern matching rules!",
                ]
            },
            
            'joke': {
                'patterns': [
                    r'^(tell me a joke|joke|make me laugh|something funny|humor)\b',
                    r'^(got any jokes|do you know jokes)',
                ],
                'responses': [
                    "Why do programmers prefer dark mode? Because light attracts bugs! 😄🐛",
                    "Why did the programmer quit his job? Because he didn't get arrays! 😂",
                    "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
                    "What's a programmer's favorite hangout place? Foo Bar! 🍺",
                    "Why do Java developers wear glasses? Because they can't C#! 👓😄",
                    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I JOIN you?' 🍻",
                    "There are 10 types of people in the world: those who understand binary and those who don't! 😄",
                    "Why did the developer go broke? Because he used up all his cache! 💸",
                ]
            },
            
            'compliment': {
                'patterns': [
                    r'^(you are (great|awesome|amazing|cool|smart|brilliant|helpful))\b',
                    r'^(good bot|nice bot|you\'re the best)',
                    r'^(i like you|you rock)',
                ],
                'responses': [
                    "Thank you! You're pretty awesome yourself! 🌟",
                    "Aww, thanks! You made my circuits happy! 😊",
                    "You're too kind! I'm just doing my job! 🤖",
                    "Thanks! I really appreciate that! Keep being awesome!",
                ]
            },
            
            'mood': {
                'patterns': [
                    r'^(how are you|how do you feel|are you okay|you good)\b',
                    r'^(what\'s your mood|how\'s it going)',
                ],
                'responses': [
                    "I'm doing great! All systems operational! 🚀 How about you?",
                    "Feeling fantastic! Ready to help with any tech questions! 😊",
                    "I'm excellent! My databases are optimized and I'm ready to chat! 💪",
                    "Running at peak performance! What can I help you with today?",
                ]
            },
            
            'learning': {
                'patterns': [
                    r'^(i want to learn|teach me|how to learn|how do i start)\b',
                    r'^(best way to learn|where to start|beginner)',
                ],
                'responses': [
                    """Great mindset! 🎓 For programming, I recommend:
1. Start with Python (beginner-friendly)
2. Practice daily with small projects
3. Use resources like freeCodeCamp, Codecademy
4. Build real projects
5. Join coding communities

What specifically interests you?""",
                    """Awesome! Learning is the best investment! 💡
- Pick a language (Python is great for beginners)
- Do online tutorials
- Code every day (even 30 minutes helps)
- Build projects that interest you
- Learn from mistakes

Would you like recommendations for a specific topic?""",
                ]
            },
            
            'time': {
                'patterns': [
                    r'^(what time|what\'s the time|current time|time now)\b',
                    r'^(what day|what date|today\'s date)',
                ],
                'handler': lambda: f"The current time is {datetime.now().strftime('%I:%M %p')} and today is {datetime.now().strftime('%A, %B %d, %Y')}. ⏰"
            },
            
            'weather': {
                'patterns': [
                    r'^(how\'s the weather|what\'s the weather|weather|is it raining|is it sunny)\b',
                ],
                'responses': [
                    "I don't have access to weather data, but I hope it's nice where you are! ☀️ Want to talk about something tech-related instead?",
                    "As a chatbot, I live in the cloud! ☁️ But I can't check the weather. How about we discuss cloud computing instead? 😄",
                ]
            },
            
            'capabilities': {
                'patterns': [
                    r'^(what do you know|what can you tell me|topics you know)\b',
                ],
                'responses': [
                    f"""I have knowledge about:

Programming Languages:
• {', '.join([k.title() for k in self.knowledge_base.keys() if k in ['python', 'javascript', 'java', 'c++', 'ruby']])}

Technologies & Concepts:
• {', '.join([k.upper() if k == 'ai' else k.title() for k in self.knowledge_base.keys() if k in ['ai', 'machine learning', 'api', 'database', 'git', 'cloud computing', 'algorithm', 'react']])}

Ask me about any of these topics!"""
                ]
            },
        }
    
    def _handle_knowledge_query(self, topic: str) -> Optional[str]:
        """Handle queries about knowledge base topics."""
        normalized_topic = topic.lower().strip()
        knowledge = self.knowledge_base.get(normalized_topic)
        
        if knowledge:
            response_parts = [f"📚 {topic.upper()}\n"]
            response_parts.append(f"{knowledge['definition']}\n")
            
            if 'features' in knowledge:
                response_parts.append(f"✨ Key Features:")
                for feature in knowledge['features']:
                    response_parts.append(f"  • {feature}")
                response_parts.append("")
            
            if 'types' in knowledge:
                if isinstance(knowledge['types'], list):
                    response_parts.append(f"📂 Types:")
                    for t in knowledge['types']:
                        response_parts.append(f"  • {t}")
                elif isinstance(knowledge['types'], dict):
                    response_parts.append(f"📂 Types:")
                    for key, val in knowledge['types'].items():
                        response_parts.append(f"  • {key}: {val}")
                response_parts.append("")
            
            if 'subfields' in knowledge:
                response_parts.append(f"🔬 Subfields:")
                for subfield in knowledge['subfields']:
                    response_parts.append(f"  • {subfield}")
                response_parts.append("")
            
            if 'uses' in knowledge:
                response_parts.append(f"💼 Uses: {knowledge['uses']}")
            
            if 'applications' in knowledge:
                response_parts.append(f"💼 Applications: {knowledge['applications']}")
            
            if 'algorithms' in knowledge:
                response_parts.append(f"🧮 Common Algorithms: {knowledge['algorithms']}")
            
            if 'difficulty' in knowledge:
                response_parts.append(f"📊 Difficulty: {knowledge['difficulty']}")
            
            if 'commands' in knowledge:
                response_parts.append(f"⌨️  Common Commands: {knowledge['commands']}")
            
            if 'platforms' in knowledge:
                response_parts.append(f"🌐 Platforms: {knowledge['platforms']}")
            
            if 'benefits' in knowledge:
                response_parts.append(f"✅ Benefits: {knowledge['benefits']}")
            
            return '\n'.join(response_parts)
        
        return None
    
    def _match_pattern(self, user_input: str) -> Tuple[str, str]:
        """Match user input against patterns to determine intent and response."""
        input_lower = user_input.lower().strip()
        
        # First, check for knowledge base queries
        for topic in self.knowledge_base.keys():
            patterns = [
                rf'\b(what is|tell me about|explain|define)\s+{re.escape(topic)}\b',
                rf'^{re.escape(topic)}\??$',
            ]
            for pattern in patterns:
                if re.search(pattern, input_lower):
                    response = self._handle_knowledge_query(topic)
                    if response:
                        return response, f'knowledge:{topic}'
        
        # Then check intent patterns
        for intent_name, intent_data in self.patterns.items():
            for pattern in intent_data['patterns']:
                if re.search(pattern, input_lower, re.IGNORECASE):
                    # Check for custom handler
                    if 'handler' in intent_data:
                        response = intent_data['handler']()
                        return response, intent_name
                    
                    # Random response from list
                    if 'responses' in intent_data:
                        response = random.choice(intent_data['responses'])
                        return response, intent_name
        
        # Fallback response
        return self._get_fallback_response(), 'unknown'
    
    def _get_fallback_response(self) -> str:
        """Get a fallback response for unrecognized input."""
        fallbacks = [
            "I'm not sure I understand. Could you rephrase that? Try asking about programming languages, tech concepts, or type 'help' for guidance! 🤔",
            "Hmm, that's interesting but I'm not quite sure how to respond. Ask me about Python, JavaScript, AI, or other tech topics! 💡",
            "I didn't quite catch that. I'm best at discussing technology and programming. What would you like to know? 🖥️",
            "That's outside my knowledge base. Try asking: 'What is Python?' or 'Tell me about AI' or 'help' to see what I can do! 🤖",
            "I'm not familiar with that topic. I specialize in programming and technology. Type 'help' to see what I can assist with! 📚",
        ]
        return random.choice(fallbacks)
    
    def chat(self, user_input: str) -> Tuple[str, str]:
        """Process user input and return bot response with intent."""
        timestamp = datetime.now().isoformat()
        
        # Log user message
        self.conversation_history.append({
            'role': 'user',
            'message': user_input,
            'timestamp': timestamp
        })
        
        # Get response
        response, intent = self._match_pattern(user_input)
        
        # Track intent
        if intent != 'unknown':
            self.intent_counts[intent] = self.intent_counts.get(intent, 0) + 1
        
        # Log bot response
        self.conversation_history.append({
            'role': 'bot',
            'message': response,
            'intent': intent,
            'timestamp': datetime.now().isoformat()
        })
        
        return response, intent
    
    def get_history(self) -> List[Dict]:
        """Get conversation history."""
        return self.conversation_history
    
    def get_stats(self) -> Dict:
        """Get conversation statistics."""
        return {
            'total_messages': len(self.conversation_history),
            'user_messages': len([m for m in self.conversation_history if m['role'] == 'user']),
            'bot_messages': len([m for m in self.conversation_history if m['role'] == 'bot']),
            'intent_counts': self.intent_counts,
            'total_intents': len(self.intent_counts),
            'unique_intents': list(self.intent_counts.keys())
        }
    
    def export_history(self, filename: str = 'chat_history.txt') -> None:
        """Export conversation history to a file."""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("CONVERSATION HISTORY\n")
            f.write("="*80 + "\n\n")
            
            for entry in self.conversation_history:
                timestamp = datetime.fromisoformat(entry['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
                role = entry['role'].upper()
                message = entry['message']
                
                f.write(f"[{timestamp}] {role}:\n")
                f.write(f"{message}\n")
                
                if 'intent' in entry:
                    f.write(f"(Intent: {entry['intent']})\n")
                
                f.write("\n" + "-"*80 + "\n\n")
            
            # Add statistics
            stats = self.get_stats()
            f.write("\n" + "="*80 + "\n")
            f.write("STATISTICS\n")
            f.write("="*80 + "\n")
            f.write(f"Total Messages: {stats['total_messages']}\n")
            f.write(f"User Messages: {stats['user_messages']}\n")
            f.write(f"Bot Messages: {stats['bot_messages']}\n")
            f.write(f"Unique Intents Detected: {stats['total_intents']}\n")
            f.write(f"Intent Breakdown:\n")
            for intent, count in stats['intent_counts'].items():
                f.write(f"  • {intent}: {count}\n")
        
        print(f"\n✅ Conversation history exported to {filename}")
    
    def export_history_json(self, filename: str = 'chat_history.json') -> None:
        """Export conversation history as JSON."""
        data = {
            'conversation': self.conversation_history,
            'statistics': self.get_stats(),
            'exported_at': datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Conversation history exported to {filename}")
    
    def clear_history(self) -> None:
        """Clear conversation history."""
        self.conversation_history.clear()
        self.intent_counts.clear()


def print_header():
    """Print chatbot header."""
    print("\n" + "="*80)
    print("🤖 TECHBOT AI - RULE-BASED CHATBOT")
    print("="*80)
    print("\nWelcome! I'm a rule-based AI assistant specializing in technology and programming.")
    print("I use pattern matching to understand your questions and provide helpful responses.")
    print("\nType 'help' to see what I can do, or 'quit' to exit.")
    print("-"*80 + "\n")


def print_menu():
    """Print interactive menu."""
    print("\n" + "─"*80)
    print("MENU")
    print("─"*80)
    print("1. Chat with the bot")
    print("2. View conversation history")
    print("3. View statistics")
    print("4. Export history (TXT)")
    print("5. Export history (JSON)")
    print("6. Clear history")
    print("7. View knowledge base topics")
    print("8. Exit")
    print("─"*80)


def view_history(chatbot: RuleBasedChatbot):
    """Display conversation history."""
    history = chatbot.get_history()
    
    if not history:
        print("\n⚠️  No conversation history yet.")
        return
    
    print("\n" + "="*80)
    print("CONVERSATION HISTORY")
    print("="*80 + "\n")
    
    for entry in history:
        timestamp = datetime.fromisoformat(entry['timestamp']).strftime('%H:%M:%S')
        role = entry['role'].upper()
        message = entry['message']
        
        print(f"[{timestamp}] {role}:")
        print(f"{message}")
        
        if 'intent' in entry:
            print(f"(Intent: {entry['intent']})")
        
        print()


def view_statistics(chatbot: RuleBasedChatbot):
    """Display conversation statistics."""
    stats = chatbot.get_stats()
    
    print("\n" + "="*80)
    print("CONVERSATION STATISTICS")
    print("="*80)
    print(f"\nTotal Messages: {stats['total_messages']}")
    print(f"User Messages: {stats['user_messages']}")
    print(f"Bot Messages: {stats['bot_messages']}")
    print(f"Unique Intents Detected: {stats['total_intents']}")
    
    if stats['intent_counts']:
        print(f"\nIntent Breakdown:")
        for intent, count in sorted(stats['intent_counts'].items(), key=lambda x: x[1], reverse=True):
            print(f"  • {intent}: {count}")
    
    print("\n" + "="*80)


def view_topics(chatbot: RuleBasedChatbot):
    """Display available knowledge base topics."""
    print("\n" + "="*80)
    print("KNOWLEDGE BASE TOPICS")
    print("="*80)
    
    topics = list(chatbot.knowledge_base.keys())
    
    print("\nProgramming Languages:")
    prog_langs = [t for t in topics if t in ['python', 'javascript', 'java', 'c++', 'ruby']]
    for lang in prog_langs:
        print(f"  • {lang.title()}")
    
    print("\nTechnologies & Concepts:")
    tech_topics = [t for t in topics if t not in prog_langs]
    for topic in tech_topics:
        display_name = topic.upper() if topic == 'ai' else topic.title()
        print(f"  • {display_name}")
    
    print("\n" + "="*80)
    print("Ask me about any of these topics!")
    print("Example: 'What is Python?' or 'Tell me about AI'")
    print("="*80)


def chat_mode(chatbot: RuleBasedChatbot):
    """Interactive chat mode."""
    print("\n" + "─"*80)
    print("CHAT MODE (type 'back' to return to menu)")
    print("─"*80 + "\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['back', 'menu']:
                break
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                response, _ = chatbot.chat(user_input)
                print(f"\nBot: {response}\n")
                return True  # Signal to exit program
            
            response, intent = chatbot.chat(user_input)
            print(f"\nBot: {response}")
            print(f"[Intent: {intent}]\n")
            
        except KeyboardInterrupt:
            print("\n\nReturning to menu...")
            break
        except EOFError:
            break
    
    return False


def main():
    """Main function to run the chatbot."""
    chatbot = RuleBasedChatbot()
    print_header()
    
    # Auto-start in chat mode
    should_exit = chat_mode(chatbot)
    if should_exit:
        return
    
    # Menu loop
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                should_exit = chat_mode(chatbot)
                if should_exit:
                    break
            
            elif choice == '2':
                view_history(chatbot)
            
            elif choice == '3':
                view_statistics(chatbot)
            
            elif choice == '4':
                filename = input("Enter filename (default: chat_history.txt): ").strip()
                if not filename:
                    filename = 'chat_history.txt'
                chatbot.export_history(filename)
            
            elif choice == '5':
                filename = input("Enter filename (default: chat_history.json): ").strip()
                if not filename:
                    filename = 'chat_history.json'
                chatbot.export_history_json(filename)
            
            elif choice == '6':
                if input("Clear all history? (yes/no): ").lower() == 'yes':
                    chatbot.clear_history()
                    print("\n✅ History cleared.")
            
            elif choice == '7':
                view_topics(chatbot)
            
            elif choice == '8':
                print("\n👋 Thank you for using TechBot AI! Goodbye!\n")
                break
            
            else:
                print("\n Invalid choice. Please select 1-8.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except EOFError:
            break


if __name__ == "__main__":
    main()
