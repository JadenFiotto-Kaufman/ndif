import torch

import nnsight
from nnsight.pydantics.Request import RequestModel

model = nnsight.LanguageModel("EleutherAI/gpt-j-6b")

import time



for i in range(3):
    start = time.time()
    with model.generate(remote=True) as runner:
        with runner.invoke([[10] * 10] * 20):
            hs = model.transformer.h[-1].output.save()

    print(hs.value)
    print(time.time() - start)

            



    
