from app import app, db, Album, Track, Milestone, Collaboration, Era
from datetime import datetime, date

def seed_database():
    """Seed the database with Taylor Lynden's career data"""
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Taylor's Little Dream (2006)
        album1 = Album(
            title="Taylor's Little Dream",
            release_date=date(2006, 5, 15),
            album_code="TL0",
            description="Taylor's debut independent album featuring 12 songs recorded in her high school studio.",
            genre="Acoustic Pop",
            sales_copies=500,
            chart_peak=None,
            producer_notes="Recorded during senior year in high school with teacher assistance."
        )
        
        tracks_album1 = [
            Track(album=album1, title="Vermont", track_number=1, duration="3:45", story="A personal reflection on growing up in Vermont"),
            Track(album=album1, title="Loverboy", track_number=2, duration="3:12"),
            Track(album=album1, title="Momma's Very Own", track_number=3, duration="2:58"),
            Track(album=album1, title="House", track_number=4, duration="3:33"),
            Track(album=album1, title="Smiling in Pain", track_number=5, duration="3:15"),
            Track(album=album1, title="Will I Ever See You Again", track_number=6, duration="3:47"),
        ]
        
        db.session.add(album1)
        db.session.add_all(tracks_album1)
        
        # The Bloom Tape (2009)
        album2 = Album(
            title="The Bloom Tape",
            release_date=date(2009, 1, 15),
            album_code="TL0.5",
            description="Debut professional album blending acoustic pop with hip-hop elements.",
            genre="Pop/Hip-Hop Fusion",
            sales_copies=30000,
            chart_peak=199,
            producer_notes="Pressed 30,011 copies. Vampire Valentine reached #199 on Billboard Hot 100."
        )
        
        tracks_album2 = [
            Track(album=album2, title="Soul Flower Bloom", track_number=1, duration="3:22", is_single=False),
            Track(album=album2, title="Summer Message", track_number=2, duration="3:01", is_single=False),
            Track(album=album2, title="Down", track_number=3, duration="2:45", is_single=False),
            Track(album=album2, title="Bees and Trees", track_number=4, duration="3:33", is_single=False),
            Track(album=album2, title="Corner Street", track_number=5, duration="3:15", is_single=False),
            Track(album=album2, title="Breaking My Heart", track_number=6, duration="3:47", is_single=False),
            Track(album=album2, title="College Girl", track_number=7, duration="3:28", is_single=False),
            Track(album=album2, title="Vampire Valentine", track_number=8, duration="3:56", is_single=True, chart_position=199),
        ]
        
        db.session.add(album2)
        db.session.add_all(tracks_album2)
        
        # Taylor Lynden (2010)
        album3 = Album(
            title="Taylor Lynden",
            release_date=date(2010, 1, 15),
            album_code="TL1",
            description="Major label debut under Columbia Records, featuring the hit single 'Glovebox'.",
            genre="Country Pop/Dream Pop",
            label="Columbia Records",
            sales_copies=500000,
            chart_peak=6,
            producer_notes="First album under Columbia Records 4-album deal. Glovebox peaked at #6."
        )
        
        tracks_album3 = [
            Track(album=album3, title="Back To The Small Town", track_number=1, duration="3:32"),
            Track(album=album3, title="Flowers", track_number=2, duration="3:45"),
            Track(album=album3, title="Go Girl", track_number=3, duration="3:18", features="Justin Bieber"),
            Track(album=album3, title="Picture in Your Wallet", track_number=4, duration="3:52"),
            Track(album=album3, title="Glovebox", track_number=5, duration="3:41", is_single=True, chart_position=6),
        ]
        
        db.session.add(album3)
        db.session.add_all(tracks_album3)
        
        # Purple Roses (2011)
        album4 = Album(
            title="Purple Roses",
            release_date=date(2011, 4, 15),
            album_code="TL2",
            description="Sophomore album featuring collaboration with Taylor Swift. Became iconic album of the era.",
            genre="Pop",
            label="Columbia Records",
            sales_copies=1607122,
            chart_peak=1,
            awards="Multiple Grammy nominations, sold 1.6M+ copies worldwide",
            producer_notes="Instant hit with critics and fans. Features 'Horror Scope' with Taylor Swift."
        )
        
        tracks_album4 = [
            Track(album=album4, title="Sunshine State", track_number=1, duration="3:28"),
            Track(album=album4, title="College Girl (21)", track_number=2, duration="3:52", features="Carly Rae Jepsen"),
            Track(album=album4, title="Purple", track_number=3, duration="3:15"),
            Track(album=album4, title="Outside The Baseball Field", track_number=4, duration="3:41"),
            Track(album=album4, title="Horror Scope", track_number=7, duration="3:56", features="Taylor Swift", is_single=True),
            Track(album=album4, title="We Are Never Seeing Each Other Again", track_number=11, duration="3:33", is_single=True, chart_position=1),
        ]
        
        db.session.add(album4)
        db.session.add_all(tracks_album4)
        
        # Homecoming (2014)
        album5 = Album(
            title="Homecoming",
            release_date=date(2014, 6, 20),
            album_code="TL3",
            description="Third studio album blending traditional pop with hip-hop elements. Major commercial success.",
            genre="Pop/Hip-Hop",
            label="Columbia Records",
            sales_copies=800000,
            chart_peak=1,
            producer_notes="Massive commercial success. Every single charted in top 30."
        )
        
        db.session.add(album5)
        
        # Little Old House On Top (2016)
        album6 = Album(
            title="Little Old House On Top",
            release_date=date(2016, 9, 2),
            album_code="TL4",
            description="Introspective album returning to roots with modern production. Compared to Taylor Swift's 'Red'.",
            genre="Pop/Indie Pop",
            label="Columbia Records",
            sales_copies=603000,
            chart_peak=1,
            producer_notes="Album returned to roots while maintaining modern sound. 14 of 15 songs charted in top 15."
        )
        
        db.session.add(album6)
        
        # Coming Of Age (2023)
        album7 = Album(
            title="Coming Of Age",
            release_date=date(2023, 5, 1),
            album_code="TL7",
            description="Upbeat bubblegum pop album marking personal identity discovery. Massive comeback.",
            genre="Pop",
            sales_copies=900000,
            chart_peak=1,
            producer_notes="Breakthrough album post-independence. Achieved 6+ billion streams."
        )
        
        db.session.add(album7)
        
        # The Night Tape (2026)
        album8 = Album(
            title="The Night Tape",
            release_date=date(2026, 5, 29),
            album_code="TL8",
            description="Latest album featuring collaborations with Keshi, Conan Grey, and DC The Don.",
            genre="Synth-Pop/Alternative",
            producer_notes="Features highly sought-after collaborations. Marks significant sonic shift."
        )
        
        db.session.add(album8)
        
        # Add Milestones
        milestones = [
            Milestone(title="Started Piano Lessons", date=date(1997, 9, 1), category="personal", description="Taylor began formal music training in 1st grade."),
            Milestone(title="Joined Choir", date=date(2003, 9, 1), category="career", description="Entered choir in 6th grade, already ahead of peers."),
            Milestone(title="First Concert Solo", date=date(2008, 5, 20), category="achievement", description="Performed 'Vermont' solo at senior choir concert."),
            Milestone(title="First EP Release", date=date(2006, 5, 15), category="career", description="Released 'Taylor's Little Dream' with 500 CDs pressed."),
            Milestone(title="Sold Out Madison Square Garden", date=date(2014, 7, 11), category="achievement", description="First tour show was sold-out MSG with 20,789 people."),
            Milestone(title="Columbia Records Deal", date=date(2009, 9, 1), category="career", description="Signed 4-album deal with Columbia Records for $800,000."),
            Milestone(title="Met Taylor Swift", date=date(2012, 4, 1), category="collaboration", description="Started touring with Taylor Swift, met in person."),
            Milestone(title="Became Independent", date=date(2018, 1, 1), category="career", description="Completed Columbia Records deal, became independent artist."),
        ]
        
        db.session.add_all(milestones)
        
        # Add Collaborations
        collaborations = [
            Collaboration(artist_name="Justin Bieber", track_title="Go Girl", album_id=3, date=date(2010, 1, 15), role="feature"),
            Collaboration(artist_name="Taylor Swift", track_title="Horror Scope", album_id=4, date=date(2011, 4, 15), role="feature"),
            Collaboration(artist_name="Taylor Swift", track_title="Sad Hello, Goodbye", album_id=4, date=date(2012, 3, 10), role="feature"),
            Collaboration(artist_name="The Weeknd", track_title="On The Nose", date=date(2023, 7, 14), role="feature"),
            Collaboration(artist_name="Kendrick Lamar", track_title="On Repeat", date=date(2024, 11, 1), role="feature"),
            Collaboration(artist_name="Keshi", track_title="Right Spot", album_id=8, date=date(2026, 5, 29), role="feature"),
            Collaboration(artist_name="Conan Grey", track_title="Across The Street", album_id=8, date=date(2026, 5, 29), role="feature"),
        ]
        
        db.session.add_all(collaborations)
        
        # Add Eras
        eras = [
            Era(
                name="The Glovebox Era",
                album_id=3,
                start_date=date(2010, 1, 1),
                end_date=date(2010, 12, 31),
                description="First major label era"
            ),
            Era(
                name="Purple Roses / Purple Once Again Tour",
                album_id=4,
                start_date=date(2011, 4, 1),
                end_date=date(2012, 12, 31),
                tour_name="Purple Once Again Tour with Taylor Swift",
                shows_count=89,
                description="Career-defining era with Taylor Swift collaboration"
            ),
            Era(
                name="Homecoming World Tour",
                album_id=5,
                start_date=date(2014, 7, 1),
                end_date=date(2015, 8, 31),
                tour_name="Homecoming World Tour",
                shows_count=142,
                description="Year-long world tour"
            ),
            Era(
                name="Coming Of Age",
                album_id=7,
                start_date=date(2023, 5, 1),
                end_date=date(2023, 12, 31),
                tour_name="Coming Of Age On Tour",
                shows_count=71,
                description="Major comeback era with multiple EPs and collaborations"
            ),
        ]
        
        db.session.add_all(eras)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
