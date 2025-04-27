Implementations of capabilities needed by different accessibility technologies.

# Setup

The Wayland library we're using first needs to parse the XML files containing Wayland protocol definitions into a single `protocols.json` file. You can do that as follows:

```
poetry run wayland-capability-tests rebuild-protocols-json /usr/share/wayland/ ~/Desktop/scratch/wayland-explorer/protocols/wayland/stable/ ~/Desktop/scratch/wayland-explorer/protocols/wlr/ > protocols.json
```

To get a copy of the protocol XML files you can clone the [wayland.app repository](https://github.com/vially/wayland-explorer/tree/main/protocols).

# Debugging

The Wayland library we're using accepts the `WAYLAND_DEBUG=1` env var to print more output.

If that's not enough you can also make use of various [helper applications](https://wayland.freedesktop.org/extras.html) that print out all events received and requests sent.

I've been using [wlanalyzer](https://github.com/blessed/wlanalyzer), which was a little annoying to build, but supports Python unlike `wayland-tracer`.
