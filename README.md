 <div align="center">

# ☁️ AWS Cloud Management Dashboard

### Manage your AWS infrastructure through a simple, interactive web interface.

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-CLI-orange?logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
</p>

</div>

---

## 🚀 About the Project

AWS Cloud Management Dashboard is a Python-based web application built with **Streamlit** that allows users to manage and monitor AWS resources through a graphical interface.

Instead of manually executing AWS CLI commands in the terminal, users can perform common cloud management operations directly from the dashboard.

The application uses **AWS CLI through Python's subprocess module** to communicate with AWS services.

## ✨ Features

| Service | Capabilities |
|---|---|
| 🖥️ **EC2** | Launch, view, start, stop, reboot and terminate instances |
| 🪣 **S3** | Create, view and manage S3 buckets and objects |
| 🔐 **IAM** | Manage IAM users, roles and policies |
| ⚡ **Lambda** | Manage Lambda functions |
| 🌐 **API Gateway** | Access API Gateway management features |
| 👤 **Account** | View AWS account information |

## ⚙️ How It Works

<div align="center">

**Streamlit Dashboard**

⬇️

**Python Service Layer**

⬇️

**AWS CLI Commands**

⬇️

**AWS Cloud Services**

</div>

The dashboard executes AWS CLI commands using Python, processes the returned JSON responses, and displays the results in the web interface.

## 🛠️ Tech Stack

- **Python** – Application logic and AWS command execution
- **Streamlit** – Interactive web interface
- **AWS CLI** – Communication with AWS services
- **Pandas** – Data handling and tabular display
- **JSON** – Processing AWS responses
- **CSS** – Dashboard styling

## 📥 Getting Started

### 1. Prerequisites

Make sure you have:

- Python 3 installed
- AWS CLI installed
- An AWS account
- AWS credentials configured

### 2. Clone the Repository

```bash
git clone https://github.com/ayush-kumawat-0/AWS-CLI-Dashboard-Streamlit
```

```bash
cd your-repository
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure AWS CLI

Run the following command:

```bash
aws configure
```

Provide your AWS Access Key, Secret Access Key, preferred region, and output format.

Verify your AWS connection:

```bash
aws sts get-caller-identity
```

### 5. Run the Dashboard

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 🖱️ How to Use

1. **Open the dashboard** using the Streamlit URL.
2. **Select an AWS service** from the sidebar.
3. **View your resources** and their current details.
4. **Choose an operation**, such as launching an EC2 instance or creating an S3 bucket.
5. **Enter the required information** and execute the operation.
6. **Check the response** displayed by the dashboard.

## ⚠️ Important Notes

- Configure AWS CLI credentials before using the dashboard.
- Ensure your IAM identity has the required permissions for each operation.
- AWS resources are region-specific. Select the correct AWS region.
- Some operations may incur AWS charges.
- Never upload AWS credentials, private keys, or `.pem` files to GitHub.

---

<div align="center">

### ☁️ Built to simplify AWS resource management.

**Python • Streamlit • AWS CLI**

</div>