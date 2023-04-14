from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from mongodb import insert

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")


def ner(text):
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    ner_results = nlp(text)
    print(ner_results)
    insert('NER', ner_results)
    return ner_results
