"""
Pour Jules : 
    Check cointégration : https://www.youtube.com/watch?v=1zz91G0nR14
    Approche stochastic full :https://hudsonthames.org/pairs-trading-with-stochastic-control-and-ou-process/
    Composition portefeuille (quelles paires, quelles stocks, buy/sell ma paire ou je buy mon stock ? ) : https://www.youtube.com/watch?v=Fllb9C7p7kE

Pour antoine : 
    Beta and secteur neutral rules (after pair selection)
    Correlation based distance and denoising matrix 
    ML approcah :https://www.youtube.com/watch?v=R22JR4tqqqs&t=1s / https://docs.google.com/presentation/d/1NFgjC5Ew2ZP5yHRqm4vXScLdk2KARAAtuH2g5blNNn4/edit#slide=id.gb9a1919e6b_0_240
    Backtest and plot bascktest 
    https://pdf.sciencedirectassets.com/271506/1-s2.0-S0957417420X00121/1-s2.0-S0957417420303146/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIHvyupD0ogQDu69QextHYkISOamV%2FYw1EbijijHHIEPQAiAjfLGbo8bkWf1BSmwkv8noNbZBUucG36YgHyL%2Bnj6sYSq8BQiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAUaDDA1OTAwMzU0Njg2NSIMW5tTLV9r7nkjKDWpKpAFbKfr%2B6UpWTfzj05EfqARymb4hS9iUe0Y6cROmPqpy1VqgOgYP6AWJlfKDv7%2BXNhlm39oGAnyQw49V0ueCY%2B85uSgJomxwlyoqEyssgsC56ZVBtaKGlXdK6i4w0h%2Be1mbrdh%2FucaIdZyLtmvJLEGsyXX1UncN%2F3speKHmKLMpTn5CZvU%2F2%2B9HPgA3ycM9hVllOqFshgI1%2FhWJRKjH4Fu7O9oKVf5y7KFp1%2FXV667qob30hDgYjR33JvfAwwy9qmcexYaAVnVPRTkbnYvEME4JYQl11UPpX%2F%2BukxGWvDi3EVWeuXDc155smZRycuTugMGGxvbe1Gy3FxxKT%2BEorN17qu7XLGjH5lKhnQeUYVVyRKuGgqERUE%2FlAbj1LbowqSWPKAOES%2FjBmhez7FB36H8SpJ%2FZFAOq0jcl2nOav9p22t3J6JffNDjLbUrNHbSO2RoZFWFBHTXSeroVX6b%2BhFq2RP4HQ9mHVt%2BO90C7WvRYteGocHEaw2kGgidU5gYME7Ilz4mGVZzz0tk296MNWQdI5lXV5PbukiweR1tokyDDizwiNECAfJY4%2BD5QhfINWQ5Ya3Qo5n4RHNJ1YnWbY5gZp%2Bb%2FrggY8eY%2F1qtvgf95kypWwhh96Nm69NyK456spnfqzMgxhSIPZQ3BtQPbhhpa%2B8NZ%2Brf09d6SW7JR1RWbU7WXYpB67g9KFbLNabaRXtzcR8RqiTGap4gpHkvlwOigqLH5Z8hRZi97qADopJzeqDeJpdluGm8F3waGdvzUIfvlbMgaK%2BTZlRCpP%2FUI1EssXwsNg4CoKFXD2%2BObGxR%2F75YJg5Ez3gnMEHX6lKip1UaNmnSKIXc%2F7wIzwXeu4yrksOXb7ZcT3Z7zgBquuAfjYxYw2vK0vAY6sgFbh%2FdMOI00q%2BKhjQMMavlorEGO7Lkph7hRwmHMrJTIFNz%2BGK8XhC9Cz9yw9AelIdSs3pPYSIdzdNG75yCnwEj9%2Bp2PHZAJ1j8w3W9zscDxcOfFpzocNKHMi%2Fruxvr5ek1%2FmLuNBzrBLOYFlZyPgOegBwM7ODdCA%2FycCcvj31vciwH0J76C97HHQhALBsZlYnJC3QmMksxxwTJb2RCmHzRUonMSjT9ex%2FxyBKA7IJ8CmeNd&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250119T180409Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY5XXGZWGJ%2F20250119%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c0d04f3fe0b69b186f7f43183417dc89dd7f30811082c4b37cfbb710ec7c2c8c&hash=134ebaee5e1a5dbbccdc2adbb503837b9b7826ac05359570ac521da6f51481e6&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0957417420303146&tid=spdf-9b03db89-5a3b-49ee-9b07-6a930e251f58&sid=aa9768c875a2e94173488ed051c3b214b8c9gxrqb&type=client&tsoh=d3d3LXNjaWVuY2VkaXJlY3QtY29tLnByb3h5LmJ1LmRhdXBoaW5lLmZy&ua=1c145c5f575f0d0b020900&rr=9048bedfea602a65&cc=fr

    
Plus tard : 
    PCA : https://www.youtube.com/watch?v=IVAmm34eKWQ
    Sparse-mean reversion : https://www.youtube.com/watch?v=IP7R-gnDF9w