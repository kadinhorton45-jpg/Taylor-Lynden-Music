async function loadCareerTimeline() {
    const milestones = await API.getMilestones();
    const container = document.getElementById('career-timeline');
    
    if (!milestones || milestones.length === 0) {
        container.innerHTML = '<p>No timeline data available</p>';
        return;
    }

    // Sort by date
    const sorted = milestones.sort((a, b) => new Date(a.date) - new Date(b.date));
    
    container.innerHTML = sorted.map((milestone, index) => `
        <div class="timeline-event" style="margin-bottom: 2rem; padding-left: 2rem; border-left: 3px solid var(--primary-color); position: relative;">
            <div style="position: absolute; left: -12px; top: 0; width: 20px; height: 20px; background: var(--secondary-color); border-radius: 50%; border: 3px solid white;"></div>
            <div style="color: var(--accent-color); font-weight: bold; margin-bottom: 0.5rem;">${formatDate(milestone.date)}</div>
            <h4 style="color: var(--primary-color); margin-bottom: 0.5rem;">${milestone.title}</h4>
            <p>${milestone.description}</p>
            <span style="display: inline-block; background: var(--accent-color); color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem; margin-top: 0.5rem;">${milestone.category}</span>
        </div>
    `).join('');
}

async function loadEras() {
    const eras = await API.getEras();
    const container = document.getElementById('eras-container');
    
    if (!eras || eras.length === 0) {
        container.innerHTML = '<p>No era data available</p>';
        return;
    }

    container.innerHTML = eras.map(era => `
        <div class="era-card" style="background: white; padding: 2rem; border-radius: 10px; margin-bottom: 2rem; box-shadow: var(--shadow);">
            <h3 style="color: var(--primary-color); margin-bottom: 1rem;">${era.name}</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                <div>
                    <strong>Period:</strong> ${era.start_date ? formatDate(era.start_date) : 'TBD'} - ${era.end_date ? formatDate(era.end_date) : 'Ongoing'}
                </div>
                <div>
                    <strong>Tour:</strong> ${era.tour_name || 'N/A'}
                </div>
            </div>
            ${era.shows_count ? `<div><strong>Shows:</strong> ${era.shows_count}</div>` : ''}
            <p style="margin-top: 1rem;">${era.description}</p>
        </div>
    `).join('');
}

async function loadCollaborators() {
    const collabs = await API.getCollaborations();
    const container = document.getElementById('collaborators-list');
    
    if (!collabs || collabs.length === 0) {
        container.innerHTML = '<li>No collaborations recorded</li>';
        return;
    }

    // Get unique artists
    const uniqueArtists = [...new Set(collabs.map(c => c.artist_name))];
    
    container.innerHTML = uniqueArtists.map(artist => `<li>${artist}</li>`).join('');
}

// Load all career content
document.addEventListener('DOMContentLoaded', () => {
    loadCareerTimeline();
    loadEras();
    loadCollaborators();
});
