<div align="center">

# 🔗 Flask URL Shortener 🚀

</div>

---

<div align="center">

"Shortening links, tracking clicks, and making the web a bit more organized—one URL at a time." 🌟

👉 Live Demo: https://url-shortener-38x8.onrender.com

</div>

## 🧩 How It Works

<div align="center">


</div>

### 1️⃣ User Submits a Long URL  
Users enter the original URL on the homepage and submit it via a form.  

### 2️⃣ Short Code Generation in the App  
The application generates a random 6-character alphanumeric short code for each URL. This happens entirely in the Flask app to keep the logic centralized and modular.  

### 3️⃣ Duplicate Handling  
If the generated short code already exists, a new code is automatically generated until a unique one is obtained. This ensures all short URLs are unique.  

### 4️⃣ Saving to the Database  
Once a unique short code is generated, the URL and its code are saved in the database. The database layer only handles storing and retrieving data, keeping responsibilities separated.  

### 5️⃣ Redirection and Tracking  
When someone visits a short URL, the app retrieves the original URL, redirects the visitor, and increments a visit counter so users can track link usage.  

---

## ⭐ Key Features

- 🔹 **Short URL Generation** – Creates unique 6-character codes automatically  
- 🔹 **Duplicate Handling** – Ensures uniqueness by regenerating codes if collisions occur  
- 🔹 **Visit Tracking** – Counts how many times each short link is accessed  
- 🔹 **Easy Management** – View all URLs and delete any short link from the dashboard  
- 🔹 **Responsive Design** – Modern interface built with TailwindCSS  
- 🔹 **Copy to Clipboard** – Quickly copy short URLs for sharing  
- 🔹 **Seamless Redirects** – Short URLs redirect directly to the original link  

---

## 🛠 Tech Stack

- 💻 **Backend:** Python, Flask  
- 🗄 **Database:** SQLite  
- 🌐 **Frontend:** TailwindCSS, HTML, JavaScript  

---

## 🚀 How to Run

1. Clone the repository: `git clone <repo-url>`  
2. Install dependencies: `pip install flask`  
3. Run the app: `python app.py`  
4. Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

<div align="center">

> "Shortening links, tracking clicks, and making the web a bit more organized—one URL at a time." 🌟

</div>
