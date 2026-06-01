let currentAlbumId = null;

async function loadAlbumDetail() {
    const urlParams = new URLSearchParams(window.location.search);
    const albumId = urlParams.get('id') || 1;
    currentAlbumId = albumId;
    
    try {
        const album = await API.getAlbum(albumId);
        displayAlbumHero(album);
        displayTracks(album.tracks);
        displayAlbumInfo(album);
    } catch (error) {
        console.error('Error loading album:', error);
        document.getElementById('album-detail').innerHTML = '<div class="container"><p>Album not found</p></div>';
    }
}

function displayAlbumHero(album) {
    const hero = document.getElementById('album-hero');
    hero.innerHTML = `
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center;">
            <div style="width: 100%; height: 400px; background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-size: 5rem; font-weight: bold;">${album.album_code || 'TL'}</div>
            <div>
                <h1 style="font-size: 3rem; color: var(--primary-color); margin-bottom: 1rem;">${album.title}</h1>
                <div style="font-size: 1.3rem; color: var(--text-secondary); margin-bottom: 2rem;">${formatDate(album.release_date)}</div>
                ${album.description ? `<p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 2rem;">${album.description}</p>` : ''}
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                    ${album.genre ? `<div><strong style="color: var(--primary-color);">Genre</strong><div>${album.genre}</div></div>` : ''}
                    ${album.label ? `<div><strong style="color: var(--primary-color);">Label</strong><div>${album.label}</div></div>` : ''}
                    ${album.chart_peak ? `<div><strong style="color: var(--primary-color);">Chart Peak</strong><div>#${album.chart_peak}</div></div>` : ''}
                    ${album.sales_copies ? `<div><strong style="color: var(--primary-color);">Sales</strong><div>${formatNumber(album.sales_copies)} copies</div></div>` : ''}
                </div>
            </div>
        </div>
    `;
}

function displayTracks(tracks) {
    const container = document.getElementById('tracks-container');
    
    if (!tracks || tracks.length === 0) {
        container.innerHTML = '<p>No tracks available</p>';
        return;
    }

    container.innerHTML = tracks.map((track, index) => `
        <div style="background: ${index % 2 === 0 ? '#f9f9f9' : 'white'}; padding: 1.5rem; display: grid; grid-template-columns: 50px 1fr 100px; gap: 1.5rem; align-items: center; border-bottom: 1px solid var(--border-color);">
            <div style="text-align: center; font-weight: bold; color: var(--primary-color); font-size: 1.2rem;">${track.track_number || index + 1}</div>
            <div>
                <div style="font-weight: bold; color: var(--primary-color);">${track.title}</div>
                ${track.features ? `<div style="font-size: 0.9rem; color: var(--text-secondary);">feat. ${track.features}</div>` : ''}
                ${track.story ? `<div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 0.5rem;">${track.story}</div>` : ''}
            </div>
            <div style="text-align: right; color: var(--text-secondary);">${track.duration || '-'}</div>
        </div>
    `).join('');
}

function displayAlbumInfo(album) {
    const info = document.getElementById('album-info');
    info.innerHTML = `
        <h3 style="color: var(--primary-color); margin-bottom: 1.5rem;">Album Information</h3>
        ${album.album_code ? `<div style="margin-bottom: 1rem;"><strong>Album Code:</strong> ${album.album_code}</div>` : ''}
        ${album.genre ? `<div style="margin-bottom: 1rem;"><strong>Genre:</strong> ${album.genre}</div>` : ''}
        ${album.label ? `<div style="margin-bottom: 1rem;"><strong>Label:</strong> ${album.label}</div>` : ''}
        ${album.chart_peak ? `<div style="margin-bottom: 1rem;"><strong>Chart Peak Position:</strong> #${album.chart_peak}</div>` : ''}
        ${album.sales_copies ? `<div style="margin-bottom: 1rem;"><strong>Physical Sales:</strong> ${formatNumber(album.sales_copies)}</div>` : ''}
        ${album.awards ? `<div style="margin-bottom: 1rem;"><strong>Awards & Recognition:</strong><p>${album.awards}</p></div>` : ''}
        ${album.producer_notes ? `<div style="margin-bottom: 1rem;"><strong>Producer Notes:</strong><p>${album.producer_notes}</p></div>` : ''}
    `;
}

// Load content
document.addEventListener('DOMContentLoaded', () => {
    loadAlbumDetail();
});
