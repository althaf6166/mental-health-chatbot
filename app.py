from flask import Flask, request, render_template
from random import choice

app = Flask(__name__)

# Expanded sample responses
responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What’s on your mind?",
        "Hey! I’m here to listen to you.",
        "Greetings! What would you like to talk about today?",
        "Hi! I’m all ears. What’s on your mind?"
    ],
    "feelings": [
        "It's completely normal to feel that way. Would you like to talk more about it?",
        "Acknowledging your feelings is a great first step. What’s been bothering you?",
        "Feelings can be tough to navigate. I'm here to help.",
        "It's okay to have ups and downs. What's been weighing on your heart?",
        "Your feelings are valid, and it's important to express them. Can you share more?"
    ],
    "support": [
        "You're not alone in this. It's okay to ask for help.",
        "Reaching out for support is important. Who do you feel comfortable talking to?",
        "Support systems are vital. Have you considered talking to someone about your feelings?",
        "It's brave to seek support. Do you have friends or family you trust?",
        "Sometimes sharing your thoughts can lighten the load. I'm here to listen."
    ],
    "self-care": [
        "Building self-esteem is a journey. Focus on things you’re proud of, no matter how small. Remember, you’re valuable and worthy just as you are.",
        "Self-care is essential. What activities make you feel good?",
        "Taking time for yourself is important. Have you tried any new hobbies lately?",
        "Consider practicing mindfulness or meditation. It can help clear your mind.",
        "Regular exercise and healthy eating can boost your mood. Have you been able to focus on those?"
    ],
    "overthinking": [
        "Overthinking can be exhausting. Try focusing on the present moment. Journaling or doing something creative can also help.",
        "It's easy to get caught in a loop of thoughts. Have you tried grounding techniques?",
        "Taking a break from your thoughts can be helpful. What do you enjoy doing to distract yourself?",
        "Sometimes, stepping back can give you a new perspective. What’s been on your mind?",
        "Breaking tasks into smaller steps can ease your mind. Is there something specific you're overthinking?"
    ],
    "anxiety": [
        "When anxiety hits, take a few deep breaths and focus on what's around you. You're not alone.",
        "Anxiety can feel overwhelming. Have you tried any relaxation techniques?",
        "It's important to recognize your triggers. What typically makes you feel anxious?",
        "Consider reaching out to a friend when you're feeling anxious. Talking helps!",
        "You are strong for facing your anxiety. What small steps can you take today?"
    ],
    "depression": [
        "It's okay not to feel okay all the time. Talking to someone you trust can make a difference.",
        "Depression can feel isolating. Remember, support is available.",
        "Have you considered professional help? It can be beneficial.",
        "You are not alone in this struggle. What small thing can you do to care for yourself today?",
        "Finding joy in small things can be a start. What used to make you happy?"
    ],
    "loneliness": [
        "Loneliness is hard, but reaching out to someone might help. You’re not alone.",
        "Building connections takes time, but it's worth it. Do you have friends you can reach out to?",
        "Consider joining a club or group that interests you. It’s a great way to meet new people.",
        "Sharing your feelings of loneliness can sometimes lift the weight. Want to talk about it?",
        "You're valuable, and your company matters. How can I support you?"
    ],
    "sleep": [
        "Establish a calming bedtime routine and avoid screens close to bedtime for better sleep.",
        "Sleep is vital for mental health. Have you tried setting a regular sleep schedule?",
        "Consider creating a relaxing environment in your bedroom. What helps you unwind?",
        "If racing thoughts keep you awake, journaling before bed can help clear your mind.",
        "A warm bath or reading can also promote better sleep. What do you usually do to relax?"
    ],
    "professional_help": [
        "If you’re feeling overwhelmed, talking to a mental health professional could be very helpful.",
        "Seeking help is a sign of strength. Have you thought about which resources might be available?",
        "A therapist can provide support tailored to your needs. Would you like more information?",
        "Sometimes a professional perspective can offer new insights. What concerns you the most?",
        "It's important to prioritize your mental health. Have you looked into local support groups?"
    ],
    "motivation": [
        "Start with small, manageable steps. It’s okay to take breaks and give yourself grace.",
        "Finding motivation can be challenging. What are your goals right now?",
        "Consider setting up a reward system for completing tasks. What motivates you?",
        "Sometimes, the first step is the hardest. What is one thing you can do today?",
        "Visualizing your success can help. Where do you see yourself in a month?"
    ],
    "relationship": [
        "Honest communication about feelings can make a difference. Talking with a trusted friend can also help.",
        "Every relationship has its challenges. What’s been on your mind regarding your relationships?",
        "Consider expressing your thoughts directly. It's important to be heard.",
        "Building trust takes time. How can you nurture your relationships?",
        "Have you had a heart-to-heart with someone close to you lately? It might help."
    ],
    "default": [
        "I’m here to support you, but I didn’t quite understand that. Could you share more?",
        "Thank you for reaching out. I may not have fully understood, but feel free to tell me more.",
        "I'm here to listen. What would you like to talk about?",
        "It sounds like there’s something on your mind. Can you clarify for me?",
        "I'm eager to help you. Can you provide more details about what you're feeling?"
    ]
}

def get_response(user_input):
    """Determine an appropriate response based on user input."""
    user_input = user_input.lower()
    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return choice(responses["greeting"])
    elif any(feel in user_input for feel in ["sad", "depressed", "down", "unhappy"]):
        return choice(responses["feelings"])
    elif any(support in user_input for support in ["support", "need someone"]):
        return choice(responses["support"])
    elif any(care in user_input for care in ["self-care", "relax", "unwind"]):
        return choice(responses["self-care"])
    elif any(overthink in user_input for overthink in ["overthinking", "think too much"]):
        return choice(responses["overthinking"])
    elif any(anxiety in user_input for anxiety in ["anxiety", "nervous", "worried"]):
        return choice(responses["anxiety"])
    elif any(depress in user_input for depress in ["depression", "feel hopeless"]):
        return choice(responses["depression"])
    elif any(lonely in user_input for lonely in ["loneliness", "alone"]):
        return choice(responses["loneliness"])
    elif any(sleep in user_input for sleep in ["sleep", "tired"]):
        return choice(responses["sleep"])
    elif any(help in user_input for help in ["professional help", "therapist"]):
        return choice(responses["professional_help"])
    elif any(motivate in user_input for motivate in ["motivation", "unmotivated"]):
        return choice(responses["motivation"])
    elif any(relate in user_input for relate in ["relationship", "partner"]):
        return choice(responses["relationship"])
    return choice(responses["default"])

@app.route("/", methods=["GET"])
def main_page():
    """Render the main page with the welcome message."""
    return render_template("main.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    """Handle user input and respond."""
    response_text = ""
    if request.method == "POST":
        user_message = request.form.get("message", "").strip()
        response_text = get_response(user_message)

    return render_template("chat.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
