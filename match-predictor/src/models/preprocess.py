import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


def read_dataset(path):

    df = pd.read_csv(path)

    return df


def clean_dataset(df):

    columns_remove = [

        # Información del partido
        'Div',
        'Date',
        'Time',

        # Fuga de información
        'HomeResult',
        'AwayResult',

        'HomePoints',
        'AwayPoints',

        'HomeWin',
        'AwayWin',

        # Goles del partido actual
        'HomeGoalsFor',
        'AwayGoalsFor',

        'HomeGoalsAgainst',
        'AwayGoalsAgainst',
        'HTR',
        'HomeOpponent',
        'AwayOpponent'
    ]

    df = df.drop(
        columns=columns_remove
    )

    return df


def split_dataset(df):

    # Variable objetivo
    y = df['FTR']

    # Variables predictoras
    X = df.drop(
        columns=['FTR']
    )

    # Limpieza
    X = clean_dataset(X)

    return X, y


def encode_teams(X):

    categorical_columns = [
        'HomeTeam',
        'AwayTeam'
    ]

    encoder = OneHotEncoder(
        handle_unknown='ignore'
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                'teams',
                encoder,
                categorical_columns
            )
        ],
        remainder='passthrough'
    )

    X_encoded = preprocessor.fit_transform(X)

    return X_encoded, preprocessor


def split_train_test(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


def get_data():

    path = (
        'match-predictor/data/processed/'
        'italy/Season 2024-2025/'
        'I1_features.csv'
    )

    df = read_dataset(path)

    X, y = split_dataset(df)

    print("Columnas texto antes del encoder:")
    print(X.select_dtypes(include='object').columns)

    X_encoded, preprocessor = encode_teams(X)

    print("Shape después del encoder:")
    print(X_encoded.shape)

    X_train, X_test, y_train, y_test = split_train_test(
        X_encoded,
        y
    )

    print("\nTrain:")
    print(X_train.shape)

    print("Test:")
    print(X_test.shape)

    print("\nResultados:")
    print(y.value_counts())


    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    get_data()