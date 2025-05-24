from flask import Flask, render_template
import feedparser
import requests
from datetime import datetime

app = Flask(__name__)

feeds = [
    # Cybersecurity
    {'url': 'https://www.bleepingcomputer.com/feed/', 'category': 'Cybersecurity'},
    {'url': 'https://krebsonsecurity.com/feed/', 'category': 'Cybersecurity'},
    {'url': 'https://therecord.media/feed/', 'category': 'Cybersecurity'},
    {'url': 'https://www.cyberscoop.com/feed/', 'category': 'Cybersecurity'},
    {'url': 'https://www.infosecurity-magazine.com/rss/news/', 'category': 'Cybersecurity'},
    {'url': 'https://portswigger.net/daily-swig/rss', 'category': 'Cybersecurity'},
    {'url': 'https://securityparrot.com/feed', 'category': 'Cybersecurity'},
    {'url': 'https://cybercrimeswatch.com/feed', 'category': 'Cybersecurity'},
    {'url': 'https://www.securitymagazine.com/rss', 'category': 'Cybersecurity'},
    {'url': 'https://imperva.com/blog/feed', 'category': 'Cybersecurity'},
    
    # Crypto & Finance
    {'url': 'https://cointelegraph.com/rss', 'category': 'Crypto/Finance'},
    {'url': 'https://www.coindesk.com/arc/outboundfeeds/rss/', 'category': 'Crypto/Finance'},
    {'url': 'https://bitcoinist.com/feed', 'category': 'Crypto/Finance'},
    {'url': 'https://newsbtc.com/feed', 'category': 'Crypto/Finance'},
    {'url': 'https://cryptopotato.com/feed/', 'category': 'Crypto/Finance'},
    {'url': 'https://dailyhodl.com/feed', 'category': 'Crypto/Finance'},
    {'url': 'https://www.investing.com/rss/news_25.rss', 'category': 'Finance'},

    # Politics & World News
    {'url': 'https://feeds.bbci.co.uk/news/world/rss.xml', 'category': 'World News'},
    {'url': 'https://www.aljazeera.com/xml/rss/all.xml', 'category': 'World News'},
    {'url': 'https://news.un.org/feed/subscribe/en/news/all/rss.xml', 'category': 'World News'},
    {'url': 'https://www.defensenews.com/arc/outboundfeeds/rss/?outputType=xml', 'category': 'Defense/Geopolitics'},
]

keywords = [
    # Cybersec/IR/Pentest
    'APT', 'zero-day', 'ransomware', 'cyber attack', 'malware', 'exploit', 'phishing',
    'DDoS', 'CVE-', 'breach', 'vulnerability', 'patch', 'mitigation', 'SIEM',
    'threat intel', 'EDR', 'firewall', 'IDS', 'IPS', 'persistence', 'privilege escalation',
    'incident response', 'forensics', 'C2 server', 'command and control', 'exfiltration',

    # Crypto/Finance
    'crypto', 'bitcoin', 'ethereum', 'blockchain', 'exchange', 'defi', 'NFT', 'wallet',
    'hack', 'crypto scam', 'stablecoin',

    # Cloud/Hardening
    'cloud security', 'AWS', 'Azure', 'GCP', 'IAM', 'misconfiguration', 'WAF', 'container',
    'Docker', 'Kubernetes', 'S3 bucket', 'public exposure', 'hardening', 'benchmark', 'compliance',

    # Law/Crime/Politics
    'espionage', 'nation-state', 'geopolitical', 'sanction', 'arrest', 'indictment', 'law enforcement',
    'FBI', 'NSA', 'CIA', 'conflict', 'election', 'AI regulation', 'social engineering',

    # New Tech
    'AI', 'machine learning', 'deepfake', 'quantum', 'zero trust'
]

def get_articles(feed_urls, keywords):
    articles = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    
    for feed in feed_urls:
        url = feed['url']
        category = feed['category']
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                feed_data = feedparser.parse(response.content)
                for entry in feed_data.entries:
                    if any(keyword.lower() in entry.title.lower() for keyword in keywords):
                        articles.append({
                            'title': entry.title,
                            'link': entry.link,
                            'published': entry.get('published', 'Unknown'),
                            'source': feed_data.feed.get('title', 'Unknown Source'),
                            'content': entry.get('summary', ''),
                            'category': category
                        })
            else:
                print(f"Failed to fetch {url}: HTTP {response.status_code}")
        except Exception as e:
            print(f"Error fetching {url}: {e}")
    return articles

@app.route("/")
def index():
    articles = get_articles(feeds, keywords)
    last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template("index.html", articles=articles, last_updated=last_updated)

if __name__ == "__main__":
    app.run(debug=True)
