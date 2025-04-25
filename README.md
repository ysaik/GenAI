# MyGenAI

## Pre-Requsites
* Ubuntu or WSL environment
    [Install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
* Install Python 3.12 or higher version
 

## Setup Python Virtual Environment

### Create python virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install requirements
```bash
(.venv) $ pip install -r requirements.txt
```

## Setup GCP Environment

### Create a Google Cloud Project
[Link](https://console.cloud.google.com/projectselector2/home/dashboard) to create the Project

Refer [How To Guide](https://developers.google.com/workspace/guides/create-project#google-cloud-console)

### Create a Billing Account
[Link](https://console.cloud.google.com/billing?organizationId=0) to create billing account.

### Enable Vertex APIs in Google cloud
You can refer the following guide to enable APIs. Search for `VertexAI` and enable it 
[Enable APIs](https://cloud.google.com/endpoints/docs/openapi/enable-api#console)



### Install gcloud cli
```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates gnupg curl -y

echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee /etc/apt/sources.list.d/google-cloud-sdk.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg

sudo apt update
sudo apt install google-cloud-sdk -y
```

### Initialize and Set Region/Zone
```bash
gcloud init # Authenticates,updated project configuration
gcloud config set project PROJECT_ID  # Refer the Project ID under project in GCP
gcloud config set compute/region us-central1 # Set the region

gcloud config set compute/zone us-central1-a # And Zone

gcloud config list # View default GCP configuration
```

Verify if VertexAI API is enabled
```bash
gcloud services list --enabled --filter="config.name=aiplatform.googleapis.com"
```


## Sample Program
```bash
(.venv) saiky@Saikumar:~/GenAI$ python3 src/first_vertexai.py 
Mr. LLM: Ask your query!!
         or 'quit' to exit: 
You: Hello There!!!
Mr LLM : Hello! How can I help you today? 😊

You : Tell me about Generative AI in 3 lines
Mr LLM : Generative AI creates new content, like text, images, audio, or code, based on learned patterns from existing data.  It leverages algorithms to "understand" the data and then generate novel outputs that resemble it.  Examples include writing articles, designing logos, composing music, and even developing software.

You : Which version of LLM are you using ?
Mr LLM : I am currently running on the Gemini Pro model.

You : Thanks
Mr LLM : You're welcome! Is there anything specific I can help you with today? Let me know what you're thinking or what you need assistance with.

You : quit
```

