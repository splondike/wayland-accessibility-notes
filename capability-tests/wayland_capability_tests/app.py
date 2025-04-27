import os
import sys
from typing import List

import typer
from wayland.parser import WaylandParser

from wayland_capability_tests import wayland_client


app = typer.Typer(no_args_is_help=True, pretty_exceptions_enable=False)


@app.command()
def test_pointer():
    client = wayland_client.WaylandClient(".")
    pointer = client.binding(
        "zwlr_virtual_pointer_manager_v1"
    ).create_virtual_pointer(client.binding("wl_seat"))
    pointer.motion_absolute(1, 50, 50, 100, 100)
    pointer.destroy()


@app.command()
def test_window():
    client = wayland_client.WaylandClient(".")
    with wayland_client.Window(client):
        import time
        time.sleep(2)


@app.command()
def rebuild_protocols_json(protocols_dirs: List[str]):
    """
    Parse the Wayland protocol definitions in protocols_dirs and outputs them as a JSON document suitable for usage by this library
    """

    parser = WaylandParser()

    for dir in protocols_dirs:
        if not os.path.exists(dir):
            raise RuntimeWarning(f"Input dir doesn't exist: {dir}")

        for root, _, files in os.walk(dir):
            for file in files:
                full_file = os.path.join(root, file)
                if file.endswith(".xml"):
                    parser.parse(full_file)

    duplicate = False
    for interface_name, definition in parser.interfaces.items():
        for category in ("events", "requests", "enums"):
            existing = set()
            for item in definition[category]:
                name = item["name"]
                if name in existing:
                    print(
                        f"Duplicate definition: {interface_name}.{category}.{name}",
                        file=sys.stderr
                    )
                    duplicate = True
                else:
                    existing.add(name)

    if duplicate:
        # Wayland protocol doesn't allow more than one thing with the same name
        # I think. Having duplicate definitions caused me a few hours of
        # debugging at one point, hence this check!
        print("Error: Duplicate definitions. You're probably including multiple files that define the same interface.", file=sys.stderr)
        sys.exit(1)

    sys.stdout.write(parser.to_json())
