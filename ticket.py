import json

with open("tickets.json", "r", encoding="utf-8") as file:
    tickets = json.load(file)

    print(f"Loaded {len(tickets)} tickets:/n")

for ticket in tickets:
    print(f"Requester: {ticket['requester']}")
    print(f"Description: {ticket['description']}")
    print(f"Category: {ticket['category']}")
    print(f"Priority: {ticket['priority']}")
    print()