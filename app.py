from pypdf import PdfWriter
import streamlit as st
import io

# Hide Streamlit style
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

## Title of the application
st.title("PDF Merger")

## Ask count of PDFs
count = st.text_input("Enter no. of PDFs:")
if count :
    try:
        count = int(count)
        if(count<1):
            raise ValueError()
        
        # Input of files 
        uploaded_files = []
        for i in range(count):
            uploaded_file = st.file_uploader(f"Choose your PDF {i+1}", type="pdf", key=f"pdf_{i}")
            uploaded_files.append(uploaded_file)
        
         # check if all files are uploaded , then continue , else code of else block works till then
        if all(uploaded_files):
            merger = PdfWriter()
            for file in uploaded_files:
                # This line makes the file work with PdfWriter 
                merger.append(io.BytesIO(file.read()))

            # Save to memory(ram) (not a file on disk)
            output = io.BytesIO()
            merger.write(output)
            merger.close()
            output.seek(0)  # Reset pointer to start

            # Download button
            st.success("✅ Merged PDF is ready!")
            # Show a download button
            st.download_button("Download Merged PDF", data=output, file_name="Merged.pdf", mime="application/pdf")
        else:
            st.info("Please upload all the PDFs above to enable merging.")

    except ValueError:
        st.write("Only natural numbers accepted!")


