# HTML Viewer EXE Repro Steps

This project packages the HTML viewer into a Windows `.exe` with `uv` and `PyInstaller`.

## 1. Install `uv`

Open PowerShell and run:

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

After it finishes, close and reopen PowerShell, then verify the install:

```powershell
uv --version
```

## 2. Go to the project folder

```powershell
cd ...
```

## 3. Install the project dependencies

This creates or updates the local environment from `pyproject.toml` and `uv.lock`:

```powershell
uv sync
```

## 4. Check that the launcher file is valid

```powershell
uv run python -m py_compile main.py
```

## 5. Build the EXE

Run PyInstaller and include the HTML file as bundled data:

```powershell
uv run pyinstaller --onefile --noconsole --add-data "html_viewer.html;." main.py
```

## 6. Start the app

The executable will be created in the `dist` folder:

```powershell
dist\main.exe
```

## Notes

- `--onefile` creates a single executable.
- `--noconsole` hides the terminal window for a cleaner GUI launch.
- `--add-data "html_viewer.html;."` makes sure the HTML file is available when the EXE runs.
