# Langfuse Observability Plugin

This plugin ships bundled with Tiyazo but is **opt-in** — it only loads when
you explicitly enable it.

## Enable

Pick one:

```bash
# Interactive: walks you through credentials + SDK install + enable
tiyazo tools  # → Langfuse Observability

# Manual
pip install langfuse
tiyazo plugins enable observability/langfuse
```

## Required credentials

Set these in `~/.tiyazo/.env` (or via `tiyazo tools`):

```bash
TIYAZO_LANGFUSE_PUBLIC_KEY=pk-lf-...
TIYAZO_LANGFUSE_SECRET_KEY=sk-lf-...
TIYAZO_LANGFUSE_BASE_URL=https://cloud.langfuse.com   # or your self-hosted URL
```

Without the SDK or credentials the hooks no-op silently — the plugin fails
open.

## Verify

```bash
tiyazo plugins list                 # observability/langfuse should show "enabled"
tiyazo chat -q "hello"              # then check Langfuse for a "Tiyazo turn" trace
```

## Optional tuning

```bash
TIYAZO_LANGFUSE_ENV=production       # environment tag
TIYAZO_LANGFUSE_RELEASE=v1.0.0       # release tag
TIYAZO_LANGFUSE_SAMPLE_RATE=0.5      # sample 50% of traces
TIYAZO_LANGFUSE_MAX_CHARS=12000      # max chars per field (default: 12000)
TIYAZO_LANGFUSE_DEBUG=true           # verbose plugin logging
```

## Disable

```bash
tiyazo plugins disable observability/langfuse
```
