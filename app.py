import streamlit as st
import pandas as pd
import plotly.express as px

# إعداد الصفحة
st.set_page_config(page_title="منصة بلدية ينبع - الذكية", layout="wide")

# تصميم احترافي (CSS)
st.markdown("""
    <style>
    /* تغيير لون الخلفية */
    .stApp {background-color: #f0f2f6;}
    
    /* تنسيق الكروت */
    div[data-testid="stMetricValue"] {
        font-size: 28px;
        color: #1e3a8a;
    }
    .css-1r6slb0 {background-color: #ffffff; padding: 20px; border-radius: 15px; border-left: 5px solid #1e3a8a;}
    
    /* تنسيق العناوين */
    h1 {color: #1e3a8a; text-align: center; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

st.title("🏛️ منصة إدارة البلاغات - محافظة ينبع")
st.markdown("<p style='text-align:center;'>تحليل ذكي ومؤشرات أداء آنية لخدمات البلدية</p>", unsafe_allow_html=True)

# تحميل ومعالجة البيانات
@st.cache_data
def load_data():
    df = pd.read_csv('my_data.csv')
    if 'status' not in df.columns:
        df['status'] = 'قيد المعالجة'
    return df

df = load_data()

# 1. شريط المؤشرات المتطور
col1, col2, col3, col4 = st.columns(4)
col1.metric("إجمالي البلاغات", f"{len(df)} بلاغ")
col2.metric("بلاغات اليوم", "14", "+2")
col3.metric("معدل الإنجاز", "89%")
col4.metric("عدد الأقسام", df['category'].nunique())

st.markdown("<br>", unsafe_allow_html=True)

# 2. قسم الرسوم البيانية المتطورة
c1, c2 = st.columns([2, 1])

with c1:
    # مخطط بار احترافي
    fig = px.bar(df['category'].value_counts().reset_index(), 
                 x='category', y='count', 
                 title="📊 حجم البلاغات حسب الفئة",
                 color='count', color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)

with c2:
    # مخطط دائري بنمط احترافي
    fig2 = px.pie(df, names='category', title="📈 النسبة المئوية للفئات", 
                  hole=0.5, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig2, use_container_width=True)

# 3. قسم البيانات (جدول تفاعلي)
st.subheader("📋 سجل البيانات التفصيلي")
st.dataframe(df, use_container_width=True)

# تذييل الصفحة
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>نظام مراقبة الأداء - بلدية محافظة ينبع © 2026</p>", unsafe_allow_html=True)
