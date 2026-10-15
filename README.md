# Chess.com Automation Bot 🤖♟️

A Python-based automation tool that integrates the **Stockfish** chess engine with **Selenium WebDriver** to track and automatically play chess games on **Chess.com**.

---

## Features
- **Automated Browser Control**: Launches Chrome using Selenium and `webdriver-manager`.
- **Manual Login Support**: Allows safe manual login to avoid Google Sign-in blocks and Cloudflare bot detection.
- **Stockfish AI Integration**: Computes the best moves in real-time using the universal Stockfish UCI engine.
- **Auto-Play Capability**: Automatically performs moves on the Chess.com interactive board.

---

## Prerequisites

Make sure you have the following installed on your system:
- [Python (3.8 or higher)](https://www.python.org/)
- [Google Chrome](https://www.google.com/chrome/)
- [Stockfish Engine](https://stockfishchess.org/download/) (Download the universal Windows/Linux/Mac binary)

