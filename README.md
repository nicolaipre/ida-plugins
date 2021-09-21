# IDA Plugins

## Plugins
- Copy hex without the junk: https://github.com/OALabs/hexcopy-ida
- Find diff in samples by copying idb from already reversed sample: https://www.zynamics.com/bindiff/manual/
- Run Yara rules over a binary: https://github.com/OALabs/findyara-ida


## Helpful tools
- Like CyberChef, but CLI and faster: https://github.com/binref/refinery


## Lumina
```
In a nutshell Lumina is the evolution of the good old FLIRT (Fast Library Identification and Recognition Technology) mechanism with some improvements:

- feature is embedded in IDA GUI : external tools to generate signatures are no longer needed
- end users can select which function they want to generate a signature for (one, all or user selection)
- unlike FLIRT, all signatures and metadata are stored in a single database to avoid individual loading of each signature file
- additional metadata is stored, instead of only function name and comment in the past.
```

### Usage
A public Lumina-like server is [Lumen](https://lumen.abda.nl/). You can also run your own private Lumen server: [(src)](https://github.com/naim94a/lumen). To use it, update your `cfg/ida.cfg`:
```
// Lumina related parameters
LUMINA_HOST = "lumen.abda.nl"; // Lumina server url (default = "lumina.hex-rays.com") // Warning: don't forget the semicolon or file parsing would fail
LUMINA_PORT = 1234

LUMINA_MIN_FUNC_SIZE = 32   // minimum function size (in bytes) to trigger a query (default = 32)
LUMINA_PORT = 4443          // TCP port (default = 443)
LUMINA_TLS= YES             // enable TLS (YES) or use plaintext tcp (NO)  (default = YES)
```

Alternatively, use this [offline Lumina server](https://github.com/synacktiv/lumina_server) by `Synacktiv`.
