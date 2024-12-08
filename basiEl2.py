import streamlit as st
# Subheader
st.subheader('Looping bersama Python')
st.text("""
         Di bawah ini adalah contoh kode yang dibuat menggunakan percabangan: 
         """)
code = """
    x = int(input("Masukan usia kamu"))
    if nama < 15: 
        print("Hello, kid!)
    else: 
        print("Hello, adult!)
        """
st.code(code, language="python")

st.text('Di atas adalah contoh percabangan sederhana. Program diatas berjalan dengan melakukan pengecekan terhadap variabel x. Berikutnya, ini adalah kode yang akan menghasilkan tampilan mathematical expression : ')

st.latex(r"""
        \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
        """)
