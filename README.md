
---

## 🌀 Flooder — The Terminal Color Flood Game

**Flooder** is a minimalist color-flood puzzle game built in pure Python using `bext` for terminal graphics.
The goal? Turn the entire board into a single color before your moves run out.
It’s simple, recursive, and dangerously addictive.

### 🎮 Gameplay

You start from the **top-left tile (>)**, and each move floods connected tiles of the same color with your chosen color.
Choose wisely — every move counts.
If the entire board becomes one color before your moves run out, you win.
If not... well, you “loose motherflecker.” *(If you know, you know — Suits reference 😏)*

---

### 🧱 Features

* Randomly generated color board on each run
* Recursive flood-fill algorithm
* Clean ASCII-art borders and colored tiles
* Optional *"rage quit"* with `Q` 😆
* Runs directly in the terminal — no GUI required

---

### ⚙️ Requirements

Make sure you have Python 3 installed and the `bext` module:

```bash
pip install bext
```

---

### ▶️ How to Play

Clone the repo and run:

```bash
git clone https://github.com/<your-username>/flooder.git
cd flooder
python flooder.py
```

Then pick your colors using the letters shown:

| Color  | Input |
| :----- | :---- |
| Red    | R     |
| Green  | G     |
| Blue   | B     |
| Yellow | Y     |
| Cyan   | C     |
| Purple | P     |

Type `Q` to quit at any time.

---

### 🧠 How It Works

Flooder uses a **recursive flood-fill algorithm**, starting at `(0, 0)` and spreading through adjacent tiles that match the starting color.
Each move recolors connected tiles and updates the board visually.
It’s recursion doing what recursion does best — *taking over the world, one tile at a time.*

---

### 🏆 Winning Condition

You win if all tiles match one color before your `moves_left` hits zero.
You lose if you run out of moves. (Don’t take it personally. It’s the algorithm, not you.)

---

### 🧑‍💻 Author

**Daniel Adeoluwa Ademoye**
Passionate about computer science, cybersecurity, and building games that prove terminal apps can still be cool.

---

### 📜 License

MIT License — do whatever you want, just don’t flood my inbox 😎
