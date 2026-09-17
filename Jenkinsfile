pipeline {
    agent any

    stages {
        stage('Generate Report') {
            steps {
                echo 'Executing student performance processing script...'
                // Executes the python logic script on Windows Agent
                bat 'python app.py'
            }
        }
        
        stage('Archive Report') {
            steps {
                echo 'Archiving the generated academic performance artifact...'
                // Saves report.txt to the Jenkins UI for future downloads
                archiveArtifacts artifacts: 'report.txt', fingerprint: true
            }
        }
    }
}
