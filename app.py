import streamlit as st
import pandas as pd
import joblib
import os

# إعداد الصفحة لتكون ذات طابع رسمي
st.set_page_config(page_title="نظام تصنيف البلاغات الذكي", layout="wide")

# ترويسة رسمية
st.title("🏛️ نظام تصنيف البلاغات الذكي - أمانة المنطقة")
st.markdown("---")

# تحميل الموارد مع معالجة الأخطاء
@st.cache_resource
def load_assets():
    if not os.path.exists('my_model.pkl'):
        return None, None
    model = joblib.load('my_model.pkl')
    df = pd.read_csv('my_data.csv')
    return model, df

model, df = load_assets()

# التحقق من أن الموديل يعمل
if model is None:
    st.error("خطأ: لم يتم العثور على ملف النموذج. يرجى التأكد من رفع ملف my_model.pkl بشكل صحيح.")
else:
    # لوحة المؤشرات (KPIs)
    col1, col2, col3 = st.columns(3)
    col1.metric("إجمالي البلاغات الواردة", len(df))
    col2.metric("التصنيفات المعتمدة", df['category'].nunique())
    col3.metric("مستوى الاستجابة", "فعال")

    # تبويب لعرض البيانات
    with st.expander("📄 أرشيف البلاغات الواردة"):
        st.dataframe(df, use_container_width=True)

    # قسم التصنيف الذكي
    st.markdown("### 🔍 تصنيف البلاغات الواردة")
    st.info("قم بإدخال تفاصيل البلاغ ليقوم النظام بتصنيفه وتوجيهه للقسم المختص آلياً.")
    
    user_input = st.text_area("نص البلاغ:", placeholder="مثال: تراكم نفايات في شارع العام...")

    if st.button("تصنيف البلاغ وإرساله"):
        if user_input:
            try:
                # التأكد أن الموديل مدرب (فحص بسيط)
                prediction = model.predict([user_input])
                st.success(f"✅ تم تصنيف البلاغ بنجاح تحت فئة: **{prediction[0]}**")
            except Exception as e:
                st.error("الموديل يحتاج إلى إعادة تدريب أو يحتوي على خلل في البيانات. يرجى التحقق من ملف pkl.")
        else:
            st.warning("يرجى كتابة نص البلاغ للتمكن من التصنيف.")
