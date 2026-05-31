{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fee7c995-8b17-46bd-bb32-39e37a89adf4",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_8896\\2401475375.py:3: DtypeWarning: Columns (1,3,4,6,7,8,10,14,19,20,21,22,23,24,25,26,27,30,31,32,34,38,42,45,56,61,69,79) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  df = pd.read_csv(\"data_clean.csv\")\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(\"data_clean.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9d3f6462-ef79-4683-bc49-2d263327c005",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"price_per_night\"] = df[\"price\"] / (df[\"minimum_nights\"] + 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5176720c-aeb4-44a1-9931-a7867c9760b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"review_intensity\"] = df[\"number_of_reviews\"] / (df[\"availability_365\"] + 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e7ba8255-67bd-41cc-8159-6967ea15ea24",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"value_score\"] = df[\"number_of_reviews\"] / (df[\"price\"] + 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f39c11bd-99a1-445d-961b-473bfa7f8d18",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"host_activity\"] = df[\"calculated_host_listings_count\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "23aded0a-cd86-456c-8f73-9c9125e9133f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"location_score\"] = df[\"latitude\"] * df[\"longitude\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5a7f67f6-1d3b-437c-95a9-aef1f86b4683",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv(\"data_final.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "76b0988f-5882-4d2d-aa1a-a5f0bda9072b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(50166, 94)"
      ]
     },
     "execution_count": 15,
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
   "execution_count": null,
   "id": "31468489-98f5-4d8c-a394-62ffe19534b1",
   "metadata": {},
   "outputs": [],
   "source": []
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
