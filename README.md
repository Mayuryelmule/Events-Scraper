🎉 Bangalore Events Scraper and React Frontend

This project is a full-stack application that:

    Scrapes event data from Insider.in using Selenium.

    Stores the event data in a JSON format (events.json).

    Serves the data using a Flask API (server.py).

    Displays the data in a beautiful React frontend with "Book Now" buttons linking to event pages.

📁 Project Structure
```bash
project-root/
│
├── backend/
│   ├── scraper.py          # Scrapes event data from the website
│   ├── events.json         # Output of the scraper script
│   └── server.py           # Flask server to serve the data as an API
│
├── frontend/
│   ├── public/
│   │   └── index.html      # HTML template for React app
│   │
│   └── src/
│       ├── App.js          # Main App component
│       ├── index.js        # React DOM rendering
│       ├── components/
│       │   └── EventCard.js    # Component to display each event
│       │   └── EventList.js    # Component to list all events
│       │
│       └── assets/          # Images and CSS if needed
│
├── README.md                # Project documentation
│
├── package.json             # Dependencies for React
│
└── requirements.txt         # Dependencies for Python backend
```

🚀 Getting Started
1️⃣ Clone the repository

git clone https://github.com/Mayuryelmule/Events-Scraper.git
cd Events-Scraper

2️⃣ Install Backend Dependencies

Make sure you have Python 3.7+ and pip installed.

cd backend
pip install -r requirements.txt

3️⃣ Install Frontend Dependencies

Ensure you have Node.js and npm installed.

cd frontend
npm install

4️⃣ Start the Backend Server

Run the Flask server:

cd backend
python3 server.py

Server will be live at 👉 http://localhost:5000/api/events
5️⃣ Start the Frontend Application

Open a new terminal and run:

cd frontend
npm start

App will be live at 👉 http://localhost:3000
🔍 Endpoints
METHOD	ENDPOINT	DESCRIPTION
GET	/api/events	Fetches all events in Bangalore
⚙️ Usage

    When the Flask server starts, it triggers scraper.py to scrape the latest events.

    Data is stored in events.json and served by Flask.

    React frontend fetches data from Flask and displays it beautifully.

✨ Features

    Scrapes real-time event data.

    Beautifully displays event cards.

    Book Now button that links directly to the event booking page.

    Fully responsive design.

🛠 Tech Stack

    Backend: Flask, Selenium

    Frontend: React.js

    Web Scraping: Selenium with BeautifulSoup

    Styling: CSS

🤝 Contributing

    Fork the repository.

    Create a new branch (feature/my-feature).

    Commit changes (git commit -m 'Add my feature').

    Push to the branch (git push origin feature/my-feature).

    Create a Pull Request.

🔐 License

MIT License. See LICENSE for more information.
