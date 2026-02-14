// API Base URL
const API_BASE = '/api';

// Initialize the app
document.addEventListener('DOMContentLoaded', function() {
    loadSearches();
    loadResults();
    setupFormSubmit();
    
    // Refresh data every 30 seconds
    setInterval(() => {
        loadSearches();
        loadResults();
    }, 30000);
});

// Setup form submission
function setupFormSubmit() {
    const form = document.getElementById('searchForm');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const destinations = document.getElementById('destinations').value
            .split('\n')
            .map(d => d.trim())
            .filter(d => d.length > 0);
        
        const dateStart = document.getElementById('dateStart').value;
        const dateEnd = document.getElementById('dateEnd').value;
        const checkInterval = parseInt(document.getElementById('checkInterval').value);
        
        if (destinations.length === 0) {
            showMessage('Please enter at least one destination', 'error');
            return;
        }
        
        if (!dateStart || !dateEnd) {
            showMessage('Please select both start and end dates', 'error');
            return;
        }
        
        try {
            const response = await fetch(`${API_BASE}/search`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    destinations: destinations,
                    date_start: dateStart,
                    date_end: dateEnd,
                    check_interval: checkInterval
                })
            });
            
            const data = await response.json();
            
            if (data.success) {
                showMessage('Search created successfully! Check your Telegram for updates.', 'success');
                form.reset();
                loadSearches();
                
                // Reload results after a short delay
                setTimeout(loadResults, 2000);
            } else {
                showMessage(data.error || 'Failed to create search', 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            showMessage('An error occurred while creating the search', 'error');
        }
    });
}

// Load active searches
async function loadSearches() {
    try {
        const response = await fetch(`${API_BASE}/searches`);
        const searches = await response.json();
        
        const container = document.getElementById('activeSearches');
        
        if (searches.length === 0) {
            container.innerHTML = '<p class="info">No active searches. Create one above!</p>';
            return;
        }
        
        container.innerHTML = searches.map(search => `
            <div class="search-item">
                <div class="search-info">
                    <h3>Search #${search.id}</h3>
                    <p><strong>Dates:</strong> ${search.date_start} to ${search.date_end}</p>
                    <p><strong>Check Interval:</strong> Every ${search.check_interval} hours</p>
                    <p><strong>Created:</strong> ${new Date(search.created_at).toLocaleString()}</p>
                    <div class="destination-tags">
                        ${search.destinations.map(dest => `<span class="tag">${dest}</span>`).join('')}
                    </div>
                </div>
                <button class="btn btn-danger" onclick="deleteSearch(${search.id})">Delete</button>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error loading searches:', error);
        document.getElementById('activeSearches').innerHTML = 
            '<p class="error-message">Failed to load searches</p>';
    }
}

// Delete a search
async function deleteSearch(searchId) {
    if (!confirm('Are you sure you want to delete this search?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/search/${searchId}`, {
            method: 'DELETE'
        });
        
        const data = await response.json();
        
        if (data.success) {
            showMessage('Search deleted successfully', 'success');
            loadSearches();
        } else {
            showMessage('Failed to delete search', 'error');
        }
    } catch (error) {
        console.error('Error deleting search:', error);
        showMessage('An error occurred while deleting the search', 'error');
    }
}

// Load results
async function loadResults() {
    try {
        const response = await fetch(`${API_BASE}/results`);
        const results = await response.json();
        
        const container = document.getElementById('results');
        
        if (results.length === 0) {
            container.innerHTML = '<p class="info">No results yet. Results will appear after the first check.</p>';
            return;
        }
        
        container.innerHTML = results.slice(0, 10).map(result => {
            const details = result.details || {};
            const priceRange = details.estimated_price_range || {};
            const tips = details.tips || [];
            
            return `
                <div class="result-item">
                    <div class="result-header">
                        <h3>${result.destination}</h3>
                        <div class="price">
                            $${priceRange.min || 'N/A'} - $${priceRange.max || 'N/A'}
                        </div>
                    </div>
                    <div class="result-details">
                        <p><strong>📅 Date Range:</strong> ${details.date_range || 'N/A'}</p>
                        <p><strong>⏰ Best Booking Time:</strong> ${details.best_booking_time || 'N/A'}</p>
                        <p><strong>🕐 Checked At:</strong> ${new Date(result.checked_at).toLocaleString()}</p>
                        ${tips.length > 0 ? `
                            <div class="tips">
                                <strong>💡 Tips:</strong>
                                <ul>
                                    ${tips.map(tip => `<li>${tip}</li>`).join('')}
                                </ul>
                            </div>
                        ` : ''}
                    </div>
                </div>
            `;
        }).join('');
        
        // Load charts for destinations with multiple data points
        loadCharts(results);
    } catch (error) {
        console.error('Error loading results:', error);
        document.getElementById('results').innerHTML = 
            '<p class="error-message">Failed to load results</p>';
    }
}

// Load price charts
async function loadCharts(results) {
    const chartsContainer = document.getElementById('charts');
    
    // Group results by destination
    const destinationData = {};
    results.forEach(result => {
        if (!destinationData[result.destination]) {
            destinationData[result.destination] = [];
        }
        destinationData[result.destination].push(result);
    });
    
    // Filter destinations with at least 2 data points
    const destinationsWithHistory = Object.keys(destinationData)
        .filter(dest => destinationData[dest].length >= 2);
    
    if (destinationsWithHistory.length === 0) {
        chartsContainer.innerHTML = '<p class="info">Charts will appear after multiple price checks for the same destination</p>';
        return;
    }
    
    chartsContainer.innerHTML = destinationsWithHistory.map(destination => `
        <div class="chart-wrapper">
            <h3>${destination}</h3>
            <canvas id="chart-${destination.replace(/[^a-zA-Z0-9]/g, '-')}"></canvas>
        </div>
    `).join('');
    
    // Create charts
    destinationsWithHistory.forEach(destination => {
        const data = destinationData[destination].reverse();
        const chartId = `chart-${destination.replace(/[^a-zA-Z0-9]/g, '-')}`;
        const ctx = document.getElementById(chartId);
        
        if (ctx) {
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.map(d => new Date(d.checked_at).toLocaleDateString()),
                    datasets: [{
                        label: 'Price (USD)',
                        data: data.map(d => d.price),
                        borderColor: '#667eea',
                        backgroundColor: 'rgba(102, 126, 234, 0.1)',
                        tension: 0.4,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top'
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: false,
                            ticks: {
                                callback: function(value) {
                                    return '$' + value;
                                }
                            }
                        }
                    }
                }
            });
        }
    });
}

// Show message to user
function showMessage(message, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = type === 'success' ? 'success-message' : 'error-message';
    messageDiv.textContent = message;
    
    const searchSection = document.querySelector('.search-section');
    searchSection.insertBefore(messageDiv, searchSection.firstChild);
    
    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}
