# main.py
import streamlit as st
from frontend import front_end
from pdf_generation import generate_pdf
import pandas as pd
import re
import sqlite3

def create_table():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_info (
            name TEXT,father_name TEXT,address TEXT,aadhaar_no TEXT,
            pan TEXT,dob TEXT,email TEXT,mobile TEXT,
            financial_year TEXT,assessment_year TEXT,
            residential_status TEXT,gender TEXT,
            return_type TEXT,status TEXT,
            bank_name TEXT,account_no TEXT,
            ifsc_code TEXT,income_salary_pension REAL,
            income_business REAL,loss_house_property REAL,
            income_other_sources REAL,gross_total_income REAL,
            deductions REAL,deduction_80c REAL,
            deduction_80d REAL,deduction_80tta REAL,
            taxable_income REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(data):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO user_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['name'],data['father_name'],
        data['address'],data['aadhaar_no'],
        data['pan'],data['dob'],data['email'],data['mobile'],
        data['Financal_year'],data['Assesment_year'],
        data['residential_status'],data['gender'],
        data['return_type'],data['status'],
        data['bank_name'],data['account_no'],
        data['ifsc_code'],data['income_salary_pension'],
        data['income_business'],data['loss_house_property'],
        data['income_other_sources'],data['gross_total_income'],
        data['deductions'],data['deduction_80c'],
        data['deduction_80d'],data['deduction_80tta'],
        data['taxable_income']
    ))
    conn.commit()
    conn.close()

def main(): 
    st.title("ITR Computation Form")
    # st.sidebar.title("Navigation")
    # page = st.sidebar.selectbox("Go to", ["Front-end", "PDF Generation"])
    #if page == "Front-end":
    
    create_table()   
    data = front_end()
    submit = st.button("Generate PDF")
    if submit:
        # Validating Mobile number
        if not re.fullmatch(r"\d{10}", data['mobile']):
            st.error("Please enter a valid 10-digit mobile number")
            return False

        # Validating PAN number
        pan_pattern = re.compile(r'^[A-Z]{3}[ABCFGPHJLT]{1}[A-Z]{1}(?!0000)[0-9]{4}[A-Z]{1}$')
        if not re.fullmatch(pan_pattern, data['pan']):
            st.error("Please enter a valid PAN number")
            return False
        
        aadhar_pattern = re.compile(r'^[2-9]{1}[0-9]{3}\s(?!0000)[0-9]{4}\s(?!0000)[0-9]{4}$')
        if not re.fullmatch(aadhar_pattern, data['aadhaar_no']):
            st.error("Please enter a valid Aadhar number")
            return False

        save_to_db(data)
        # PDF Generation
        pdf_path = generate_pdf(data)
        st.success("PDF generated successfully!")
        with open(pdf_path, "rb") as file:
            st.download_button(
            label="Download PDF",
            data=file,
            file_name="Computation.pdf",
            mime="application/pdf"
        )
      
    else:
        st.error("Please fill in all required fields")

if __name__ == "__main__":
    main()
