# Recover-TG-Account-


### Set Environment Variables

```API_ID```= api id

```API_HASH``` api hash

```SESSION``` old string session (string session of the account you want to log in to) 

---

📌 Telegram Userbot with String Session and OTP Forwarding

This system allows you to recover and manage your Telegram account using a string session and a userbot.
It is especially useful when you don’t have access to your original phone number but still want to log in again.


---

## 🔹 How It Works

1. Login with String Session

First, you create and save a string session using Pyrogram or Telethon.

The string session acts as a permanent login, so the bot can stay logged in without needing OTP each time.



2. Userbot Runs on Your Account

A userbot (a Python script using the string session) keeps running and listens to incoming messages on your Telegram account.



3. Phone Number Login Attempt

When you try to log in to the same account using your phone number on another device, Telegram will send an OTP/login code to your existing sessions.



4. OTP Extraction by Userbot

The running userbot automatically detects and extracts the OTP (5-digit login code) from the incoming Telegram message.



5. OTP Delivery

The extracted OTP can then be:

Displayed in the console

Sent to your private chat

Or forwarded to a specific group/channel in a safe format




6. Account Recovery

You can then use this OTP on the new device to successfully log in.





---

🔹 Benefits

No SIM required: As long as the string session is valid, you don’t need your original SIM card for OTP.

Automation: OTPs are automatically captured and delivered by the userbot.

Convenience: Makes account recovery easy if you forget or lose access to your phone number.



---

🔹 Security Notes

A string session grants full access to your account.

Never share your string session or OTP with anyone.

Keep the userbot running only on your own secure machine (PC, VPS, or server you trust).

If you log out from all devices in Telegram, the string session will expire and you will need a new OTP to log in again.


