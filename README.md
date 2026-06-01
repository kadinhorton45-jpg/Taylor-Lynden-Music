# Taylor Lynden Music Career Website

A comprehensive interactive website documenting Taylor Lynden's complete music career from 2005 to present.

## Features

- **Interactive Timeline**: Complete career timeline with milestones and achievements
- **Discography**: Full album catalog with tracks, features, and chart performance
- **Album Details**: In-depth information for each album including:
  - Tracklists with featuring artists
  - Chart positions and sales figures
  - Producer notes and album stories
  - Era information and tours
- **Career Story**: Detailed biography and career progression
- **Collaborations**: Showcase of notable artist collaborations
- **Responsive Design**: Mobile-friendly interface
- **Admin API**: Easy content management for new releases

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite (easily switchable to PostgreSQL)
- **Frontend**: HTML/CSS/JavaScript
- **Server**: Gunicorn for production

## Project Structure

```
.
├── app.py                 # Main Flask application
├── seed_data.py          # Database seeding script
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
├── templates/
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── career.html       # Career story page
│   ├── discography.html  # Complete discography
│   ├── timeline.html     # Full timeline
│   └── album_detail.html # Individual album pages
└── static/
    ├── css/
    │   ├── style.css     # Main styling
    │   └── responsive.css # Mobile responsive styles
    └── js/
        ├── main.js       # Global functions
        ├── index.js      # Homepage logic
        ├── career.js     # Career page logic
        ├── discography.js # Discography page logic
        ├── timeline.js   # Timeline page logic
        └── album_detail.js # Album detail page logic
```

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/kadinhorton45-jpg/taylor-lynden-music.git
cd taylor-lynden-music
```

### 2. Set Up Python Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

### 5. Seed Database
```bash
python seed_data.py
```

### 6. Run Development Server
```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

## Deployment on Custom Server

### Using Gunicorn (Recommended)

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Nginx as Reverse Proxy

Create `/etc/nginx/sites-available/taylor-lynden`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/taylor-lynden-music/static;
        expires 30d;
    }
}
```

### Using Systemd Service

Create `/etc/systemd/system/taylor-lynden.service`:

```ini
[Unit]
Description=Taylor Lynden Music Website
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/taylor-lynden-music
Environment="PATH=/path/to/taylor-lynden-music/venv/bin"
ExecStart=/path/to/taylor-lynden-music/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

### Enable and Start Service

```bash
sudo systemctl daemon-reload
sudo systemctl enable taylor-lynden
sudo systemctl start taylor-lynden
sudo systemctl status taylor-lynden
```

## API Endpoints

### Public Endpoints
- `GET /api/albums` - Get all albums
- `GET /api/albums/<id>` - Get specific album
- `GET /api/milestones` - Get all milestones
- `GET /api/collaborations` - Get all collaborations
- `GET /api/eras` - Get all eras

### Admin Endpoints (Add authentication in production)
- `POST /api/admin/album` - Add new album
- `POST /api/admin/track` - Add track to album
- `POST /api/admin/milestone` - Add milestone
- `POST /api/admin/collaboration` - Add collaboration

## Adding New Releases

### Via API

```bash
curl -X POST http://localhost:5000/api/admin/album \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Album",
    "release_date": "2026-06-01",
    "album_code": "TL9",
    "description": "Album description",
    "genre": "Pop",
    "sales_copies": 500000,
    "chart_peak": 1
  }'
```

### Database Update

Edit `seed_data.py` to include new data and re-run:

```bash
python seed_data.py
```

## Database Models

### Album
- title, release_date, album_code
- cover_art, description, genre, label
- sales_copies, chart_peak, awards
- producer_notes, created_at

### Track
- title, track_number, duration
- features, is_single, chart_position
- streams, lyrics_snippet, story

### Milestone
- title, date, category (achievement/collaboration/personal/career)
- description, image_url, related_album_id

### Collaboration
- artist_name, track_title, album_id
- date, description, role (feature/producer/writer)

### Era
- name, album_id, start_date, end_date
- tour_name, shows_count, merchandise, milestones, description

## Customization

### Styling
Edit `static/css/style.css` to customize colors, fonts, and layout.

Key CSS variables:
- `--primary-color`: #6b5b95 (Purple)
- `--secondary-color`: #ff6b9d (Pink)
- `--accent-color`: #ffc933 (Yellow)

### Content
Modify `seed_data.py` to update career information and album data.

## Production Checklist

- [ ] Set `FLASK_ENV=production`
- [ ] Set `FLASK_DEBUG=False`
- [ ] Add authentication to admin endpoints
- [ ] Use PostgreSQL instead of SQLite
- [ ] Set up SSL/HTTPS
- [ ] Configure error logging
- [ ] Set up database backups
- [ ] Add rate limiting to API
- [ ] Implement caching
- [ ] Set up monitoring

## License

This project is created for Taylor Lynden's music career documentation.

## Support

For issues or questions, please create an issue in the GitHub repository.
