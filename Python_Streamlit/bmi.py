import streamlit as st
import pandas as pd
import math


#Tampilkan judul
st.title("Penghitung BMI")

#Minta pengguna untuk memasukkan tinggi dan berat badan
height = st.number_input("Tinggi(meter): ", min_value=0.01, placeholder="Masukkan tinggi badan kamu")
weight = st.number_input("Berat badan(kilogram): ", placeholder="Masukkan berat badan kamu", min_value=0.01)

#Hitung BMI
bmi = weight / (height * height)

#Menampilkan hasil perhitung
st.write("BMI: ", bmi)
 #Tampilkan interpretasi BMI
if bmi < 18.5:
    st.write("Kurus")
elif bmi < 25:
    st.write("Normal")
elif bmi < 30:
    st.write("Overweight")
else:
    st.write("Obesitas")


# def calculate_bmi(height, weight):
    # """
    # Menghitung BMI dari tinggi dan berat badan.
# 
    # Args:
        # height: Tinggi badan dalam meter.
        # wight: Berat badan dalam kilogram.
    # 
    # Returns:
        # Nilai BMI.
    # """
# 
    # return weight / (height * height)


# def main():
    # """
    # Program penghitung BMI.
    # """

    # Tampilkan judul
    # st.title("Penghitung BMI")

    # Minta pengguna untuk memasukkan tinggi dan berat badan
    # height = st.number_input("Tinggi(meter): ")
    # weight = st.number_input("Berat badan(kilogram): ")

    # try:
        # bmi = calculate_bmi(height, weight)
    # except ZeroDivisionError:
        # st.error("Berat dan tinggi badan tidak boleh 0")

    # Hitung BMI
    # bmi = weight / (height * height)

    # Menampilkan hasil perhitungan
    # st.write("BMI: ", bmi)

    # Tampilkan interpretasi BMI
    # if bmi < 18.5:
        # st.write("Kurus")
    # elif bmi < 25:
        # st.write("Normal")
    # elif bmi < 30:
        # st.write("Overweight")
    # else:
        # st.write("Obesitas")

# if __name__ == "__main__":
    # main()

