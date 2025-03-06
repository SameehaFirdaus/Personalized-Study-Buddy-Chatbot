import pandas as pd
import random

class StudyBuddyChatbot:
    def __init__(self):
        self.resources = pd.read_csv('study_resources.csv')

    def get_response(self, user_input):
        user_input = user_input.lower()
        
        if "study plan" in user_input:
            return self.create_study_plan()
        elif "help" in user_input:
            return "I can help you with study plans, resources, and answering questions about your subjects!"
        elif "resources" in user_input:
            return self.suggest_resources()
        else:
            return "I'm sorry, I didn't understand that. You can ask me for a study plan or resources."

    def create_study_plan(self):
        return "Here's a simple study plan: \n1. Review your notes for 30 minutes. \n2. Practice problems for 1 hour. \n3. Take a break for 15 minutes. \n4. Repeat for each subject."

    def suggest_resources(self):
        resource = random.choice(self.resources['resource_name'].tolist())
        return f"How about checking out this resource: {resource}."
