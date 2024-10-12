## README for Let-It-Be-Compound
# Sci-Topia's Original Project
### Project Overview

This project is an **interactive periodic table** that allows users to explore elements interactively, form chemical compounds using selected elements, and view educational resources such as videos and images related to the periodic table.

### Features
1. **Interactive Periodic Table**:
   - Elements can be selected to view their details on Wikipedia.
   - Users can choose multiple elements (up to four) to form compounds.
   - The application displays the result of synthesized compounds using a **Python-based WebSocket** backend.

2. **Python WebSocket Server**:
   - The server connects to Google Generative AI (`gemini-1.5-flash`) to generate information about synthesized compounds based on user input.
   - AI responses are embedded within an HTML `<div>` element with formatted text.

3. **Resource Pages**:
   - **Video**: Watch an educational video, *The Periodic Table Song*.
   - **Image**: Explore or download a **Periodic Table Chart** in PDF.
   - **Documentation**: Read about the history of the periodic table.
   - **Interactive Links**: Links to additional web resources and the about page.

### Installation and Setup

#### Prerequisites
- **Python 3.x** and `pip`
- WebSocket and Google Generative AI dependencies:
  ```bash
  pip install websockets google-generativeai
  ```
- **Web Server**: Any static file server to host the HTML and CSS files locally or online.

#### Google Generative AI Setup
1. Obtain an API key from Google Generative AI and replace it inside the `ptry.py` file:
   ```python
   genai.configure(api_key="YOUR_API_KEY")
   ```

#### File Structure
```
/PeriodicTableProject
│
├── ptry.py           # Python WebSocket server code
├── Periodic_table.html  # Main interactive periodic table page
├── rp.html           # Resource page with videos and documents
├── style.css         # Styling for the web pages
└── assets/           # Folder containing media files (videos, PDFs, images)
```

#### Running the WebSocket Server
1. Start the Python WebSocket server:
   ```bash
   python ptry.py
   ```
2. Open **`Periodic_table.html`** in your browser.

### Usage
- **Explore Elements**: Click on any element to open its Wikipedia page.
- **Form Compounds**:
   - Hold `CTRL` and click up to four elements.
   - Press `CTRL + Enter` to generate the compound.
   - The backend AI will provide details about possible compounds.
  
- **Resource Links**: Explore the video, periodic table image, and document links provided.

### Example Code Snippets

**WebSocket Python Handler (from `ptry.py`):**
```python
async def handle_websocket(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        response = chat_session.send_message(message)
        await websocket.send(response.text)
```

**HTML Table Example (from `Periodic_table.html`):**
```html
<table class="cont">
    <tr>
        <td class="color1 el-name" title="Hydrogen">1<br>H</td>
        <td class="color9 el-name" title="Helium">2<br>He</td>
    </tr>
</table>
```

### Styling (from `style.css`)
- Custom colors are used to visually distinguish different element groups:
  ```css
  .color1 { background-color: #00b6bc; }
  .color5 { background-color: #f53951; }
  td:hover { filter: brightness(200%); }
  ```

### Contributions
Feel free to fork this repository and submit pull requests to enhance functionality.

### License
This project is open-source and distributed under the MIT License.
