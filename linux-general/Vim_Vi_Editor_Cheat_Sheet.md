# Core commands for opening, editing, saving, and exiting Vi/Vim. 

Essential navigation, editing, and saving commands for Vi and Vim.

## **Modes**
* **Normal Mode:** Default entry mode for navigation and commands. Press `Esc` to return here.
* **Insert Mode:** Used for typing text. Enter by pressing `i`, `a`, or `o`.
* **Command-Line Mode:** Used for saving, quitting, and searching. Enter by typing `:` while in Normal mode.

## **Navigation (Normal Mode)**
| Action | Key / Command |
| :--- | :--- |
| **Move Left / Down / Up / Right** | `h` / `j` / `k` / `l` |
| **Move to End of Word** | `e` |
| **Move to Beginning of Line** | `0` (Zero) |
| **Move to End of Line** | `$` |
| **Jump to Line Number** | `:[line_number]` or `[line_number]G` |
| **Jump to Top / Bottom of File** | `gg` / `G` |

## **Editing & Manipulation (Normal Mode)**
| Action | Key / Command |
| :--- | :--- |
| **Insert Text (Before Cursor)** | `i` |
| **Insert Text (After Cursor)** | `a` |
| **Open New Line Below** | `o` |
| **Delete / Cut Current Line** | `dd` |
| **Copy (Yank) Current Line** | `yy` |
| **Paste Copied Line Below** | `p` |
| **Undo Last Change** | `u` |
| **Redo Change** | `Ctrl + r` |

## **Search, Save, and Quit (Command-Line Mode)**
| Action | Command |
| :--- | :--- |
| **Search Forward for Text** | `/[search_term]` (Press `n` for next match, `N` for previous) |
| **Save (Write) Changes** | `:w` |
| **Quit Editor** | `:q` |
| **Save and Quit** | `:wq` or `ZZ` |
| **Force Quit (Discard Changes)** | `:q!` |
| **Show Line Numbers** | `:set nu` |
| **Hide Line Numbers** | `:set nonu` |
