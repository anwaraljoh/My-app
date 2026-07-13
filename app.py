import streamlit as st
import pandas as pd
import joblib

st.title("لوحة تحكم مشروعي")

# تحميل البيانات والنموذج
df = pd.read_csv('my_data.csv')
model = joblib.load('my_model.pkl')

# عرض البيانات
st.write("### البيانات")
st.dataframe(df.head())

# جزء التنبؤ
user_input = st.number_input("أدخلي قيمة للتنبؤ:")
if st.button("تنفيذ التنبؤ"):
    prediction = model.predict([[user_input]])
    st.write(f"النتيجة المتوقعة هي: {prediction[0]}")