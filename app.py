import streamlit as st
import random
import datetime

# Question Bank


# question_bank = {
#     "Basic Concept of Ratios": [
#         # Easy Questions (11)
#     ],
#     "Comparing Ratios": [
#         # Add 20 categorized questions for Comparing Ratios
#     ],
#     "Proportions": [
#         # Add 20 categorized questions for Proportions
#     ],
#     "Word Problems on Ratio": [
#         # Add 20 categorized questions for Word Problems
#     ],
#     "Unitary Method": [
#         # Add 20 categorized questions for Unitary Method
#     ],
#     "Problems Involving Ratios": [
#         # Add 20 categorized questions for Problems Involving Ratios
#     ],
#     "Real-Life Applications": [
#         # Add 20 categorized questions for Real-Life Applications
#     ],
#     "Miscellaneous": [
#         # Add 20 categorized questions for Miscellaneous topics
#     ]
# }



question_bank = {
    "Basic Concept of Ratios": [
        # Easy Questions (11)
        {"question": "Write the ratio of 8 pens to 24 pens in its simplest form.", "answer": "1:3"},
        {"question": "If the ratio of apples to bananas is 3:4 and there are 21 apples, how many bananas are there?", "answer": "28"},
        {"question": "Simplify the ratio 15:45.", "answer": "1:3"},
        {"question": "Write the ratio of 12 hours to 1 day in simplest form.", "answer": "1:2"},
        {"question": "What is the ratio of 500 g to 2 kg?", "answer": "1:4"},
        {"question": "Write the ratio of 25 paise to 1 in its simplest form.", "answer": "1:4"},
        {"question": "Simplify the ratio 20:30.", "answer": "2:3"},
        {"question": "Write the ratio of 6 meters to 12 meters.", "answer": "1:2"},
        {"question": "Express the ratio 1 dozen:2 dozen in simplest form.", "answer": "1:2"},
        {"question": "If the ratio of boys to girls in a class is 2:3 and there are 10 boys, how many girls are there?", "answer": "15"},
        {"question": "Convert the ratio 500:2000 into its simplest form.", "answer": "1:4"},
        # Medium Questions (6)
        {"question": "Simplify the ratio 750 m to 1.5 km.", "answer": "1:2"},
        {"question": "Write the ratio of 45 minutes to 2 hours.", "answer": "3:8"},
        {"question": "The weights of two dogs are 12 kg and 16 kg. What is their ratio in simplest form?", "answer": "3:4"},
        {"question": "Write the ratio of 7:35 in simplest form.", "answer": "1:5"},
        {"question": "A basket contains 40 marbles, 8 of which are red. What is the ratio of red marbles to total marbles?", "answer": "1:5"},
        {"question": "If a recipe uses sugar and flour in the ratio 3:5 and there are 15 cups of flour, how much sugar is needed?", "answer": "9"},
        # Hard Questions (3)
        {"question": "The ratio of angles in a triangle is 2:3:4. Find the angles.", "answer": "40, 60, 80"},
        {"question": "Express the ratio of 2 liters to 250 ml in simplest form.", "answer": "8:1"},
        {"question": "If the ratio of boys to girls in a school is 7:5 and there are 364 boys, how many girls are there?", "answer": "260"},
    ],
    "Comparing Ratios": [
        {"question": "Compare the ratios 4:5 and 6:7.", "answer": "4:5 is smaller"},
        {"question": "Which is larger, the ratio 3:4 or 7:8?", "answer": "7:8"},
        {"question": "Is 8:10 equivalent to 4:5?(Yes or no)", "answer": "Yes"},
        {"question": "Compare the ratios 9:12 and 3:4. (equal/greater/lesser)", "answer": "equal"},
        {"question": "Which is greater, 5:6 or 10:11?", "answer": "10:11"},
        {"question": "Are 15:45 and 1:3 equivalent?(Yes or no)", "answer": "Yes"},
        {"question": "Compare 1:2 and 2:3.", "answer": "2:3 is larger"},
        {"question": "Is the ratio 25:100 equal to 1:4?(Yes or no)", "answer": "Yes"},
        {"question": "Which is smaller, 5:9 or 6:11?", "answer": "5:9"},
        {"question": "Are 12:16 and 3:4 equivalent?(Yes or no)", "answer": "Yes"},
        {"question": "Compare 7:8 and 13:15.", "answer": "7:8 is larger"},
        {"question": "Which is larger, 10:20 or 7:14? (equal/greater/lesser)", "answer": "equal"},
        {"question": "Are 14:28 and 1:2 equivalent?(Yes or no)", "answer": "Yes"},
        {"question": "Compare 3:5 and 9:15. (equal/greater/lesser)", "answer": "equal"},
        {"question": "Which is larger, 1:3 or 3:9? (equal/greater/lesser)", "answer": "equal"},
        {"question": "Is 6:18 equivalent to 1:3?(Yes or no)", "answer": "Yes"},
        {"question": "Compare 4:7 and 8:14.", "answer": "8:14 is larger"},
        {"question": "Which is smaller, 2:3 or 4:5?", "answer": "2:3"},
        {"question": "Is 18:36 equivalent to 1:2?(Yes or no)", "answer": "Yes"},
        {"question": "Compare 5:8 and 10:16. (equal/greater/lesser)", "answer": "equal"},
    ],
    "Proportions": [
        {"question": "Is 3:5 :: 6:10 a proportion?(Yes or no)", "answer": "Yes"},
        {"question": "Solve for x: 2:5 = x:10.", "answer": "4"},
        {"question": "Is 4:6 :: 2:3 a proportion?(Yes or no)", "answer": "Yes"},
        {"question": "Solve for y: 9:y = 3:4.", "answer": "12"},
        {"question": "Are 5:8 :: 15:24 proportional?(Yes or no)", "answer": "Yes"},
        {"question": "Solve for z: 7:14 = z:28.", "answer": "14"},
        {"question": "Is 10:15 :: 2:3 a proportion?(Yes or no)", "answer": "Yes"},
        {"question": "Solve for w: w:6 = 10:15.", "answer": "4"},
        {"question": "Are 8:12 and 10:15 proportional?(Yes or no)", "answer": "Yes"},
        {"question": "Solve for x: x:8 = 12:16.", "answer": "6"},
        {"question": "Are 9:12 :: 6:8 proportional?(Yes or no)", "answer": "Yes"},
        {"question": "Solve for a: 4:a = 3:6.", "answer": "8"},
        {"question": "Is 5:7 :: 10:14 a proportion?(Yes or no)", "answer": "Yes"},
        {"question": "Solve for b: b:9 = 5:15.", "answer": "3"},
        {"question": "Are 3:4 :: 6:8 proportional?(Yes or no)", "answer": "Yes"},
        {"question": "Solve for c: c:12 = 8:24.", "answer": "4"},
        {"question": "Is 6:10 :: 12:20 a proportion?(Yes or no)", "answer": "Yes"},
        {"question": "Solve for d: 2:d = 6:12.", "answer": "4"},
        {"question": "Are 7:9 :: 14:18 proportional?(Yes or no)", "answer": "Yes"},
        {"question": "Solve for e: e:5 = 10:25.", "answer": "2"},
    ],
    "Word Problems on Ratio": [
        {"question": "The ratio of cats to dogs is 3:2. If there are 12 cats, how many dogs are there?", "answer": "8"},
        {"question": "A bag contains 6 red balls and 4 blue balls. What is the ratio of red to blue balls?", "answer": "3:2"},
        {"question": "The ratio of students to teachers is 30:1. If there are 60 students, how many teachers are there?", "answer": "2"},
        {"question": "Divide 500 between A and B in the ratio 3:2.", "answer": "300, 200"},
        {"question": "The ratio of pencils to erasers is 5:3. If there are 15 pencils, how many erasers are there?", "answer": "9"},
        {"question": "A car travels 240 km using 20 liters of fuel. What is the ratio of distance to fuel?", "answer": "12:1"},
        {"question": "The ratio of boys to girls in a class is 7:5. If there are 35 boys, how many girls are there?", "answer": "25"},
        {"question": "A ribbon is cut into two pieces in the ratio 2:3. If the longer piece is 15 cm, what is the length of the shorter piece?(in cm)", "answer": "10"},
        {"question": "A train travels 600 km in 5 hours. What is the ratio of distance to time?", "answer": "120:1"},
        {"question": "The ratio of mangoes to oranges in a basket is 3:4. If there are 12 mangoes, how many oranges are there?", "answer": "16"},
        {"question": "The cost of two pens is in the ratio 3:4. If the cheaper pen costs 9, what is the cost of the more expensive pen?", "answer": "12"},
        {"question": "The ages of two brothers are in the ratio 4:5. If the younger one is 20 years old, what is the age of the older brother?", "answer": "25"},
        {"question": "The profit earned by two businesses is in the ratio 7:8. If one business earns 56,000, what is the profit of the other?", "answer": "64,000"},
        {"question": "Divide 72 candies between two children in the ratio 5:4.", "answer": "40, 32"},
        {"question": "The ratio of the width to the length of a rectangle is 2:5. If the width is 10 cm, what is the length? (in cm)", "answer": "25"},
        {"question": "In a class, the ratio of boys to total students is 3:5. If there are 15 boys, what is the total number of students?", "answer": "25"},
        {"question": "A bag contains coins in the ratio 1:2:3 for 1, 2, and 5 coins. If there are 30 1 coins, how many 5 coins are there?", "answer": "90"},
        {"question": "The weights of two parcels are in the ratio 4:7. If the lighter parcel weighs 16 kg, what is the weight of the heavier parcel? (in km)", "answer": "28"},
        {"question": "Divide 600 among three people in the ratio 2:3:5.", "answer": "120,180,300"},
        {"question": "The price of two cars is in the ratio 7:9. If the cheaper car costs 14 lakh, what is the price of the more expensive car?(__ lakhs)", "answer": "18"},
    ],
    
     "Unitary Method": [
        {"question": "If the cost of 5 apples is 50, what is the cost of 1 apple?", "answer": "10"},
        {"question": "A car travels 180 km in 3 hours. How far will it travel in 5 hours?(in km)", "answer": "300"},
        {"question": "The cost of 8 pens is 96. What is the cost of 1 pen?", "answer": "12"},
        {"question": "A machine produces 240 items in 8 hours. How many items will it produce in 5 hours?", "answer": "150"},
        {"question": "If 6 kg of rice costs 300, what is the cost of 10 kg of rice?", "answer": "500"},
        {"question": "A car consumes 4 liters of petrol to cover 50 km. How far will it go on 10 liters of petrol?(in km)", "answer": "125"},
        {"question": "If 20 books cost 400, what is the cost of 1 book?", "answer": "20"},
        {"question": "A cyclist covers 90 km in 3 hours. How much distance will they cover in 7 hours?(in km)", "answer": "210"},
        {"question": "If 15 meters of cloth costs 450, what is the cost of 9 meters?", "answer": "270"},
        {"question": "A train runs at a speed of 60 km in 4 hours. How far will it travel in 2 hours?", "answer (in km)": "30"},
        {"question": "If 16 kg of wheat costs 320, what is the cost of 25 kg of wheat?", "answer": "500"},
        {"question": "A painter paints 45 square meters in 5 hours. How much can they paint in 8 hours?(in square meter)", "answer": "72"},
        {"question": "If 500 ml of milk costs 25, what is the cost of 2 liters?", "answer": "100"},
        {"question": "A farmer produces 400 kg of wheat in 4 days. How much can they produce in 10 days?(in kg)", "answer": "1000"},
        {"question": "If a person earns 480 in 8 hours, how much do they earn in 5 hours?", "answer": "300"},
        {"question": "A bus travels 120 km in 2 hours. What is its speed per hour?(in km/h)", "answer": "60 "},
        {"question": "If 3 packets of biscuits cost 75, what is the cost of 7 packets?", "answer": "175"},
        {"question": "A bakery makes 360 cookies in 6 hours. How many cookies can it make in 10 hours?", "answer": "600 cookies"},
        {"question": "If 9 chocolates cost 81, what is the cost of 15 chocolates?", "answer": "135"},
    ],
     
       "Problems Involving Ratios": [
        {"question": "The ratio of boys to girls in a school is 4:5. If there are 180 boys, how many girls are there?", "answer": "225"},
        {"question": "A company divides 50,000 among its employees in the ratio 3:2:5. How much does the employee with the largest share receive?", "answer": "25000"},
        {"question": "The ratio of two numbers is 7:11, and their sum is 90. What are the numbers?", "answer": "35,55"},
        {"question": "The ages of A and B are in the ratio 3:4. If the sum of their ages is 28, what is the age of A?", "answer": "12"},
        {"question": "Two quantities are in the ratio 5:8. If the smaller quantity is 25, what is the larger quantity?", "answer": "40"},
        {"question": "A bag contains red, blue, and green marbles in the ratio 3:4:5. If there are 36 marbles, how many are blue?", "answer": "12"},
        {"question": "The monthly income of A, B, and C is in the ratio 2:3:5. If A earns 20,000, what is the total income of B and C?", "answer": "80000"},
        {"question": "The weights of two parcels are in the ratio 2:3. If the heavier parcel weighs 45 kg, what is the weight of the lighter parcel?(in kg)", "answer": "30"},
        {"question": "A and B invest money in the ratio 7:3. If their total investment is 1,00,000, how much did A invest?(in Rs.)", "answer": "70000"},
        {"question": "The ratio of sugar to flour in a recipe is 1:4. If 250 grams of sugar is used, how much flour is required?(in kg)", "answer": "1"},
        {"question": "The ratio of boys to girls in a classroom is 5:6. If there are 33 students, how many are girls?", "answer": "18"},
        {"question": "The ratio of the length to the width of a rectangle is 3:2. If the length is 15 cm, what is the width?(in cm)", "answer": "10"},
        {"question": "Divide 720 between A and B in the ratio 5:7.", "answer": "300, 420"},
        {"question": "The ratio of the diameter to the radius of a circle is?", "answer": "2:1"},
        {"question": "The ratio of the sides of two squares is 3:4. What is the ratio of their areas?", "answer": "9:16"},
        {"question": "A fruit basket contains apples and oranges in the ratio 7:5. If there are 24 oranges, how many apples are there?", "answer": "28"},
        {"question": "A school has 120 students in Grade 6 and 180 students in Grade 7. What is the ratio of Grade 6 to Grade 7 students?", "answer": "2:3"},
        {"question": "The ratio of the speed of two cars is 4:5. If the slower car travels at 60 km/h, what is the speed of the faster car? (in km/h)", "answer": "75"},
        {"question": "Divide 600 among three friends in the ratio 2:3:5.", "answer": "120, 180, 300"},
        {"question": "The ratio of milk to water in a solution is 5:2. If there are 35 liters of milk, how much water is there?(in Litres)", "answer": "14"},
    ],
       "Miscellaneous": [
        {"question": "The ratio of the circumference to the diameter of a circle is?", "answer": "3.14"},
        {"question": "Simplify the ratio 150:250.", "answer": "3:5"},
        {"question": "The ratio of the sides of a triangle is 3:4:5. If the perimeter is 36 cm, what is the length of the longest side?", "answer": "15 cm"},
        {"question": "The cost of 3 similar items is 90. What is the cost of 7 such items?", "answer": "210"},
        {"question": "The number of students in two schools is in the ratio 7:9. If the first school has 280 students, how many students are in the second school?", "answer": "360"},
        {"question": "The profit earned by two shops is in the ratio 2:3. If the larger shop earns 45,000, what is the profit of the smaller shop?", "answer": "30,000"},
        {"question": "Divide 45 liters of milk into two parts in the ratio 3:2.", "answer": "27 liters, 18 liters"},
        {"question": "If the radius of two circles is in the ratio 1:3, what is the ratio of their areas?", "answer": "1:9"},
        {"question": "The ratio of sugar to flour in a recipe is 2:5. If 250 grams of sugar is used, how much flour is required? (answer in grams)", "answer": "625"},
        {"question": "Two angles of a triangle are in the ratio 2:3, and the third angle is 60°. What is the smaller one of the two angles?", "answer": "40"},
        {"question": "Simplify the ratio 48:64.", "answer": "3:4"},
        {"question": "The price of two items is in the ratio 7:9. If the cheaper item costs 140, what is the cost of the more expensive item?", "answer": "180"},
        {"question": "The ratio of the height of a flagpole to its shadow is 3:1. If the shadow is 5 meters long, what is the height of the flagpole?(answer in meter)", "answer": "15"},
        {"question": "Divide 990 among A, B, and C in the ratio 3:4:5.", "answer": "270, 360, 450"},
        {"question": "A rectangle’s length and width are in the ratio 7:4. If the width is 20 cm, what is the length? (answer in cm)", "answer": "35"},
        {"question": "The ratio of the number of cats to dogs in a shelter is 5:7. If there are 35 dogs, how many cats are there?", "answer": "25"},
        {"question": "The ratio of students to teachers in a school is 15:1. If there are 450 students, how many teachers are there?", "answer": "30"},
        {"question": "Simplify the ratio 84:126.", "answer": "2:3"},
        {"question": "The ratio of red to blue marbles in a bag is 2:3. If there are 40 blue marbles, how many red marbles are there?", "answer": "26"},
        {"question": "The ratio of the length to the width of a photograph is 4:3. If the width is 12 cm, what is the length? (answer in cm)", "answer": "16"},
    ],  
    
    
}





# History Tracking
if "history" not in st.session_state:
    st.session_state["history"] = []

# App Layout
st.title("Ratio and Proportion Quiz")
st.sidebar.header("Quiz Settings")
topic = st.sidebar.selectbox("Choose a topic", list(question_bank.keys()))
st.sidebar.write("Selected Topic:", topic)

# Quiz Logic
if topic:
    questions = random.sample(question_bank[topic], len(question_bank[topic]))
    score = 0

    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}.** {q['question']}")
        answer = st.text_input(f"Your Answer for Question {i+1}", key=i)

        if st.button(f"Submit Answer for Q{i+1}", key=f"submit-{i}"):
            if answer.strip().lower() == q["answer"].strip().lower():
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Wrong! Correct Answer: {q['answer']}")

    # Save the score with the date
    st.session_state["history"].append({"date": str(datetime.date.today()), "score": score})

    st.write(f"**Your Score:** {score}/{len(questions)}")

# Display History
if st.sidebar.button("Show History"):
    st.sidebar.write("**Accuracy History**")
    for record in st.session_state["history"]:
        st.sidebar.write(f"Date: {record['date']} | Score: {record['score']}")
