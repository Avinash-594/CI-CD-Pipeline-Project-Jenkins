pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Avinash-594/product-price-pipeline.git'
            }
        }

        stage('Install Python Libs') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Data Script') {
            steps {
                sh 'python3 scripts/fetch_and_filter.py'
            }
        }

        stage('Upload to S3') {
            steps {
                sh 'aws s3 cp filtered_products_*.json s3://your-bucket-name/'
            }
        }
    }
}
