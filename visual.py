import json
import matplotlib.pyplot as plt
from collections import defaultdict

# Load JSON file
with open('NER-annotation.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Mapping short labels to full names
label_mapping = {
    "PER": "PERSON",
    "LOC": "LOCATION",
    "DIS": "DISEASE",
    "SYM": "SYMPTOMS",
    "ORG": "ORGANIZATION",
    "YEAR": "YEAR"
}

# Extract annotations
annotations = data.get("annotations", [])

# Count occurrences of each entity type
entity_counts = defaultdict(int)
for annotation in annotations:
    if annotation and isinstance(annotation, list) and len(annotation) > 1:
        entities = annotation[1].get("entities", [])
        for _, _, entity_type in entities:
            full_label = label_mapping.get(entity_type, entity_type)  # Map label if possible
            entity_counts[full_label] += 1

# Plot bar chart
plt.figure(figsize=(18, 16))
plt.bar(entity_counts.keys(), entity_counts.values(), color='skyblue')
plt.xlabel("Entity Labels")
plt.ylabel("Frequency")
plt.title("Name Entity Recognition (NER) Results")
plt.xticks(rotation=45)
plt.show()


# Save plot as PNG
plt.savefig("NER-visuals.png", dpi=300, bbox_inches='tight')
plt.show()