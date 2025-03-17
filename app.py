import streamlit as st

# Define the quiz questions and answers (related to Pakistan)
quiz_data = [
    {"question": "What is the capital of Pakistan?", 
     "options": ["Karachi", "Islamabad", "Lahore", "Quetta"], 
     "answer": "Islamabad"},
    
    {"question": "Who was the founder of Pakistan?", 
     "options": ["Allama Iqbal", "Zulfikar Ali Bhutto", "Quaid-e-Azam Muhammad Ali Jinnah", "Benazir Bhutto"], 
     "answer": "Quaid-e-Azam Muhammad Ali Jinnah"},
    
    {"question": "Which is the national flower of Pakistan?", 
     "options": ["Rose", "Sunflower", "Jasmine", "Lotus"], 
     "answer": "Jasmine"},
    
    {"question": "Which is the largest city in Pakistan by population?", 
     "options": ["Karachi", "Lahore", "Rawalpindi", "Multan"], 
     "answer": "Karachi"},
    
    {"question": "In which year Pakistan became independent?", 
     "options": ["1947", "1950", "1965", "1971"], 
     "answer": "1947"},
    
    
    {"question": "Who was the first Prime Minister of Pakistan?", 
     "options": ["Liaquat Ali Khan", "Zulfikar Ali Bhutto", "Imran Khan", "Benazir Bhutto"], 
     "answer": "Liaquat Ali Khan"},
    
    {"question": "Which mountain range is located in the north of Pakistan?", 
     "options": ["Himalayas", "Karakoram", "Alps", "Andes"], 
     "answer": "Karakoram"},
    
    {"question": "Which Pakistani cricketer is known as 'The Rawalpindi Express'?", 
     "options": ["Wasim Akram", "Shoaib Akhtar", "Imran Khan", "Javed Miandad"], 
     "answer": "Shoaib Akhtar"},
    
    {"question": "What is the national animal of Pakistan?", 
     "options": ["Lion", "Markhor", "Tiger", "Elephant"], 
     "answer": "Markhor"},
    
    {"question": "What is the currency of Pakistan?", 
     "options": ["Rupee", "Dollar", "Yen", "Pound"], 
     "answer": "Rupee"},
    
    {"question": "Which famous Pakistani poet is known as 'Mufakkir-e-Pakistan' (The Thinker of Pakistan)?", 
     "options": ["Allama Iqbal", "Faiz Ahmed Faiz", "Ahmed Faraz", "Ghulam Ahmed Pervez"], 
     "answer": "Allama Iqbal"}
]

# App title with an emoji
st.title("Pakistan Quiz App 🎉")

# Function to display the quiz and calculate the score
def run_quiz():
    score = 0
    total_questions = len(quiz_data)
    
    # Loop through the quiz data and display questions with options
    for i, question_data in enumerate(quiz_data):
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["answer"]
        
        # Display question and options
        st.subheader(f"Q{i+1}: {question}")
        user_answer = st.radio(f"Choose an answer for Q{i+1}:", options)
        
        # Check if the user's answer is correct
        if user_answer == correct_answer:
            score += 1

    # Show the final score
    st.write(f"Your final score is: {score}/{total_questions} 🏆")
    if score == total_questions:
        st.success("Congratulations! You got all the answers correct! 🎉🎉")
    elif score > total_questions // 2:
        st.success(f"Great job! You got {score} out of {total_questions} right! 👍")
    else:
        st.warning(f"You scored {score}/{total_questions}. Better luck next time! ✨")

# Add a button to start the quiz
if st.button("Start Quiz 🚀"):
    run_quiz()
