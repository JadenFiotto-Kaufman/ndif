from .Model import Model

model = Model('gpt2')

with model.invoke(['Hello world'], device='cuda:0') as invoker:


    mmlp0 = model.h[0].mlp.output.copy()
    mmlp1 = model.h[1].mlp.output

    model.h[2].mlp.output = mmlp0 + mmlp1
