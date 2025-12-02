# 📡 Cybersecurity & Financial Threat Intelligence Aggregator

A Flask web application that aggregates and surfaces the latest headlines and alerts from across the cybersecurity, finance, cryptocurrency, geopolitics, crime, and world news ecosystems. This serves as a centralized dashboard for monitoring breaking news, active cyber threats, financial market movements, and geopolitical events relevant to incident response, penetration testing, cloud infrastructure security, and strategic risk monitoring.

## What It Does

- **Aggregates and filters content** from multiple public RSS feeds
- **Surfaces high-priority articles** containing keywords relevant to cybersecurity operations, financial risk, and geopolitical intelligence
- **Real-time monitoring** of breaking news from trusted sources
- **Keyword-based filtering** tailored for cybersecurity professionals, SOC analysts, and risk managers
- **Category organization** to group articles by domain (Cybersecurity, Finance, Crypto, World News, Geopolitics, Defense)

## Features

- **Web-based dashboard** with clean, modern UI
- **Dark/Light theme toggle** with preference persistence
- **Search functionality** to filter articles by title, content, or both
- **Responsive design** built with Bootstrap
- **Real-time feed aggregation** from 20+ trusted sources
- **Keyword filtering** for relevant threat intelligence

## Technologies

- **Python 3.12+**
- **Flask** - Web framework for routing and rendering
- **feedparser** - RSS/Atom feed parsing
- **requests** - HTTP library for fetching feeds
- **Bootstrap 5** - Frontend framework
- **JavaScript** - Client-side interactivity

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/cyberfeed_scraper.git
   cd cyberfeed_scraper/cyber_newsfeed_web
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or if using Python 3 specifically:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

   **Note:** If you encounter an "externally-managed-environment" error, you may need to:
   - Use a virtual environment (recommended):
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     pip install -r requirements.txt
     ```
   - Or use the `--user` flag:
     ```bash
     pip install --user -r requirements.txt
     ```

## Usage

### Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```
   
   Or with Python 3:
   ```bash
   python3 app.py
   ```

2. **Access the application:**
   - Open your web browser and navigate to: `http://127.0.0.1:5000`
   - The application will automatically fetch and display articles from all configured feeds

### Using the Dashboard

- **Search Articles:** Use the search bar to filter articles by title, content, or both
- **Toggle Theme:** Click the "Toggle Dark Mode" button to switch between dark and light themes (preference is saved)
- **View Articles:** Click on any article title to open it in a new tab
- **Browse by Category:** Articles are automatically categorized by source domain

## Example Use Cases

- **Spotting new zero-day exploits** or nation-state attack attributions within minutes of publication
- **Monitoring financial markets** for events linked to cybercrime (crypto laundering, stock market DDoS schemes)
- **Tracking law enforcement actions** and major cybercrime arrests via press releases
- **Watching geopolitical conflicts** and their potential impact on cloud services and infrastructure

## Configured Sources

The application monitors feeds from:

- **Cybersecurity:** Bleeping Computer, Krebs on Security, The Record, Cyberscoop, InfoSecurity Magazine, PortSwigger, Security Parrot, and more
- **Crypto/Finance:** CoinTelegraph, CoinDesk, Bitcoinist, NewsBTC, CryptoPotato, DailyHODL, Investing.com
- **World News:** BBC News, Al Jazeera, UN News, Defense News

## Customization

### Adding New Feeds

Edit `app.py` and add new feed entries to the `feeds` list:
```python
feeds = [
    {'url': 'https://example.com/feed/', 'category': 'Your Category'},
    # ... existing feeds
]
```

### Modifying Keywords

Update the `keywords` list in `app.py` to filter for different topics:
```python
keywords = [
    'your', 'custom', 'keywords', 'here'
]
```

## Project Structure

```
cyber_newsfeed_web/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main HTML template
├── static/
│   └── style.css      # Custom styles
└── README.md          # This file
```

## Troubleshooting

- **ModuleNotFoundError:** Make sure all dependencies are installed: `pip install -r requirements.txt`
- **Port already in use:** If port 5000 is busy, modify `app.py` to use a different port:
  ```python
  app.run(debug=True, port=5001)
  ```
- **Feed fetch errors:** Some feeds may be temporarily unavailable. The app will continue with available feeds.

## Future Improvements (Maybe?)

- Redis-backed persistent caching
- Email alerting or webhook-based notifications
- Docker containerization for easy deployment
- Enhanced search with sorting and filtering options
- User authentication and personalized feeds
- Scheduled background updates

## License

This project is for personal use and educational purposes.

## Author

Adam. 
Built for daily monitoring of global developments affecting cloud infrastructure security, cyber incident readiness, financial risk assessment, and geopolitical threat mapping.

---

**Note:** This is a development server, intended to be for personal local use.
