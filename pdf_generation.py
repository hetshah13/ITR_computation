from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'BU', 12)
        self.cell(0, 1, 'Personal-Information', 0, 0, 'C')

    def add_box(self, x, y, w, h):
        self.rect(x, y, w, h)

    def add_section(self, title, details, x, y, w, h, title_font_size=12, content_font_size=10, line_height=6):
        self.set_xy(x, y)
        self.set_font('Arial', 'B', title_font_size)
        self.cell(w, 10, title, 0, 1, 'C')
        self.add_box(x, y + 10, w, h - 10)
        self.set_xy(x, y + 10)  # Adjust for title height
        self.set_font('Arial', '', content_font_size)
        for key, value in details.items():
            self.cell(w - 4, line_height, f"{key}: {value}", 0, 1, 'L')

    def add_income_section(self, details, x, y, w, h, content_font_size=10, line_height=6):
        self.add_box(x, y, w, h)
        self.set_xy(x + 2, y + 2)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'COMPUTATION OF INCOME', 0, 1, 'L')
        self.set_font('Arial', '', content_font_size)
        y += 12
        for key, value in details.items():
            self.set_xy(x + 2, y)
            self.cell(w - 4, line_height, f"{key}: {value}", 0, 1, 'L')
            y += line_height

def generate_pdf(data):
    pdf = PDF()
    pdf.add_page()
    
    personal_info = {
        "Name": data['name'],
        "Father's Name": data['father_name'],
        "Address": data['address'],
        "Aadhaar Card No.": data['aadhaar_no'],
        "PAN": data['pan'],
        "Date of Birth": data['dob'],
        "E-Mail": data['email'],
        "Mobile": data['mobile'],
        "Financal_year": data['Financal_year'],
        "Assesment_year": data['Assesment_year'],
        "Residential Status": data['residential_status'],
        "Gender": data['gender'],
        "Return Type": data['return_type'],
        "Status": data['status'],
        "Primary Bank Name": data['bank_name'],
        "Primary Bank Account No.": data['account_no'],
        "Primary Bank IFSC Code": data['ifsc_code']
    }
    pdf.add_section("", personal_info, 10, 8, 190, 102)
    
    income_computation = {
        "Income from Salary/Pension": data['income_salary_pension'],
        "Income from Business": data['income_business'],
        "Loss from House Property": data['loss_house_property'],
        "Income From Other Sources": data['income_other_sources'],
        "Gross Total Income": data['gross_total_income'],
        "Deductions": data['deductions'],
        "80C - Deduction on Certain Payments": data['deduction_80c'],
        "80D - Medical Insurance": data['deduction_80d'],
        "80TTA": data['deduction_80tta'],
        "Taxable Income": data['taxable_income']
    }
    pdf.add_income_section(income_computation, 10, 120, 190, 60)
    
    pdf_output = "Het_comp.pdf"
    pdf.output(pdf_output)
    return pdf_output
