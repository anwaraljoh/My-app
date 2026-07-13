import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# إعداد الصفحة
st.set_page_config(page_title="منصة البلدية الذكية", layout="wide")

st.title("🚧 منصة رصد ومعالجة البلاغات البلدية")

# تحميل البيانات والموديل
@st.cache_resource
def load_assets():
    df = pd.read_csv('my_data.csv')
    # تأكد من أن الملف موجود بهذا الاسم في GitHub
    model = joblib.load('my_model (1).pkl') 
    return df, model

try:
    df, model = load_assets()

    # 1. المؤشرات (تأكد أن 'status' هو اسم العمود في ملفك)
    # إذا لم يكن موجوداً، سيظهر خطأ، لذا تأكد من ملف CSV
    col1, col2 = st.columns(2)
    with col1:
        st.metric("إجمالي البلاغات", len(df))
    with col2:
        # حساب البلاغات التي حالتها 'Done'
        done_count = len(df[df['status'] == 'Done'])
        st.metric("البلاغات المنجزة", done_count)

    st.markdown("---")

    # 2. الرسم البياني
    fig = px.pie(df, names='category', title="توزيع البلاغات حسب الفئة")
    st.plotly_chart(fig, use_container_width=True)

    # 3. قسم التصنيف بالذكاء الاصطناعي
    st.subheader("🤖 تصنيف بلاغ جديد")
    user_input = st.text_area("أدخل نص البلاغ:")
    
    if st.button("تصنيف البلاغ"):
        if user_input:
            pred = model.predict([user_input])
            st.success(f"✅ فئة البلاغ هي: **{pred[0]}**")
        else:
            st.warning("يرجى إدخال نص للتحليل.")

except Exception as e:
    st.error(f"حدث خطأ: {e}")
    st.info("تأكد أن ملف `my_data.csv` يحتوي على أعمدة بأسماء `status` و `category`.")
