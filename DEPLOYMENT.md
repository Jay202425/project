# Streamlit Cloud Deployment Guide

This guide will help you deploy your OpenAI chatbot to Streamlit Cloud.

## Prerequisites

- GitHub account
- OpenAI API key
- Streamlit Cloud account (free at https://streamlit.io/cloud)

## Deployment Steps

### 1. Push Code to GitHub

Your code is already in a GitHub repository. Make sure all changes are pushed.

### 2. Sign in to Streamlit Cloud

1. Go to https://streamlit.io/cloud
2. Sign in with your GitHub account
3. Authorize Streamlit to access your repositories

### 3. Deploy Your App

1. Click **"New app"** button
2. Select your repository: `Jay202425/project`
3. Select branch: `copilot/create-open-ai-bot` (or your main branch)
4. Set main file path: `app.py`
5. Click **"Advanced settings"** (optional)
6. Click **"Deploy!"**

### 4. Configure Secrets (IMPORTANT!)

Before your app will work, you need to add your OpenAI API key:

1. In your deployed app, click the menu (⋮) in the top right
2. Select **"Settings"**
3. Go to the **"Secrets"** tab
4. Add your API key in TOML format:

```toml
OPENAI_API_KEY = "sk-proj-your-actual-api-key-here"
```

5. Click **"Save"**
6. The app will automatically restart with the new secrets

### 5. Access Your App

Your app will be available at a URL like:
```
https://your-app-name.streamlit.app
```

## Troubleshooting

### App Shows "OPENAI_API_KEY not found"

- Make sure you added the API key to Streamlit secrets (Step 4)
- Check that the format is correct (TOML format with quotes)
- Wait a few seconds for the app to restart after saving secrets

### App Won't Start

- Check the logs in Streamlit Cloud dashboard
- Ensure all dependencies in `requirements.txt` are compatible
- Verify your OpenAI API key is valid

### App is Slow

- Free Streamlit Cloud apps sleep after inactivity
- First request may be slow while the app wakes up
- Upgrade to a paid plan for always-on apps

## Features

Your deployed app will have:

- ✅ Real-time streaming responses
- ✅ Conversation history
- ✅ Modern chat interface
- ✅ Mobile-responsive design
- ✅ Secure API key management

## Updating Your App

To update your deployed app:

1. Make changes to your code locally
2. Commit and push to GitHub
3. Streamlit Cloud will automatically detect changes and redeploy

## Cost Considerations

- Streamlit Cloud free tier includes 1 app
- OpenAI API charges apply based on usage
- Monitor your OpenAI API usage at https://platform.openai.com/usage

## Support

- Streamlit Documentation: https://docs.streamlit.io
- OpenAI API Documentation: https://platform.openai.com/docs
- Repository Issues: Create an issue in your GitHub repository
