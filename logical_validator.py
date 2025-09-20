import pandas as pd
from itertools import product

df_raw = pd.read_excel(xl).loc[:,['Group','Conditions','Candidates']]
df_raw['Candidates'] = df_raw['Candidates'].apply(lambda x: [int(i.strip()) for i in x.split(',')])

# ✅ Comparacion con la respuesta esperada
def compare_with_expected(df_actual, df_expected_raw):
    df_expected = df_expected_raw.dropna(how='all').rename(columns=lambda x: x.replace('.1', '')).fillna('')
    comparison = pd.DataFrame(df.values == test.values)
    comparison.columns = ['Match']
    return pd.concat([df_actual, df_expected, comparison], axis=1)

groups = df_raw['Group'].tolist()
candidates = [df_raw.loc[df_raw['Group'] == g, 'Candidates'].values[0] for g in groups]
all_combinations = list(product(*candidates))

def is_valid(A, B, C, D):
    # A: <= C
    if not (A <= C):
        return False
    # B: < A and < C
    if not (B < A and B < C):
        return False
    # C: == (D * B) / A
    if A == 0 or (D * B) % A != 0 or C != (D * B) // A:
        return False
    # D: < C + B and > (3 * B) - A
    if not (D < C + B and D > (3 * B) - A):
        return False
    return True
valid_combinations = [combo for combo in all_combinations if is_valid(*combo)]

df = pd.DataFrame(valid_combinations[0], columns=['My Answer'])
df['My Answer'] = df['My Answer'].astype(int)

test = pd.read_excel(xl).loc[:,['Expected Answer']]
df_final = compare_with_expected(df, test)

print(df_final)
