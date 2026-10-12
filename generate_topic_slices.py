import json
import os

os.makedirs("topics", exist_ok=True)

with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

# Group by topicId
topics_map = {}
for q in questions:
    tid = q.get("topicId")
    if tid not in topics_map:
        topics_map[tid] = {
            "topicId": tid,
            "topicName": q.get("topicName"),
            "questions": []
        }
    topics_map[tid]["questions"].append(q)

manifest = []
for tid, data in sorted(topics_map.items()):
    filename = f"topic_{tid}.json"
    filepath = os.path.join("topics", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data["questions"], f, ensure_ascii=False, indent=2)
    
    file_size_kb = os.path.getsize(filepath) / 1024
    print(f"Generated {filepath}: {len(data['questions'])} questions ({file_size_kb:.1f} KB)")
    
    manifest.append({
        "topicId": tid,
        "topicName": data["topicName"],
        "count": len(data["questions"]),
        "file": filename
    })

manifest_path = os.path.join("topics", "manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump({
        "version": 10,
        "totalQuestions": len(questions),
        "totalTopics": len(manifest),
        "topics": manifest
    }, f, ensure_ascii=False, indent=2)

print(f"\nManifest generated at {manifest_path} with {len(manifest)} topics.")
