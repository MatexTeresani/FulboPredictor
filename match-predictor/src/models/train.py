from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import preprocess


def create_model():

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    return model


def train_model(model, X_train, y_train):

    model.fit(
        X_train,
        y_train
    )

    return model


def evaluate(y_test, predictions):

    return accuracy_score(
        y_test,
        predictions
    )


def main():

    X_train, X_test, y_train, y_test = preprocess.get_data()

    model = create_model()

    model = train_model(
        model,
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    matrix = confusion_matrix(
        y_test, 
        predictions 
    )
    
    accuracy = evaluate(
        y_test,
        predictions
    )
    print('matriz de confusion')
    print(matrix)
    print('reporte')
    print(
        classification_report(
            y_test,
            predictions
        )
    )

    print("Accuracy:", accuracy)


main()