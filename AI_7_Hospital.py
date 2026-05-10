# Expert System for Hospital and Medical Facilities
# Rule-Based Medical Diagnosis System

def display_intro():
    print("==========================================")
    print(" HOSPITAL EXPERT SYSTEM ")
    print("==========================================")
    print("This system suggests possible diseases")
    print("based on the symptoms entered by the user.")
    print("Note: This is not a real medical diagnosis.")
    print("==========================================\n")


def get_symptoms():
    print("Available Symptoms:")
    print("1. fever")
    print("2. cough")
    print("3. headache")
    print("4. chest pain")
    print("5. fatigue")
    print("6. body pain")
    print("7. rash")
    print("8. stress")
    print("9. sore throat")
    print("10. breathing problem\n")

    symptoms = input("Enter symptoms separated by commas: ")
    symptom_list = symptoms.lower().split(',')

    cleaned_symptoms = []

    for symptom in symptom_list:
        cleaned_symptoms.append(symptom.strip())

    return cleaned_symptoms


def diagnose(symptoms):

    # Flu Rule
    if 'fever' in symptoms and 'cough' in symptoms:
        return {
            "disease": "Flu",
            "advice": "Drink fluids, take rest, and monitor temperature."
        }

    # COVID Rule
    elif 'fever' in symptoms and 'breathing problem' in symptoms:
        return {
            "disease": "COVID-19",
            "advice": "Get tested immediately and isolate yourself."
        }

    # Migraine Rule
    elif 'headache' in symptoms and 'stress' in symptoms:
        return {
            "disease": "Migraine",
            "advice": "Avoid stress and take proper rest."
        }

    # Viral Infection Rule
    elif 'rash' in symptoms and 'fever' in symptoms:
        return {
            "disease": "Viral Infection",
            "advice": "Consult a physician for proper medication."
        }

    # Heart Problem Rule
    elif 'chest pain' in symptoms:
        return {
            "disease": "Possible Heart Disease",
            "advice": "Seek emergency medical attention immediately."
        }

    # Common Cold Rule
    elif 'cough' in symptoms and 'sore throat' in symptoms:
        return {
            "disease": "Common Cold",
            "advice": "Take steam inhalation and warm fluids."
        }

    # Weakness Rule
    elif 'fatigue' in symptoms and 'body pain' in symptoms:
        return {
            "disease": "Weakness or Viral Fever",
            "advice": "Take proper nutrition and enough sleep."
        }

    # Default Rule
    else:
        return {
            "disease": "Unknown",
            "advice": "Please consult a doctor for detailed diagnosis."
        }


def display_result(result):
    print("\n==========================================")
    print(" DIAGNOSIS RESULT ")
    print("==========================================")
    print("Possible Disease :", result["disease"])
    print("Medical Advice   :", result["advice"])
    print("==========================================\n")


def ask_continue():
    choice = input("Do you want another diagnosis? (yes/no): ")
    return choice.lower() == "yes"


# Main Program
display_intro()

while True:

    user_symptoms = get_symptoms()

    result = diagnose(user_symptoms)

    display_result(result)

    if not ask_continue():
        print("\nThank you for using the Hospital Expert System.")
        print("Stay Healthy!")
        break