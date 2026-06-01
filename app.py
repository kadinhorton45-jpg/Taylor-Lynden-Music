from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///taylor_lynden.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    album_code = db.Column(db.String(10), unique=True)
    cover_art = db.Column(db.String(500))
    description = db.Column(db.Text)
    genre = db.Column(db.String(100))
    label = db.Column(db.String(100))
    sales_copies = db.Column(db.Integer)
    chart_peak = db.Column(db.Integer)
    awards = db.Column(db.Text)
    producer_notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tracks = db.relationship('Track', backref='album', lazy=True, cascade='all, delete-orphan')
    era = db.relationship('Era', backref='album', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date.isoformat(),
            'album_code': self.album_code,
            'cover_art': self.cover_art,
            'description': self.description,
            'genre': self.genre,
            'label': self.label,
            'sales_copies': self.sales_copies,
            'chart_peak': self.chart_peak,
            'awards': self.awards,
            'producer_notes': self.producer_notes,
            'tracks': [track.to_dict() for track in self.tracks]
        }

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    track_number = db.Column(db.Integer)
    duration = db.Column(db.String(10))
    features = db.Column(db.String(500))
    is_single = db.Column(db.Boolean, default=False)
    chart_position = db.Column(db.Integer)
    streams = db.Column(db.Integer)
    lyrics_snippet = db.Column(db.Text)
    story = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'track_number': self.track_number,
            'duration': self.duration,
            'features': self.features,
            'is_single': self.is_single,
            'chart_position': self.chart_position,
            'streams': self.streams,
            'lyrics_snippet': self.lyrics_snippet,
            'story': self.story
        }

class Era(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    tour_name = db.Column(db.String(200))
    shows_count = db.Column(db.Integer)
    merchandise = db.Column(db.Text)
    milestones = db.Column(db.Text)
    description = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'tour_name': self.tour_name,
            'shows_count': self.shows_count,
            'merchandise': self.merchandise,
            'milestones': self.milestones,
            'description': self.description
        }

class Milestone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(100))  # 'achievement', 'collaboration', 'personal', 'career'
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    related_album_id = db.Column(db.Integer, db.ForeignKey('album.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date.isoformat(),
            'category': self.category,
            'description': self.description,
            'image_url': self.image_url,
            'related_album_id': self.related_album_id
        }

class Collaboration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(200), nullable=False)
    track_title = db.Column(db.String(200), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))
    date = db.Column(db.Date)
    description = db.Column(db.Text)
    role = db.Column(db.String(100))  # 'feature', 'producer', 'writer'

    def to_dict(self):
        return {
            'id': self.id,
            'artist_name': self.artist_name,
            'track_title': self.track_title,
            'album_id': self.album_id,
            'date': self.date.isoformat() if self.date else None,
            'description': self.description,
            'role': self.role
        }

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/discography')
def discography():
    return render_template('discography.html')

@app.route('/album/<int:album_id>')
def album_detail(album_id):
    return render_template('album_detail.html')

# API Routes
@app.route('/api/albums')
def get_albums():
    albums = Album.query.order_by(Album.release_date).all()
    return jsonify([album.to_dict() for album in albums])

@app.route('/api/albums/<int:album_id>')
def get_album(album_id):
    album = Album.query.get_or_404(album_id)
    return jsonify(album.to_dict())

@app.route('/api/milestones')
def get_milestones():
    milestones = Milestone.query.order_by(Milestone.date).all()
    return jsonify([m.to_dict() for m in milestones])

@app.route('/api/collaborations')
def get_collaborations():
    collabs = Collaboration.query.all()
    return jsonify([c.to_dict() for c in collabs])

@app.route('/api/eras')
def get_eras():
    eras = Era.query.all()
    return jsonify([e.to_dict() for e in eras])

# Admin Routes (Protected in production)
@app.route('/api/admin/album', methods=['POST'])
def add_album():
    data = request.json
    album = Album(
        title=data['title'],
        release_date=datetime.fromisoformat(data['release_date']).date(),
        album_code=data.get('album_code'),
        cover_art=data.get('cover_art'),
        description=data.get('description'),
        genre=data.get('genre'),
        label=data.get('label'),
        sales_copies=data.get('sales_copies'),
        chart_peak=data.get('chart_peak'),
        awards=data.get('awards'),
        producer_notes=data.get('producer_notes')
    )
    db.session.add(album)
    db.session.commit()
    return jsonify(album.to_dict()), 201

@app.route('/api/admin/track', methods=['POST'])
def add_track():
    data = request.json
    track = Track(
        album_id=data['album_id'],
        title=data['title'],
        track_number=data.get('track_number'),
        duration=data.get('duration'),
        features=data.get('features'),
        is_single=data.get('is_single', False),
        chart_position=data.get('chart_position'),
        streams=data.get('streams'),
        lyrics_snippet=data.get('lyrics_snippet'),
        story=data.get('story')
    )
    db.session.add(track)
    db.session.commit()
    return jsonify(track.to_dict()), 201

@app.route('/api/admin/milestone', methods=['POST'])
def add_milestone():
    data = request.json
    milestone = Milestone(
        title=data['title'],
        date=datetime.fromisoformat(data['date']).date(),
        category=data.get('category'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        related_album_id=data.get('related_album_id')
    )
    db.session.add(milestone)
    db.session.commit()
    return jsonify(milestone.to_dict()), 201

@app.route('/api/admin/collaboration', methods=['POST'])
def add_collaboration():
    data = request.json
    collab = Collaboration(
        artist_name=data['artist_name'],
        track_title=data['track_title'],
        album_id=data.get('album_id'),
        date=datetime.fromisoformat(data['date']).date() if data.get('date') else None,
        description=data.get('description'),
        role=data.get('role')
    )
    db.session.add(collab)
    db.session.commit()
    return jsonify(collab.to_dict()), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
