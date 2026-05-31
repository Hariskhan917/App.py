{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a3b6af1b-1d54-4b78-958e-17ddd2a23162",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.metrics import classification_report\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a4bd94db-743f-49e3-9244-2009044ea456",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_10252\\154993452.py:1: DtypeWarning: Columns (1,3,4,6,7,8,10,14,19,20,21,22,23,24,25,26,27,30,31,32,34,38,42,45,56,61,69,79) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  df = pd.read_csv(\"data_final.csv\")\n"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv(\"data_final.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f3b83ae7-1be9-439c-9ac7-5de30004287b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(50166, 94)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a7964308-9b48-4c5c-a1fe-9825e04e772c",
   "metadata": {},
   "outputs": [],
   "source": [
    "features = [\n",
    "    \"price\",\n",
    "    \"minimum_nights\",\n",
    "    \"availability_365\",\n",
    "    \"number_of_reviews\",\n",
    "    \"price_per_night\",\n",
    "    \"review_intensity\",\n",
    "    \"value_score\",\n",
    "    \"host_activity\"\n",
    "]\n",
    "\n",
    "X = df[features].fillna(0)\n",
    "y = df[\"popular\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9685e988-792e-4a17-94f0-2691eb4fb014",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X, y, test_size=0.4\n",
    "    , random_state=42, stratify=y\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "76b6cdb7-1837-4147-9fa9-d8e9e772b0ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "scaler = StandardScaler()\n",
    "X_train = scaler.fit_transform(X_train)\n",
    "X_test = scaler.transform(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2ad5d43f-ab45-4c17-901a-246f0af2e00f",
   "metadata": {},
   "outputs": [],
   "source": [
    "models = {\n",
    "    \"Logistic\": LogisticRegression(),\n",
    "    \"DecisionTree\": DecisionTreeClassifier(),\n",
    "    \"RandomForest\": RandomForestClassifier(n_estimators=200)\n",
    "}\n",
    "\n",
    "best_model = None\n",
    "best_score = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26c64c65-88b2-4b89-ab7d-47a22e20217f",
   "metadata": {},
   "outputs": [],
   "source": [
    "for name, model in models.items():\n",
    "    model.fit(X_train, y_train)\n",
    "    score = model.score(X_test, y_test)\n",
    "\n",
    "    print(name, score)\n",
    "\n",
    "    if score > best_score:\n",
    "        best_model = model\n",
    "        best_score = score"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
