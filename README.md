```bash
conda create -n jenkins-env python=3.10 -y
conda activate jenkins-env
pip install -r src/requirments.txt
pip install .   # to build the package
```

## Test the FastAPI
at request body
```json

{
  "Gender": "Male",
  "Married": "No",
  "Dependents": "2",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5849,
  "CoapplicantIncome": 0,
  "LoanAmount": 1000,
  "Loan_Amount_Term": 1,
  "Credit_History": 1.0,
  "Property_Area": "Rural"
}

```

## Dokarizing the project

```bash
docker build -t loan_pred:v1 .

docker build -t sadhiin/cicd_jenkins:latest .
docker push sadhiin/cicd_jenkins:latest

docker run -d -it --name modelv1 -p 5000:8888 sadhiin/cicd_jenkins:latest bash

docker exec modelv1 python prediction_model/training_pipeline.py

docker exec modelv1 pytest -v --junitxml=TestResults.xml --cache-clear

docker cp modelv1:/app/src/TestResults.xml .

docker exec -d  -w /app modelv1 python main.py

docker exec -d  -w /app modelv1 sh -c "python main.py &"    # [for the long running/loop run process]

docker exe -w /src modelv1 uvicorn main:app --proxy-headers --host 0.0.0.0 --post 8888
```


# Installation of Jenkins

Source: [https://www.jenkins.io/doc/book/installing/linux/#debianubuntu](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu)
```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins

sudo apt update
sudo apt install fontconfig openjdk-17-jre
java -version



sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

# [Installing docker in Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update


sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

```
Update the package index: ```sudo apt update -y```
Install Docker: ```sudo apt install -y docker.io```
Start the Docker service: ```sudo systemctl start docker```
Enable Docker to start automatically on boot: ```sudo systemctl enable docker```


### To be able to call Jenkins docker
```bash
# Adding jenkins as super user
sudo usermod -a -G docker jenkins

# Adding current user as well
sudo usermod -a -G docker $USER
```

## Please check the all update on main branch.