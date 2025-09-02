
cat > README.md <<EOL
# EduBridge Flask Project

## Overview
EduBridge is a web application built using Python Flask and MariaDB. The app provides educational resources, quizzes, a community forum, and a pitch deck for presentations.

## Features
- Home page with welcome message
- Quiz functionality
- Educational resources page
- Community page
- Pitch deck page

## Technologies Used
- Python 3
- Flask
- MariaDB
- HTML, CSS
- Render (for deployment)

## Database
The application connects to MariaDB using the following environment variables:
- \`DB_HOST\`
- \`DB_USER\`
- \`DB_PASSWORD\`
- \`DB_NAME\`

## Running Locally
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/osukemmy/edubridge-flask.git
   \`\`\`
2. Navigate into the project directory and activate the virtual environment:
   \`\`\`bash
   cd edubridge_flask
   python3 -m venv venv
   source venv/bin/activate
   \`\`\`
3. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`
4. Run the app:
   \`\`\`bash
   python app.py
   \`\`\`
5. Open your browser at \`http://127.0.0.1:5000\`.

## Deployment
The app is deployed on Render: [EduBridge Flask Live](https://edubridge-flask-4.onrender.com)

## GitHub Repository
[EduBridge Flask Repo](https://github.com/osukemmy/edubridge-flask)

## Author
Kemunto Ruth Osoro

EOL

