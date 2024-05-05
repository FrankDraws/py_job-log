document.addEventListener('DOMContentLoaded', function () {
    const jobList = document.getElementById('job-list');
    const jobDetails = document.getElementById('job-details');

    // Function to display job details
    function showJobDetails(event, job) {
        event.preventDefault(); // Prevent the default behavior of navigating to a new page
        
        // Store the job details in sessionStorage
        sessionStorage.setItem('selectedJob', JSON.stringify(job));

        // Navigate to the job-details.html page in the same window
        window.location.href = 'job-details.html';
    }

    // Function to populate job list
    function populateJobList(jobs) {
        jobList.innerHTML = ''; // Clear previous list
        jobs.forEach(function(job) {
            const listItem = document.createElement('li');
            listItem.textContent = `${job.date} / ${job.company}`;
            listItem.addEventListener('click', function(event) {
                showJobDetails(event, job);
            });
            jobList.appendChild(listItem);
        });
    }

    // Fetch job data from Flask server
    fetch('/')
        .then(response => response.json())
        .then(data => {
            populateJobList(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});

// Python log data script
function logData() {
    var data = {
        Date: new Date().toISOString(),
        Company: document.getElementById("company").value,
        Position: document.getElementById("position").value,
        Description: document.getElementById("description").value
    };

    // Send data to Python script for logging
    fetch('/log_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.ok) {
            console.log('Data logged successfully.');
            // You can perform additional actions here, like refreshing the UI
        } else {
            console.error('Failed to log data.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
