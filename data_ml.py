import json
import uuid
from datasets import load_dataset

dataset = load_dataset("AdaptLLM/finance-tasks")

def parse_entry(entry):
    pass

def save_to_json(question, answer, id):
    data = {
        "id": str(id),
        "Question": question,
        "Answer": answer
    }
    with open('output.json', 'a') as f:
        json.dump(data, f)
        f.write('\n') 


entries = ["Is the sky blue? Yes", "Is grass green? Yes"]
for entry in entries:
    questions_answers = parse_entry(entry)
    for question, answer in questions_answers:
        unique_id = uuid.uuid4()  
        save_to_json(question, answer, unique_id)
