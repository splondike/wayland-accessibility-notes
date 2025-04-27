See here for repos containing the XML protocol files:

https://github.com/vially/wayland-explorer/blob/main/.gitmodules

---

Implementations of capabilities needed by different window managers.

# Setup

The Wayland library we're using first needs to parse the XML files containing Wayland protocol definitions into a single `protocols.json` file. You can do that as follows:

```
poetry run wayland-capability-tests rebuild-protocols-json /usr/share/wayland/ ~/Desktop/scratch/wayland-explorer/protocols/wayland/stable/ ~/Desktop/scratch/wayland-explorer/protocols/wlr/ > protocols.json
```
