from paths import *
import nlp
from lfqa_utils import *


if __name__ == "__main__":
    print("Root:"+ ROOT, "DATA Root:" +DATA_ROOT, "Code Root:" +CODE_ROOT)
    eli5 = nlp.load_dataset('eli5')
    print(eli5['test_eli5'][12345])
    # wiki40b_snippets = nlp.load_dataset('wiki_snippets', name='wiki40b_en_100_0')['train']
    # print(wiki40b_snippets)
