
# Schema Validation
def validate_schema(df, expected_columns):
    actual = list(df.columns)
    expected = list(expected_columns.keys())
    return actual == expected


# Datatype Validation
def validate_dtypes(df, expected):
    error = {}
    for col,dtype in expected.items():
        if str(df[col].dtype) != dtype:
            error[col] = {
                "expected" : dtype,
                "found" : str(df[col].dtype)
            }
    return error


# Missing Values
def check_missing(df):
    return df.isnull().sum()


# Duplicate Records
def check_duplicates(df):
    return df.duplicated().sum()


# Invalid Amount
def validate_amount(df):
    return (df["Amount"] < 0).sum()


# Class Distribution
def class_distribution(df):
    return df["Class"].value_counts(normalize=True)
