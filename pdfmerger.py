import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def merge_pdfs():
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not files:
        return

    merger = PyPDF2.PdfMerger()

    for file in files:
        with open(file, "rb") as pdf_file:
            merger.append(pdf_file)

    output_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save Merged PDF As"
    )

    if output_path:
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Success", f"Merged PDF saved as:\n{output_path}")

# GUI
root = tk.Tk()
root.title("PDF Merger by RS")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Merge Multiple PDF Files", font=("Arial", 14))
label.pack(pady=10)

button = tk.Button(frame, text="Upload & Merge PDFs", command=merge_pdfs, width=30)
button.pack(pady=20)

root.mainloop()

