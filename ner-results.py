import json
import pandas as pd
from collections import defaultdict

def count_entity_mentions(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    entity_counts = defaultdict(lambda: defaultdict(int))
    
    for annotation in data["annotations"]:
        if annotation and len(annotation) > 1 and "entities" in annotation[1]:
            text = annotation[0]
            for start, end, entity in annotation[1]["entities"]:
                word = text[start:end]
                entity_counts[entity][word] += 1
    
    return entity_counts

def save_to_csv(entity_counts, output_file):
    rows = []
    for entity, word_counts in entity_counts.items():
        for word, count in word_counts.items():
            rows.append([entity, word, count])
    
    df = pd.DataFrame(rows, columns=["Entity", "Word", "Count"])
    df.to_csv(output_file, index=False)

json_file = "NER-annotation.json"
output_file = "entity_counts.csv"

entity_counts = count_entity_mentions(json_file)
save_to_csv(entity_counts, output_file)

print(f"Saved entity counts to {output_file}")