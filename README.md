
# **FastAPI File Upload with PostgreSQL Integration**  

This project is a simple **FastAPI-based file upload API** that allows users to upload files and store them in a local directory (`uploads/`). It also connects to a **PostgreSQL database**, which can be used to store metadata about the uploaded files.  

## **Features**  
- Upload files using `multipart/form-data`  
- Store uploaded files in the `uploads/` directory  
- Retrieve uploaded files via an API endpoint  
- Connect to a PostgreSQL database (for potential file metadata storage)  

## **Setup & Installation**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/Soumyadeep-dev/yourrepo.git
cd yourrepo
```

### **2. Create a Virtual Environment (Optional but Recommended)**  
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4. Configure Database Connection**  
Modify the `DATABASE_URL` in your FastAPI application (`main.py`):  
```python
DATABASE_URL = "postgresql://postgres:'password@localhost:5432/file_upload_db"
UPLOAD_DIR = "uploads"
```
> **Note:** It is recommended to use **environment variables** instead of hardcoding credentials.

### **5. Run the FastAPI Server**  
```sh
uvicorn main:app --reload
```
The server will be available at **http://localhost:8000**  

## **Usage**  

### **Upload a File**  
You can upload a file using `curl`:  
```sh
curl -X 'POST' 'http://localhost:8000/upload/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@yourfile.txt'
```
#### **Sample Response**  
```json
{
  "message": "File uploaded",
  "file_name": "yourfile.txt",
  "file_path": "uploads/yourfile.txt"
}
```

### **Retrieve Uploaded Files**  
To download an uploaded file, use:  
```sh
curl -O http://localhost:8000/files/yourfile.txt
```
or open **http://localhost:8000/files/yourfile.txt** in your browser.

## **To-Do List**  
- [ ] Store file metadata in PostgreSQL  
- [ ] Add authentication for file uploads  
- [ ] Implement file size and type validation  

## **License**  
This project is open-source under the **MIT License**.

---

Let me know if you want any modifications! 🚀
