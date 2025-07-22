import datetime

chat_log = []

def log(message):
    chat_log.append(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}")

def greet_user():
    print("👋 Welcome to the Student Helpdesk Chatbot!")
    print("Type your query or type 'help' to see options.\n")
    log("Bot: Greeted user")

def show_menu():
    print("🔹 You can ask things like:")
    print(" - What is the last date for fee payment?")
    print(" - Show faculty contacts for Computer Science")
    print(" - What are the elective courses in semester 4?")
    print(" - Exit")
    log("Bot: Displayed menu")

def get_fee_deadline():
    response = "📌 The last date for fee payment is **August 15, 2025**."
    print(response)
    log("Bot: " + response)

def get_faculty_contacts(dept):
    contacts = {
        "computer science": ["Dr. A. Mehta - cse@college.edu", "Prof. K. Rao - krao@college.edu"],
        "electronics": ["Dr. L. Verma - ece@college.edu", "Prof. D. Singh - dsingh@college.edu"]
    }
    response = contacts.get(dept.lower(), "❌ Department not found. Try 'Computer Science' or 'Electronics'.")
    if isinstance(response, list):
        print("📞 Faculty Contacts for", dept.title() + ":")
        for contact in response:
            print(" -", contact)
    else:
        print(response)
    log(f"Bot: Faculty contact response for {dept}")

def get_electives(semester):
    electives = {
        "4": ["AI Basics", "Cybersecurity", "IoT Fundamentals"],
        "5": ["Machine Learning", "Blockchain", "Mobile App Development"]
    }
    response = electives.get(semester, "❌ Elective courses not available for that semester.")
    if isinstance(response, list):
        print(f"📚 Elective Courses in Semester {semester}:")
        for course in response:
            print(" -", course)
    else:
        print(response)
    log(f"Bot: Electives response for semester {semester}")

def save_chat_log():
    with open("chat_log.txt", "w") as file:
        for entry in chat_log:
            file.write(entry + "\n")
    print("💾 Chat log saved as 'chat_log.txt'.")

def main():
    greet_user()
    while True:
        user_input = input("\nYou: ").strip()
        log("User: " + user_input.lower())

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Have a great day.")
            log("Bot: Session ended")
            break
        elif "fee" in user_input.lower() and "last date" in user_input.lower():
            get_fee_deadline()
        elif "faculty contacts" in user_input.lower():
            if "computer science" in user_input.lower():
                get_faculty_contacts("computer science")
            elif "electronics" in user_input.lower():
                get_faculty_contacts("electronics")
            else:
                print("❓ Please specify department like 'Computer Science' or 'Electronics'.")
                log("Bot: Asked for department clarification")
        elif "elective" in user_input.lower() and "semester" in user_input.lower():
            for word in user_input.split():
                if word.isdigit():
                    get_electives(word)
                    break
            else:
                print("❓ Please specify semester number.")
        elif user_input.lower() == "help":
            show_menu()
        else:
            print("🤖 Sorry, I didn't understand that. Try asking something else or type 'help'.")
            log("Bot: Fallback message")

    save_chat_log()

if __name__ == "__main__":
    main()
