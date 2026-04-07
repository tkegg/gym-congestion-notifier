# 🏋️‍♂️ Gym Congestion Notifier

## 📝 Overview
A fully automated, serverless web scraping and notification pipeline. This application monitors the real-time congestion status of my "Local Gym" and sends a push notification to my smartphone via the LINE Messaging API when the gym is relatively empty.

I built this project to solve a personal pain point (avoiding crowded gym hours) while practicing modern automation, dynamic web scraping, and secure API integration.

## 🏗️ Architecture & Workflow
1. **Scheduled Trigger:** GitHub Actions (Cron) runs the script periodically without the need for a local server.
2. **Dynamic Scraping:** Python and Playwright launch a headless browser to retrieve real-time occupancy data from the gym's dynamic website.
3. **Data Processing:** The script evaluates the fetched data against predefined congestion thresholds.
4. **Push Notification:** If the gym is uncrowded, a POST request is sent to the `https://api.line.me/v2/bot/message/push` endpoint to alert my personal LINE account.

## 💻 Tech Stack
- **Language:** Python
- **Web Scraping:** Playwright (Chosen over traditional libraries to reliably handle JavaScript-rendered dynamic content)
- **CI/CD & Automation:** GitHub Actions
- **API Integration:** LINE Messaging API

## 🔒 Security & Best Practices
- **No Hardcoded Credentials:** All sensitive data, including the LINE Channel Access Token and User ID, are strictly excluded from the source code.
- **GitHub Secrets Integration:** Environment variables are securely injected during the GitHub Actions workflow using `${{ secrets.LINE_TOKEN }}`.
- **Clean Git History:** The repository is managed with a strict `.gitignore` to prevent accidental credential leaks.
