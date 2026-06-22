from pathlib import Path
import sys
import webbrowser


def get_viewer_path() -> Path:
    if getattr(sys, "frozen", False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent
    return base_path / "html_viewer.html"


def main() -> None:
    viewer_path = get_viewer_path()
    if not viewer_path.exists():
        raise FileNotFoundError(f"Viewer file not found: {viewer_path}")

    webbrowser.open_new_tab(viewer_path.as_uri())
    print(f"Opened viewer: {viewer_path}")


if __name__ == "__main__":
    main()
