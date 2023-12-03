import streamlit as st
import pandas as pd
import numpy as np
from function import status, os_system
import matplotlib.pyplot as plt
import pickle
import os

st.title("Aplikasi")


with st.container():
    income = st.number_input("Income")
    name_email_similarity = st.number_input("name email")
    current_address_months_count = st.number_input("current address")
    customer_age = st.number_input("customer age")
    days_since_request = st.number_input("days")
    intended_balcon_amount = st.number_input("intended")
    zip_count_4w = st.number_input("zip count")
    velocity_6h = st.number_input("velocity")
    velocity_24h = st.number_input("velocity 24h")
    velocity_4w = st.number_input("velocity 4w")
    bank_branch_count_8w = st.number_input("bank branch")
    date_of_birth_distinct_emails_4w = st.number_input("date of birth")
    credit_risk_score = st.number_input("credit risk")
    housing_status = st.selectbox(
        "housing status", ("BA", "BB", "BC", "BD", "BE", "BF", "BG")
    )
    housing_status = status(housing_status)
    bank_months_count = st.number_input("bank months")
    proposed_credit_limit = st.number_input("proposed credit")
    session_length_in_minutes = st.number_input("session length")
    device_os = st.selectbox(
        "device os", ("windows", "other", "linux", "macintosh", "x11")
    )
    device_os = os_system(device_os)

    submit_button = st.button("Predict")

    if submit_button:
        script_directory = os.path.dirname(__file__)
        model = os.path.join(script_directory, "models/model.pkl")
        scaler = os.path.join(script_directory, "models/scaler.pkl")
        # Load Pikle File Model dan Scaler
        with open(model, "rb") as file1:
            best_model = pickle.load(file1)
        with open(scaler, "rb") as file2:
            scaler = pickle.load(file2)

        # data baru yang diinput harus di-standardization terlebih dahulu
        data_baru = [
            [
                income,
                name_email_similarity,
                current_address_months_count,
                customer_age,
                days_since_request,
                intended_balcon_amount,
                zip_count_4w,
                velocity_6h,
                velocity_24h,
                velocity_4w,
                bank_branch_count_8w,
                date_of_birth_distinct_emails_4w,
                credit_risk_score,
                housing_status,
                bank_months_count,
                proposed_credit_limit,
                session_length_in_minutes,
                device_os,
            ]
        ]
        data_baru = scaler.transform(data_baru)

        # prediksi data baru, yang sudah di-standardization, menggunakan model SVM terbaik
        hasil_prediksi = best_model.predict(data_baru)[0]
        # hasil_prediksi = int(hasil_prediksi)
        print(hasil_prediksi)

        st.write(f"device: {device_os}")
        st.write("Hasil prediksi index Anda adalah ")
        try:
            if hasil_prediksi == 0:
                st.write("Not Fraud")
            else:
                st.write("Fraud")
        except Exception as err:
            print(err)
