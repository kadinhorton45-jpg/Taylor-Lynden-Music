let allEvents = [];

async function loadFullTimeline() {
    allEvents = await API.getMilestones();
    const container = document.getElementById('full-timeline');
    
    if (!allEvents || allEvents.length === 0) {
        container.innerHTML = '<p>No timeline events found</p>';
        return;
    }

    displayTimeline(allEvents);
}

function displayTimeline(events) {
    const container = document.getElementById('full-timeline');
    
    // Sort by date
    const sorted = events.sort((a, b) => new Date(b.date) - new Date(a.date));
    
    container.innerHTML = sorted.map((event, index) => `
        <div class="timeline-event" style="margin-bottom: 3rem; padding: 2rem; background: white; border-radius: 10px; box-shadow: var(--shadow); border-left: 4px solid var(--secondary-color);">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                <div>
                    <h3 style="color: var(--primary-color); margin-bottom: 0.5rem;">${event.title}</h3>
                    <div style="color: var(--accent-color); font-weight: bold;">${formatDate(event.date)}</div>
                </div>
                <span style="background: var(--accent-color); color: white; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: bold;">${event.category || 'Event'}</span>
            </div>
            <p style="color: var(--text-secondary); margin-bottom: 1rem;">${event.description}</p>
            ${event.image_url ? `<img src="${event.image_url}" style="max-width: 100%; height: auto; border-radius: 8px; margin-top: 1rem;" alt="${event.title}">` : ''}
        </div>
    `).join('');
}

// Search functionality
const searchInput = document.getElementById('timeline-search');
if (searchInput) {
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const filtered = allEvents.filter(event => 
            event.title.toLowerCase().includes(query) || 
            event.description.toLowerCase().includes(query)
        );
        displayTimeline(filtered);
    });
}

// Filter functionality
const categoryFilter = document.getElementById('category-filter');
if (categoryFilter) {
    categoryFilter.addEventListener('change', (e) => {
        const category = e.target.value;
        if (category === 'all') {
            displayTimeline(allEvents);
        } else {
            const filtered = allEvents.filter(event => event.category === category);
            displayTimeline(filtered);
        }
    });
}

// Load content
document.addEventListener('DOMContentLoaded', () => {
    loadFullTimeline();
});
