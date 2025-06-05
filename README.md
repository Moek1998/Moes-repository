# Lobe Chat Setup

This is a deployment of [LobeHub/lobe-chat](https://github.com/lobehub/lobe-chat), an open-source, modern-design AI chat framework.

## Features

* Modern UI design
* Multiple AI providers (OpenAI, Claude, Gemini, Ollama, DeepSeek, Qwen)
* Knowledge Base (upload files / knowledge management / RAG)
* Multi-modal support with plugins and artifacts
* Thinking capabilities

## Quick Start

### Prerequisites

- Docker and Docker Compose installed
- An OpenAI API key (optional but recommended)

### Setup Instructions

1. Navigate to the `docker-data` directory:
   ```
   cd docker-data
   ```

2. Run the setup script to create the required environment file:
   ```
   ./setup.ps1
   ```

3. Edit the `.env` file to customize your configuration:
   - Set a secure PostgreSQL password
   - Set secure MinIO credentials
   - Add your OpenAI API key (optional)

4. Start the Lobe Chat services:
   ```
   docker-compose up -d
   ```

5. Access Lobe Chat at: http://localhost:3210

6. Initial login credentials:
   - Username: admin
   - Password: 123

## Configuration Options

The `.env` file contains several configuration options:

- `LOBE_PORT`: The port to access Lobe Chat (default: 3210)
- `POSTGRES_PASSWORD`: Password for the PostgreSQL database
- `MINIO_ROOT_USER`/`MINIO_ROOT_PASSWORD`: Credentials for the MinIO service
- `OPENAI_API_KEY`: Your OpenAI API key for AI services

## Additional Resources

- [Official Documentation](https://lobehub.com/docs)
- [GitHub Repository](https://github.com/lobehub/lobe-chat)
- [Discord Community](https://discord.gg/lobehub)

## License

This project is Apache 2.0 licensed, following the original license of LobeHub/lobe-chat.

# Amazon Bedrock Setup for App Studio

This repository contains a PowerShell script to automate the setup of Amazon Bedrock for use with App Studio, following AWS IAM best practices.

## Quick Start Guide

1. Download the script files from this repository
2. Open PowerShell as administrator
3. Navigate to the directory containing the script
4. Run the script with your App Studio Account ID and Instance ID:

```powershell
.\setup-bedrock-for-appstudio.ps1 -AppStudioAccountId "111122223333" -AppStudioInstanceId "11111111-2222-3333-4444-555555555555"
```

## Prerequisites

Before running the script, you need:

1. AWS CLI installed and configured with admin credentials
2. PowerShell 5.1 or higher
3. Your App Studio account ID and instance ID (found in App Studio's Account Settings)

## Troubleshooting

If you encounter the error:
```
The term '.\setup-bedrock-for-appstudio.ps1' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

This means PowerShell cannot find the script file. Make sure:

1. You're in the correct directory where the script is located
2. The script file exists and has the correct name
3. Try using the full path to the script:
   ```powershell
   & "C:\Users\YourUsername\path\to\setup-bedrock-for-appstudio.ps1" -AppStudioAccountId "111122223333" -AppStudioInstanceId "11111111-2222-3333-4444-555555555555"
   ```

## Optional Parameters

- `-PolicyName`: Custom name for the IAM policy (default: "BedrockAccessForAppStudio")
- `-RoleName`: Custom name for the IAM role (default: "AppStudioBedrockAccessRole")
- `-Region`: AWS region where your Bedrock resources are located (default: "us-east-1")
- `-AllowModelSubscriptions`: Include this switch to add permissions for subscribing to third-party models
- `-AllowProvisioning`: Include this switch to add permissions for managing provisioned model throughput

## After Running the Script

After successfully running the script:

1. Enable the Amazon Bedrock models you want to use in the AWS console
2. Create the Amazon Bedrock connector in App Studio using the role ARN provided by the script output 