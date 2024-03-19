import pandas as pd

# Sample data
data = {
    'Name': ['Totals and Components', 'Thousand Pound Correction', 'Date Adjustment', 'Selective Editing', 'Cell Key Perturbation', 'Ratio of Means', 'Winsorisation', 'Horvitz-Thompson Ratio Estimator', 'Mean of Ratios'],
    'Theme': ['Editing', 'Editing', 'Editing', 'Editing', 'Statistical Disclosure Control', 'Imputation', 'Sample Design & Estimation', 'Sample Design & Estimation', 'Imputation'],
    'Expert_Group': ['Editing & Imputation', 'Editing & Imputation', 'Editing & Imputation', 'Editing & Imputation', 'Statistical Disclosure Control', 'Editing & Imputation', 'Sample Design & Estimation', 'Sample Design & Estimation', 'Editing & Imputation'],
    "Languages": ['Python/Pandas', 'Python/Pandas', 'Python/Pandas', 'Python/Pandas', 'Python/R', 'Python/PySpark', 'Python/PySpark', 'Python/PySpark', 'Python/PySpark']
}

# Creating DataFrame
df = pd.DataFrame(data)

# Function to search for partial matches
def search_partial(df, query):
    result = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    return result

# Example usage
query = 'To'  # Partial search query
result = search_partial(df, query)
print("Search results:\n", result)