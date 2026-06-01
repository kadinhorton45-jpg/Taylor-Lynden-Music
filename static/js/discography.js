let allAlbums = [];

async function loadDiscography() {
    allAlbums = await API.getAlbums();
    const container = document.getElementById('discography-list');
    
    if (!allAlbums || allAlbums.length === 0) {
        container.innerHTML = '<p>No albums found</p>';
        return;
    }

    displayAlbums(allAlbums);
}

function displayAlbums(albums) {
    const container = document.getElementById('discography-list');
    
    container.innerHTML = albums
        .sort((a, b) => new Date(b.release_date) - new Date(a.release_date))
        .map(album => `
        <div class="discography-item" style="background: white; padding: 1.5rem; margin-bottom: 1rem; border-radius: 10px; display: flex; gap: 2rem; box-shadow: var(--shadow); cursor: pointer;" onclick="window.location.href='/album/${album.id}'">
            <div style="width: 120px; height: 120px; background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-size: 2rem; font-weight: bold; flex-shrink: 0;">${album.album_code || 'TL'}</div>
            <div style="flex: 1;">
                <h3 style="color: var(--primary-color); margin-bottom: 0.5rem;">${album.title}</h3>
                <div style="color: var(--text-secondary); margin-bottom: 0.5rem;">${formatDate(album.release_date)}</div>
                <div style="margin-bottom: 0.5rem;"><strong>Genre:</strong> ${album.genre || 'N/A'}</div>
                ${album.chart_peak ? `<div style="margin-bottom: 0.5rem;"><strong>Chart Peak:</strong> #${album.chart_peak}</div>` : ''}
                ${album.sales_copies ? `<div><strong>Sales:</strong> ${formatNumber(album.sales_copies)} copies</div>` : ''}
                <p style="margin-top: 1rem; color: var(--text-secondary);">${album.description || 'No description available'}</p>
            </div>
        </div>
    `).join('');
}

// Filter functionality
const filterButtons = document.querySelectorAll('.filter-btn');
filterButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
        filterButtons.forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');
        
        const filter = e.target.dataset.filter;
        if (filter === 'all') {
            displayAlbums(allAlbums);
        } else {
            // Filter by type (would need album type field in database)
            displayAlbums(allAlbums);
        }
    });
});

// Load content
document.addEventListener('DOMContentLoaded', () => {
    loadDiscography();
    
    // Add active style to first filter button
    const firstBtn = document.querySelector('.filter-btn');
    if (firstBtn) firstBtn.classList.add('active');
});
