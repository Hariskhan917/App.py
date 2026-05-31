{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "83fffede-9994-4661-a354-043dd7777cbc",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_5396\\1640030059.py:3: DtypeWarning: Columns (1,3,4,6,7,8,10,12,14,19,20,21,22,23,24,25,26,27,30,31,32,34,38,42,45,46,56,61,69,79) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  df = pd.read_csv(\"data_raw.csv\")\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                        id                           listing_url  \\\n",
      "0                  2992450  https://www.airbnb.com/rooms/2992450   \n",
      "1                  3820211  https://www.airbnb.com/rooms/3820211   \n",
      "2                  5651579  https://www.airbnb.com/rooms/5651579   \n",
      "3                  6015313  https://www.airbnb.com/rooms/6015313   \n",
      "4                  6623339  https://www.airbnb.com/rooms/6623339   \n",
      "...                    ...                                   ...   \n",
      "63763  1517487888239654553                                   NaN   \n",
      "63764  1517500089629177426                                   NaN   \n",
      "63765  1517507288743285688                                   NaN   \n",
      "63766  1517516598039809920                                   NaN   \n",
      "63767  1517621939131940180                                   NaN   \n",
      "\n",
      "          scrape_id last_scraped       source  \\\n",
      "0      2.026022e+13   2026-02-15  city scrape   \n",
      "1      2.026022e+13   2026-02-15  city scrape   \n",
      "2      2.026022e+13   2026-02-15  city scrape   \n",
      "3      2.026022e+13   2026-02-15  city scrape   \n",
      "4      2.026022e+13   2026-02-15  city scrape   \n",
      "...             ...          ...          ...   \n",
      "63763           NaN          NaN          NaN   \n",
      "63764           NaN          NaN          NaN   \n",
      "63765           NaN          NaN          NaN   \n",
      "63766           NaN          NaN          NaN   \n",
      "63767           NaN          NaN          NaN   \n",
      "\n",
      "                                                   name  \\\n",
      "0                            Luxury 2 bedroom apartment   \n",
      "1             Restored Precinct in Center Sq. w/Parking   \n",
      "2            Large studio apt  by Capital Center & ESP@   \n",
      "3      Comfortable 3BR Home w/ Central Air | Pine Hills   \n",
      "4      Center Sq. Loft in Converted Precinct w/ Parking   \n",
      "...                                                 ...   \n",
      "63763                                     P28 Suite 109   \n",
      "63764                                     P28 Suite 108   \n",
      "63765                                     P28 Suite 103   \n",
      "63766                                     P28 Suite 101   \n",
      "63767          Belle Étage 4BD 3BA Apt – Kypseli Athens   \n",
      "\n",
      "                                             description  \\\n",
      "0      The apartment is located in a quiet neighborho...   \n",
      "1      Step into the charming and comfy 1BR/1BA apart...   \n",
      "2      Spacious studio with hardwood floors, fully eq...   \n",
      "3      Updated 3-bedroom home in Pine Hills near hosp...   \n",
      "4      Step into the charming and comfy 1BR/1BA apart...   \n",
      "...                                                  ...   \n",
      "63763                                                NaN   \n",
      "63764                                                NaN   \n",
      "63765                                                NaN   \n",
      "63766                                                NaN   \n",
      "63767                                                NaN   \n",
      "\n",
      "      neighborhood_overview  \\\n",
      "0                       NaN   \n",
      "1                       NaN   \n",
      "2                       NaN   \n",
      "3                       NaN   \n",
      "4                       NaN   \n",
      "...                     ...   \n",
      "63763                   NaN   \n",
      "63764                   NaN   \n",
      "63765                   NaN   \n",
      "63766                   NaN   \n",
      "63767                   NaN   \n",
      "\n",
      "                                             picture_url    host_id  ...  \\\n",
      "0      https://a0.muscache.com/pictures/44627226/0e72...    4621559  ...   \n",
      "1      https://a0.muscache.com/pictures/prohost-api/H...   19648678  ...   \n",
      "2      https://a0.muscache.com/pictures/b3fc42f3-6e5e...   29288920  ...   \n",
      "3      https://a0.muscache.com/pictures/hosting/Hosti...   31223807  ...   \n",
      "4      https://a0.muscache.com/pictures/prohost-api/H...   19648678  ...   \n",
      "...                                                  ...        ...  ...   \n",
      "63763                                                NaN  678257512  ...   \n",
      "63764                                                NaN  678257512  ...   \n",
      "63765                                                NaN  678257512  ...   \n",
      "63766                                                NaN  678257512  ...   \n",
      "63767                                                NaN   60982106  ...   \n",
      "\n",
      "           license  instant_bookable calculated_host_listings_count  \\\n",
      "0              NaN               NaN                              1   \n",
      "1              NaN               NaN                              7   \n",
      "2              NaN               NaN                              2   \n",
      "3              NaN               NaN                              1   \n",
      "4              NaN               NaN                              7   \n",
      "...            ...               ...                            ...   \n",
      "63763  00002937625               NaN                             10   \n",
      "63764  00002937571               NaN                             10   \n",
      "63765  00002937524               NaN                             10   \n",
      "63766  00002937444               NaN                             10   \n",
      "63767  00003531475               NaN                             40   \n",
      "\n",
      "      calculated_host_listings_count_entire_homes  \\\n",
      "0                                             1.0   \n",
      "1                                             7.0   \n",
      "2                                             1.0   \n",
      "3                                             1.0   \n",
      "4                                             7.0   \n",
      "...                                           ...   \n",
      "63763                                         NaN   \n",
      "63764                                         NaN   \n",
      "63765                                         NaN   \n",
      "63766                                         NaN   \n",
      "63767                                         NaN   \n",
      "\n",
      "      calculated_host_listings_count_private_rooms  \\\n",
      "0                                              0.0   \n",
      "1                                              0.0   \n",
      "2                                              1.0   \n",
      "3                                              0.0   \n",
      "4                                              0.0   \n",
      "...                                            ...   \n",
      "63763                                          NaN   \n",
      "63764                                          NaN   \n",
      "63765                                          NaN   \n",
      "63766                                          NaN   \n",
      "63767                                          NaN   \n",
      "\n",
      "       calculated_host_listings_count_shared_rooms  reviews_per_month  \\\n",
      "0                                              0.0               0.06   \n",
      "1                                              0.0               2.26   \n",
      "2                                              0.0               2.96   \n",
      "3                                              0.0                NaN   \n",
      "4                                              0.0               2.55   \n",
      "...                                            ...                ...   \n",
      "63763                                          NaN                NaN   \n",
      "63764                                          NaN                NaN   \n",
      "63765                                          NaN                NaN   \n",
      "63766                                          NaN                NaN   \n",
      "63767                                          NaN                NaN   \n",
      "\n",
      "                                              source_url  \\\n",
      "0      https://data.insideairbnb.com/united-states/ny...   \n",
      "1      https://data.insideairbnb.com/united-states/ny...   \n",
      "2      https://data.insideairbnb.com/united-states/ny...   \n",
      "3      https://data.insideairbnb.com/united-states/ny...   \n",
      "4      https://data.insideairbnb.com/united-states/ny...   \n",
      "...                                                  ...   \n",
      "63763  https://data.insideairbnb.com/greece/attica/at...   \n",
      "63764  https://data.insideairbnb.com/greece/attica/at...   \n",
      "63765  https://data.insideairbnb.com/greece/attica/at...   \n",
      "63766  https://data.insideairbnb.com/greece/attica/at...   \n",
      "63767  https://data.insideairbnb.com/greece/attica/at...   \n",
      "\n",
      "                       scraped_at neighbourhood_group  \n",
      "0      2026-05-31 23:19:54.396774                 NaN  \n",
      "1      2026-05-31 23:19:54.396774                 NaN  \n",
      "2      2026-05-31 23:19:54.396774                 NaN  \n",
      "3      2026-05-31 23:19:54.396774                 NaN  \n",
      "4      2026-05-31 23:19:54.396774                 NaN  \n",
      "...                           ...                 ...  \n",
      "63763  2026-05-31 23:20:34.105506                 NaN  \n",
      "63764  2026-05-31 23:20:34.105506                 NaN  \n",
      "63765  2026-05-31 23:20:34.105506                 NaN  \n",
      "63766  2026-05-31 23:20:34.105506                 NaN  \n",
      "63767  2026-05-31 23:20:34.105506                 NaN  \n",
      "\n",
      "[63768 rows x 88 columns]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(\"data_raw.csv\")\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "8ce388e3-93cd-4e41-b201-ca0e9c8fc130",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL\\AppData\\Local\\Temp\\ipykernel_5396\\751359073.py:3: DtypeWarning: Columns (1,3,4,6,7,8,10,12,14,19,20,21,22,23,24,25,26,27,30,31,32,34,38,42,45,46,56,61,69,79) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  df = pd.read_csv(\"data_raw.csv\")\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Initial shape: (63768, 88)\n",
      "After cleaning: (50166, 88)\n",
      "Final shape: (50166, 89)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(\"data_raw.csv\")\n",
    "\n",
    "print(\"Initial shape:\", df.shape)\n",
    "\n",
    "# clean column names\n",
    "df.columns = df.columns.str.strip()\n",
    "\n",
    "# convert price safely\n",
    "df[\"price\"] = df[\"price\"].replace('[\\$,]', '', regex=True)\n",
    "df[\"price\"] = pd.to_numeric(df[\"price\"], errors=\"coerce\")\n",
    "\n",
    "# DO NOT destroy dataset\n",
    "df = df.dropna(subset=[\"price\", \"number_of_reviews\"])\n",
    "\n",
    "print(\"After cleaning:\", df.shape)\n",
    "\n",
    "# target variable\n",
    "df[\"popular\"] = (df[\"number_of_reviews\"] >\n",
    "                 df[\"number_of_reviews\"].median()).astype(int)\n",
    "\n",
    "print(\"Final shape:\", df.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "883ab33f-c22b-4140-88e1-27b193426824",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"price\"] = df[\"price\"].replace('[\\$,]', '', regex=True).astype(float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "84b5cfee-ff8f-480e-9ebf-b14dd884f422",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv(\"data_clean.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "060f6e21-676c-48c1-9300-fde180a1c7e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(50166, 89)"
      ]
     },
     "execution_count": 21,
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
   "id": "9593ea07-884c-4f96-b21e-d2969f0a19a8",
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
