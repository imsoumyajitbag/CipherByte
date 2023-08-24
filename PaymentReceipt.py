import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

class PaymentReceiptGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Payment Receipt Generator")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Payment Receipt Generator")
        self.label.pack()

        self.name_label = tk.Label(self.root, text="Customer Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.amount_label = tk.Label(self.root, text="Amount:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()

        self.generate_button = tk.Button(self.root, text="Generate Receipt", command=self.generate_receipt)
        self.generate_button.pack()

    def generate_receipt(self):
        customer_name = self.name_entry.get()
        amount = self.amount_entry.get()

        if not customer_name or not amount:
            return

        pdf_filename = f"receipt_{customer_name}.pdf"
        self.create_pdf_receipt(pdf_filename, customer_name, amount)

        self.name_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

        self.label.config(text=f"Receipt generated: {pdf_filename}")

    def create_pdf_receipt(self, filename, customer_name, amount):
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()

        elements = []

        header = Paragraph("Payment Receipt", styles['Title'])
        elements.append(header)
        elements.append(Spacer(1, 12))

        customer_info = f"Customer: {customer_name}"
        customer_paragraph = Paragraph(customer_info, styles['Normal'])
        elements.append(customer_paragraph)

        amount_info = f"Amount: ${amount}"
        amount_paragraph = Paragraph(amount_info, styles['Normal'])
        elements.append(amount_paragraph)

        elements.append(Spacer(1, 36))

        table_data = [['Description', 'Amount'],
                      ['Product 1', '$50'],
                      ['Product 2', '$30'],
                      ['Total', f'${amount}']]

        table = Table(table_data, colWidths=[250, 100])
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                   ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                   ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                   ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                   ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

        elements.append(table)

        doc.build(elements)

if __name__ == "__main__":
    root = tk.Tk()
    receipt_generator = PaymentReceiptGenerator(root)
    root.mainloop()
