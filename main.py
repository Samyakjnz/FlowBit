from agents.classifier_agent import classify_and_route
from agents.email_agent import extract_email_fields

sample_email = """From: client@example.com
Subject: Request for Quote

Hello, we would like a quote for your services. Please get back to us ASAP."""

format_, intent, thread_id, content = classify_and_route(sample_email, "sample_email.txt")

if format_ == "Email":
    result = extract_email_fields(content)
    print("\n[Email Agent Output]")
    for k, v in result.items():
        print(f"{k}: {v}")


from agents.json_agent import transform_json

print("\n----\n[Testing JSON Agent]")

json_input = {
    "client_name": "Acme Corp",
    "rfq_number": "RFQ-123",
    "items": ["item1", "item2"],
    "deadline": "2025-06-01"
}

result = transform_json(json_input)
print(result)
