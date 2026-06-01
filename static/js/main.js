// Global API functions
const API = {
    getAlbums: async () => {
        const response = await fetch('/api/albums');
        return response.json();
    },
    getAlbum: async (id) => {
        const response = await fetch(`/api/albums/${id}`);
        return response.json();
    },
    getMilestones: async () => {
        const response = await fetch('/api/milestones');
        return response.json();
    },
    getCollaborations: async () => {
        const response = await fetch('/api/collaborations');
        return response.json();
    },
    getEras: async () => {
        const response = await fetch('/api/eras');
        return response.json();
    }
};

// Utility functions
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

function formatNumber(num) {
    return new Intl.NumberFormat().format(num);
}

function calculateCareerSpan() {
    const startYear = 2005;  // Taylor's first release
    const currentYear = new Date().getFullYear();
    return currentYear - startYear;
}

// Update last updated timestamp
function updateLastUpdatedTime() {
    const lastUpdated = document.getElementById('last-updated');
    if (lastUpdated) {
        lastUpdated.textContent = formatDate(new Date());
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateLastUpdatedTime();
});
