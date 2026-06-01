async function loadLatestAlbums() {
    const albums = await API.getAlbums();
    const container = document.getElementById('latest-albums');
    
    if (!albums || albums.length === 0) {
        container.innerHTML = '<p>No albums found</p>';
        return;
    }

    // Get last 6 albums
    const latest = albums.slice(-6);
    
    container.innerHTML = latest.map(album => `
        <div class="album-card" onclick="window.location.href='/album/${album.id}'">
            <div class="album-cover">${album.album_code || 'TL'}</div>
            <div class="album-info">
                <div class="album-title">${album.title}</div>
                <div class="album-year">${new Date(album.release_date).getFullYear()}</div>
                <span class="album-code">${album.album_code || 'Album'}</span>
            </div>
        </div>
    `).join('');
}

async function loadHighlights() {
    const milestones = await API.getMilestones();
    const container = document.getElementById('milestones-container');
    
    if (!milestones || milestones.length === 0) {
        container.innerHTML = '<p>No milestones found</p>';
        return;
    }

    // Get last 6 milestones
    const featured = milestones.slice(-6);
    
    container.innerHTML = featured.map(milestone => `
        <div class="milestone-card">
            <h3>${milestone.title}</h3>
            <div class="milestone-date">${formatDate(milestone.date)}</div>
            <p>${milestone.description}</p>
            <span class="category-badge" style="background: var(--accent-color); color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem;">${milestone.category}</span>
        </div>
    `).join('');
}

async function loadCollaborations() {
    const collabs = await API.getCollaborations();
    const container = document.getElementById('collabs-container');
    
    if (!collabs || collabs.length === 0) {
        container.innerHTML = '<p>No collaborations found</p>';
        return;
    }

    // Get random 6 collaborations
    const featured = collabs.sort(() => 0.5 - Math.random()).slice(0, 6);
    
    container.innerHTML = featured.map(collab => `
        <div class="collab-card">
            <div class="collab-artist">feat. ${collab.artist_name}</div>
            <div class="collab-track">"${collab.track_title}"</div>
        </div>
    `).join('');
}

async function loadStats() {
    const albums = await API.getAlbums();
    const milestones = await API.getMilestones();
    
    let totalTracks = 0;
    albums.forEach(album => {
        totalTracks += (album.tracks ? album.tracks.length : 0);
    });
    
    document.getElementById('total-albums').textContent = albums.length;
    document.getElementById('total-tracks').textContent = totalTracks;
    document.getElementById('career-span').textContent = calculateCareerSpan();
}

// Load all content
document.addEventListener('DOMContentLoaded', () => {
    loadLatestAlbums();
    loadHighlights();
    loadCollaborations();
    loadStats();
});
