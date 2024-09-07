import streamlit as st

def front_end():
    st.header("Personal Information")
    name = st.text_input("Name")
    father_name = st.text_input("Father's Name")
    address = st.text_input("Address")
    aadhaar_no = st.text_input("Aadhaar Card No.")
    pan = st.text_input("PAN")
    dob = st.date_input("Date of Birth")
    email = st.text_input("E-Mail")
    mobile = st.text_input("Mobile")

    st.write("Financial Year")
    f = st.date_input("From:") 
    t = st.date_input("To")
    from_str = f.strftime("%d-%m-%Y")
    to_str = t.strftime("%d-%m-%Y")
    Financal_year = from_str +" to " + to_str

    Assesment_year = st.text_input("Assesment Year")
    residential_status = st.selectbox("Residential Status", ["Resident", "Non-Resident"])
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    return_type = st.text_input("Return Type")
    status = st.text_input("Status")
    bank_name = st.text_input("Primary Bank Name")
    account_no = st.text_input("Bank Account No.")
    ifsc_code = st.text_input("Bank IFSC Code")
    
    st.header("Computation of Income")
    income_salary_pension = st.number_input("Income from Salary/Pension", min_value=0.0, step=0.10)
    income_business = st.number_input("Income from Business", min_value=0.0, step=0.10)
    loss_house_property = st.number_input("Loss from House Property", min_value=0.0, step=0.10)
    income_other_sources = st.number_input("Income From Other Sources", min_value=0.0, step=0.10)

    # Automatically calculate the Gross Total Income
    gross_total_income = income_salary_pension + income_business - loss_house_property + income_other_sources
    st.write("Gross Total Income: ₹", gross_total_income)

    st.write("Deduction:")

    deduction_80c = st.number_input("80C - Deduction on Certain Payments", min_value=0.0, step=0.10)
    deduction_80d = st.number_input("80D - Medical Insurance", min_value=0.0, step=0.10)
    deduction_80tta = st.number_input("80TTA", min_value=0.0, step=0.10)

    deductions = deduction_80c + deduction_80d + deduction_80tta
    st.write("Total Deduction: ₹", deductions)

    taxable_income = gross_total_income - deductions
    st.write("Taxable Income: ₹", taxable_income)
    #st.number_input("Net Taxable Income", min_value=0.0, step=0.10)

    return {
        "name": name,
        "father_name": father_name,
        "address": address,
        "aadhaar_no": aadhaar_no,
        "pan": pan,
        "dob": dob,
        "email": email,
        "mobile": mobile,
        "Financal_year": Financal_year,
        "Assesment_year": Assesment_year,
        "residential_status": residential_status,
        "gender": gender,
        "return_type": return_type,
        "status": status,
        "bank_name": bank_name,
        "account_no": account_no,
        "ifsc_code": ifsc_code,
        "income_salary_pension": income_salary_pension,
        "income_business": income_business,
        "loss_house_property": loss_house_property,
        "income_other_sources": income_other_sources,
        "gross_total_income": gross_total_income,
        "deductions": deductions,
        "deduction_80c": deduction_80c,
        "deduction_80d": deduction_80d,
        "deduction_80tta": deduction_80tta,
        "taxable_income": taxable_income
    }
