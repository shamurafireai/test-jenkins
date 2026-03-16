pipeline {
    agent any

    environment {
        SERVICE_NAME = "myfastapi.service"
        APP_PATH = "/var/lib/jenkins/apps/myfastapi"
        VENV_PATH = "${APP_PATH}/venv"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/shamurafireai/test-jenkins.git'
            }
        }

        stage('Copy Code to App Directory') {
            steps {
                sh """
                mkdir -p ${APP_PATH}
                cp -r * ${APP_PATH}/
                """
            }
        }

        stage('Install Python & Pip') {
            steps {
                sh """
                sudo apt update
                sudo apt install -y python3 python3-pip python3-venv
                python3 --version
                pip3 --version
                """
            }
        }

        stage('Setup Virtualenv') {
            steps {
                sh """
                if [ ! -d "${VENV_PATH}" ]; then
                    python3 -m venv ${VENV_PATH}
                fi
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                sh """
                ${VENV_PATH}/bin/pip install --upgrade pip
                ${VENV_PATH}/bin/pip install -r ${APP_PATH}/requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                ${VENV_PATH}/bin/python -m pytest ${APP_PATH}/tests.py
                """
            }
        }

        stage('Create systemd Service') {
            steps {
                sh """
sudo bash -c 'cat > /etc/systemd/system/${SERVICE_NAME} << EOF
[Unit]
Description=FastAPI Jenkins App
After=network.target

[Service]
User=jenkins
WorkingDirectory=${APP_PATH}
ExecStart=${VENV_PATH}/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always
Environment="PATH=${VENV_PATH}/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin"

[Install]
WantedBy=multi-user.target
EOF'
"""
            }
        }

        stage('Start / Restart Service') {
            steps {
                sh """
                sudo systemctl daemon-reload
                sudo systemctl enable ${SERVICE_NAME}
                sudo systemctl restart ${SERVICE_NAME}
                sudo systemctl status ${SERVICE_NAME} --no-pager
                """
            }
        }

    }

    post {
        always {
            echo 'Deployment finished.'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
