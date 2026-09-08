from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load saved model package
model_package = joblib.load("smartcart_model.pkl")

ohe = model_package["ohe"]
scaler = model_package["scaler"]
pca = model_package["pca"]
cluster_centers = model_package["cluster_centers"]
cluster_names = model_package["cluster_names"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get customer data from form
    data = pd.DataFrame([{
        "Education": request.form["Education"],
        "Income": float(request.form["Income"]),
        "Recency": float(request.form["Recency"]),
        "NumDealsPurchases": float(request.form["NumDealsPurchases"]),
        "NumWebPurchases": float(request.form["NumWebPurchases"]),
        "NumCatalogPurchases": float(request.form["NumCatalogPurchases"]),
        "NumStorePurchases": float(request.form["NumStorePurchases"]),
        "NumWebVisitsMonth": float(request.form["NumWebVisitsMonth"]),
        "Complain": float(request.form["Complain"]),
        "Response": float(request.form["Response"]),
        "Age": float(request.form["Age"]),
        "Tenure_days": float(request.form["Tenure_days"]),
        "Total_spending": float(request.form["Total_spending"]),
        "Total_Children": float(request.form["Total_Children"]),
        "Living_With": request.form["Living_With"]
    }])


    # Categorical columns
    cat_cols = ["Education", "Living_With"]

    # One-hot encoding
    encoded = ohe.transform(data[cat_cols])

    encoded_df = pd.DataFrame(
        encoded.toarray(),
        columns=ohe.get_feature_names_out(cat_cols),
        index=data.index
    )

    # Combine numerical + encoded categorical features
    data = pd.concat(
        [
            data.drop(columns=cat_cols),
            encoded_df
        ],
        axis=1
    )

    # Make sure feature order is exactly the same as training
    data = data.reindex(columns=scaler.feature_names_in_)


    # Scaling
    data_scaled = scaler.transform(data)


    # PCA
    data_pca = pca.transform(data_scaled)


    # Distance from each Agglomerative cluster center
    distances = np.linalg.norm(
        data_pca[:, np.newaxis, :] -
        cluster_centers[np.newaxis, :, :],
        axis=2
    )

    # Nearest cluster
    cluster = distances.argmin(axis=1)[0]


    # Cluster information
    cluster_name = cluster_names[int(cluster)]


    return render_template(
        "index.html",
        prediction=int(cluster),
        cluster_name=cluster_name
    )


if __name__ == "__main__":
    app.run(debug=True)