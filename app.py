from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock job listings
job_listings = [
    {'id': 1, 'title': 'Software Engineer', 'location': 'Remote'},
    {'id': 2, 'title': 'Data Scientist', 'location': 'Remote'},
    {'id': 3, 'title': 'Frontend Developer', 'location': 'Remote'},
]

# Main route
@app.route('/')
def home():
    return 'Welcome to the Remote Job Solutions API!'

# Job search API
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    search_query = request.args.get('search', '').lower()  # Get search query from URL parameters
    filtered_jobs = [job for job in job_listings if search_query in job['title'].lower()]
    if not filtered_jobs:
        return jsonify({'message': 'No jobs found'}), 404
    return jsonify(filtered_jobs)

if __name__ == '__main__':
    app.run(debug=True)