from extractor import extract

path = "data/documents/AI PROBLEM STATEMENTS 2.pdf"

pages = extract(path)

print(f"Extracted {len(pages)} pages\n")

for page in pages:
    print("=" * 80)
    print(f"Source : {page['source']}")
    print(f"Page   : {page['page']}")
    print(f"Length : {len(page['text'])} characters")
    print(page["text"])
    print()