import tensorflow_hub as hub

BERT_URL = 'https://tfhub.dev/google/bert_cased_L-12_H-768_A-12/1'
module = hub.Module(BERT_URL)

print('Download complete')
