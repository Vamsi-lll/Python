# Infinite Scroll with PyAutoGUI 🐾

So I randomly stumbled upon [longdogechallenge.com](https://longdogechallenge.com/)—a website where you just keep scrolling forever to see more doges.  
At some point I thought: *“Why am I working so hard with my finger on the mouse wheel? Let Python do the scrolling for me!”*  

And here we are. This little script uses **PyAutoGUI** to take over the scrolling job. Sit back, relax, and let your computer do the infinite scroll marathon.

---

## What this does
- Opens up the browser window (you do that part).
- Waits 5 seconds so you can get ready.
- Scrolls down forever… until you stop it.
- Basically, it’s like hiring a tiny robot intern whose only job is to scroll.

---

## Requirements
- Python 3.x
- PyAutoGUI (`pip install pyautogui`)

---

## How to use
1. Go to [longdogechallenge.com](https://longdogechallenge.com/) in your browser.
2. Run the script:
   ```bash
   python infinite_scroll.py
