#!/usr/bin/env python3
"""
Python Version Manager - TUI Interface
A beautiful terminal user interface for managing Python versions
"""

import platform
import sys
import asyncio
from typing import Optional

try:
    from textual.app import App, ComposeResult
    from textual.containers import Container, Horizontal, Vertical, ScrollableContainer
    from textual.widgets import Header, Footer, Static, Button, Label, ProgressBar, LoadingIndicator
    from textual.binding import Binding
    from textual.screen import Screen
    from textual import work
    from rich.text import Text
    from rich.panel import Panel
    from rich.table import Table
except ImportError:
    print("ERROR: TUI mode requires the 'textual' package.")
    print("Install it with: pip install textual")
    sys.exit(1)

# Import from main module
from python_version import (
    get_os_info,
    is_admin,
    check_python_version,
    get_latest_python_info_with_retry,
    update_python_windows,
    update_python_linux,
    update_python_macos,
    validate_version_string,
)


class VersionDisplay(Static):
    """Widget to display version comparison"""
    
    def __init__(self, local_ver: str = "...", latest_ver: str = "...", needs_update: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.local_ver = local_ver
        self.latest_ver = latest_ver
        self.needs_update = needs_update
    
    def compose(self) -> ComposeResult:
        yield Static(id="version-content")
    
    def on_mount(self) -> None:
        self.update_display()
    
    def update_display(self) -> None:
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Label", style="bold white")
        table.add_column("Value")
        
        table.add_row("Installed:", f"[bold cyan]{self.local_ver}[/bold cyan]")
        table.add_row("Latest:", f"[bold green]{self.latest_ver}[/bold green]")
        
        if self.needs_update:
            status = "[bold yellow]UPDATE AVAILABLE[/bold yellow]"
        elif self.latest_ver != "...":
            status = "[bold green]UP TO DATE[/bold green]"
        else:
            status = "[dim]Checking...[/dim]"
        
        table.add_row("Status:", status)
        
        self.query_one("#version-content", Static).update(table)
    
    def set_versions(self, local_ver: str, latest_ver: str, needs_update: bool) -> None:
        self.local_ver = local_ver
        self.latest_ver = latest_ver
        self.needs_update = needs_update
        self.update_display()


class SystemInfoDisplay(Static):
    """Widget to display system information"""
    
    def compose(self) -> ComposeResult:
        yield Static(id="sysinfo-content")
    
    def on_mount(self) -> None:
        self.update_display()
    
    def update_display(self) -> None:
        os_name, arch = get_os_info()
        
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Label", style="bold white")
        table.add_column("Value", style="cyan")
        
        table.add_row("OS:", os_name.upper())
        table.add_row("Arch:", arch)
        table.add_row("Executable:", sys.executable)
        table.add_row("Platform:", platform.platform())
        table.add_row("Elevated:", "Yes" if is_admin() else "No")
        
        self.query_one("#sysinfo-content", Static).update(table)


class StatusBar(Static):
    """Status bar for showing messages"""
    
    def __init__(self, **kwargs):
        super().__init__("", **kwargs)
        self.message = ""
    
    def set_message(self, message: str, style: str = "") -> None:
        self.message = message
        if style:
            self.update(f"[{style}]{message}[/{style}]")
        else:
            self.update(message)
    
    def clear(self) -> None:
        self.update("")


class MainScreen(Screen):
    """Main TUI screen"""
    
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("r", "refresh", "Refresh"),
        Binding("u", "update_python", "Update"),
        Binding("i", "show_info", "Info"),
        Binding("?", "help", "Help"),
    ]
    
    CSS = """
    MainScreen {
        layout: vertical;
    }
    
    #main-container {
        height: 100%;
        padding: 1 2;
    }
    
    #title-box {
        height: auto;
        margin-bottom: 1;
        text-align: center;
        padding: 1 2;
        background: $surface;
        border: double $primary;
        color: $text;
    }
    
    #content-area {
        height: 1fr;
        layout: horizontal;
    }
    
    #left-panel {
        width: 1fr;
        height: 100%;
        padding: 1 2;
        border: solid $primary;
        margin-right: 1;
        background: $surface;
    }
    
    #right-panel {
        width: 1fr;
        height: 100%;
        padding: 1 2;
        border: solid $primary;
        background: $surface;
    }
    
    .panel-title {
        text-style: bold;
        color: $text;
        margin-bottom: 1;
        text-align: center;
        background: $surface-darken-1;
        padding: 0 1;
        border-bottom: solid $primary;
    }
    
    #button-area {
        height: auto;
        margin-top: 1;
        layout: horizontal;
        align: center middle;
        padding: 1 0;
    }
    
    Button {
        margin: 0 2;
        min-width: 20;
    }
    
    #status-bar {
        height: 1;
        dock: bottom;
        padding: 0 2;
        background: $surface;
        border-top: solid $primary;
    }
    
    #loading {
        height: 3;
        align: center middle;
        display: none;
    }
    
    #loading.visible {
        display: block;
    }
    
    .update-available Button#update-btn {
        background: $success;
    }
    """
    
    def __init__(self):
        super().__init__()
        self.local_ver: str = "..."
        self.latest_ver: Optional[str] = None
        self.needs_update: bool = False
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        
        with Container(id="main-container"):
            yield Static(
                "[bold]PYTHON VERSION MANAGER[/bold]\n[dim]v1.2.3 | Side-by-side Installation[/dim]",
                id="title-box"
            )
            
            with Container(id="loading"):
                yield LoadingIndicator()
                yield Label("Checking for updates...")
            
            with Horizontal(id="content-area"):
                with Vertical(id="left-panel"):
                    yield Static("VERSION STATUS", classes="panel-title")
                    yield VersionDisplay(id="version-display")
                
                with Vertical(id="right-panel"):
                    yield Static("SYSTEM INFO", classes="panel-title")
                    yield SystemInfoDisplay(id="sysinfo-display")
            
            with Horizontal(id="button-area"):
                yield Button("Refresh", id="refresh-btn", variant="default")
                yield Button("Update Python", id="update-btn", variant="primary")
                yield Button("Quit", id="quit-btn", variant="error")
            
            yield StatusBar(id="status-bar")
        
        yield Footer()
    
    def on_mount(self) -> None:
        """Called when screen is mounted"""
        self.check_versions()
    
    @work(exclusive=True)
    async def check_versions(self) -> None:
        """Check Python versions in background"""
        loading = self.query_one("#loading")
        loading.add_class("visible")
        self.query_one("#status-bar", StatusBar).set_message("Checking for updates...", "dim")
        
        # Run version check
        try:
            local_ver, latest_ver, needs_update = await asyncio.to_thread(
                check_python_version, True  # silent=True
            )
            
            self.local_ver = local_ver
            self.latest_ver = latest_ver
            self.needs_update = needs_update
            
            # Update display
            version_display = self.query_one("#version-display", VersionDisplay)
            version_display.set_versions(
                local_ver,
                latest_ver or "Unknown",
                needs_update
            )
            
            if needs_update:
                self.query_one("#status-bar", StatusBar).set_message(
                    f"Update available: {local_ver} → {latest_ver}", "yellow"
                )
                self.add_class("update-available")
            else:
                self.query_one("#status-bar", StatusBar).set_message(
                    "You're running the latest version!", "green"
                )
                
        except Exception as e:
            self.query_one("#status-bar", StatusBar).set_message(
                f"Error checking versions: {e}", "red"
            )
        finally:
            loading.remove_class("visible")
    
    @work(exclusive=True)
    async def do_update(self) -> None:
        """Perform Python update in background"""
        if not self.latest_ver:
            self.query_one("#status-bar", StatusBar).set_message(
                "No version info available. Please refresh first.", "red"
            )
            return
        
        loading = self.query_one("#loading")
        loading.add_class("visible")
        
        status_bar = self.query_one("#status-bar", StatusBar)
        status_bar.set_message(f"Installing Python {self.latest_ver}...", "yellow")
        
        try:
            os_name, _ = get_os_info()
            
            # Run update based on OS
            if os_name == 'windows':
                success = await asyncio.to_thread(update_python_windows, self.latest_ver)
            elif os_name == 'linux':
                success = await asyncio.to_thread(update_python_linux, self.latest_ver)
            elif os_name == 'darwin':
                success = await asyncio.to_thread(update_python_macos, self.latest_ver)
            else:
                status_bar.set_message(f"Unsupported OS: {os_name}", "red")
                return
            
            if success:
                status_bar.set_message(
                    f"Python {self.latest_ver} installed successfully", "green"
                )
                # Show usage instructions
                self.app.push_screen(SuccessScreen(self.latest_ver, os_name))
            else:
                status_bar.set_message(
                    "Installation encountered issues. Check terminal output.", "yellow"
                )
                
        except Exception as e:
            status_bar.set_message(f"Error during update: {e}", "red")
        finally:
            loading.remove_class("visible")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses"""
        if event.button.id == "refresh-btn":
            self.action_refresh()
        elif event.button.id == "update-btn":
            self.action_update_python()
        elif event.button.id == "quit-btn":
            self.action_quit()
    
    def action_refresh(self) -> None:
        """Refresh version information"""
        self.check_versions()
    
    def action_update_python(self) -> None:
        """Start Python update"""
        if not self.needs_update:
            self.query_one("#status-bar", StatusBar).set_message(
                "Already up to date! No update needed.", "green"
            )
            return
        self.do_update()
    
    def action_quit(self) -> None:
        """Quit the application"""
        self.app.exit()
    
    def action_help(self) -> None:
        """Show help"""
        self.app.push_screen(HelpScreen())


class SuccessScreen(Screen):
    """Screen shown after successful installation"""
    
    BINDINGS = [
        Binding("escape", "go_back", "Back"),
        Binding("q", "quit", "Quit"),
    ]
    
    CSS = """
    SuccessScreen {
        align: center middle;
    }
    
    #success-container {
        width: 70;
        height: auto;
        padding: 2 3;
        border: double $success;
        background: $surface;
    }
    
    #success-title {
        text-align: center;
        text-style: bold;
        color: $success;
        margin-bottom: 1;
        padding: 1;
        background: $surface-darken-1;
        border-bottom: solid $success;
    }
    
    #instructions {
        margin: 1 0;
    }
    
    #back-btn {
        margin-top: 1;
        width: 100%;
    }
    """
    
    def __init__(self, version: str, os_name: str):
        super().__init__()
        self.version = version
        self.os_name = os_name
    
    def compose(self) -> ComposeResult:
        # Extract major.minor
        parts = self.version.split('.')
        major_minor = f"{parts[0]}.{parts[1]}" if len(parts) >= 2 else self.version
        
        with Container(id="success-container"):
            yield Static("INSTALLATION COMPLETE", id="success-title")
            yield Static(f"Python {self.version} has been installed successfully.")
            
            # OS-specific instructions
            if self.os_name in ('linux', 'darwin'):
                instructions = f"""
[bold white]Usage Instructions:[/bold white]

[cyan]Run scripts:[/cyan]
  $ python{major_minor} your_script.py

[cyan]Create virtual environment:[/cyan]
  $ python{major_minor} -m venv myproject
  $ source myproject/bin/activate

[cyan]Verify installation:[/cyan]
  $ python{major_minor} --version
"""
            else:  # Windows
                instructions = f"""
[bold white]Usage Instructions:[/bold white]

[cyan]Use Python Launcher:[/cyan]
  > py -{major_minor} your_script.py

[cyan]List all versions:[/cyan]
  > py --list

[cyan]Create virtual environment:[/cyan]
  > py -{major_minor} -m venv myproject
  > myproject\\Scripts\\activate
"""
            
            yield Static(instructions, id="instructions")
            yield Static("[dim]Previous Python version remains as system default.[/dim]")
            yield Button("Back", id="back-btn")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.action_go_back()
    
    def action_go_back(self) -> None:
        self.app.pop_screen()
    
    def action_quit(self) -> None:
        self.app.exit()


class HelpScreen(Screen):
    """Help screen with keyboard shortcuts"""
    
    BINDINGS = [
        Binding("escape", "go_back", "Back"),
        Binding("q", "go_back", "Back"),
    ]
    
    CSS = """
    HelpScreen {
        align: center middle;
    }
    
    #help-container {
        width: 60;
        height: auto;
        padding: 2 3;
        border: double $primary;
        background: $surface;
    }
    
    #help-title {
        text-align: center;
        text-style: bold;
        margin-bottom: 1;
        color: $text;
        padding: 1;
        background: $surface-darken-1;
        border-bottom: solid $primary;
    }
    
    #close-btn {
        width: 100%;
        margin-top: 1;
    }
    """
    
    def compose(self) -> ComposeResult:
        with Container(id="help-container"):
            yield Static("KEYBOARD SHORTCUTS", id="help-title")
            
            help_text = """
[bold cyan]Navigation[/bold cyan]
  [bold white]R[/bold white]  Refresh version info
  [bold white]U[/bold white]  Update Python
  [bold white]I[/bold white]  Show system info
  [bold white]?[/bold white]  Show this help
  [bold white]Q[/bold white]  Quit application

[bold cyan]CLI Commands[/bold cyan]
  pyvm check   Check version
  pyvm update  Update Python
  pyvm info    System info
  pyvm tui     This interface

[dim]Press Escape or Q to close[/dim]
"""
            yield Static(help_text)
            yield Button("Close", id="close-btn")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.action_go_back()
    
    def action_go_back(self) -> None:
        self.app.pop_screen()


class PyvmTUI(App):
    """Main TUI Application"""
    
    TITLE = "Python Version Manager"
    SUB_TITLE = "pyvm-updater"
    
    CSS = """
    Screen {
        background: $background;
    }
    """
    
    SCREENS = {
        "main": MainScreen,
    }
    
    def on_mount(self) -> None:
        self.push_screen("main")


def run_tui():
    """Entry point for TUI mode"""
    app = PyvmTUI()
    app.run()


if __name__ == "__main__":
    run_tui()
