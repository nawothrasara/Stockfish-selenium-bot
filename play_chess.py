import time
import chess
import chess.engine
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

# TODO: Replace this path with the location where Stockfish is installed on your computer
STOCKFISH_PATH = r"path_to_your_stockfish/stockfish.exe"

print("[STATUS] Loading Stockfish Engine...")
try:
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    print("[SUCCESS] Stockfish Engine started successfully!")
except Exception as e:
    print("[ERROR] Please check the Stockfish path:", e)
    exit()

print("[STATUS] Launching Chrome Browser...")
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.chess.com/login")
    print("[SUCCESS] Chrome Browser opened successfully!")
except Exception as e:
    print("[ERROR] WebDriver error occurred:", e)
    exit()

print("\n" + "="*50)
print("Please log in to Chess.com in the browser and start a game.")
print("="*50)

# Wait for manual login and game start
input("Once the game has started and the opponent is found, click on the terminal and press Enter...")

# Initialize the chess board
board = chess.Board()

print("[STATUS] Auto-play bot started tracking the game...")

def play_move_on_board(driver, move):
    """Function to automatically click and make a move on Chess.com board"""
    move_str = move.uci() # e.g., "e2e4"
    from_square = move_str[:2] # e.g., "e2"
    to_square = move_str[2:4]   # e.g., "e4"
    
    try:
        # Chess.com uses square classes like 'square-e2', 'square-e4'
        from_element = driver.find_element(By.CSS_SELECTOR, f'.square-{from_square}')
        to_element = driver.find_element(By.CSS_SELECTOR, f'.square-{to_square}')
        
        # Click the 'from' square and then the 'to' square to move the piece
        actions = ActionChains(driver)
        actions.click(from_element).pause(0.2).click(to_element).perform()
        
    except Exception as e:
        print(f"[WARNING] Could not auto-click move {move_str}: {e}")

try:
    while not board.is_game_over():
        # Get the best move from Stockfish for the current board state
        result = engine.play(board, chess.engine.Limit(time=1.0))
        best_move = result.move
        
        print(f"🤖 Stockfish moving: {best_move}")
        
        # Perform the move automatically on the browser board
        play_move_on_board(driver, best_move)
        
        # Push the move to the internal board tracker
        board.push(best_move)
        
        # Wait a couple of seconds before the next turn
        time.sleep(2)
        
except KeyboardInterrupt:
    print("\n[INFO] Program stopped by user.")
finally:
    engine.quit()
    driver.quit()