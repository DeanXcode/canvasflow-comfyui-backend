# CanvasFlow ComfyUI Backend

This repository contains a lightweight ComfyUI backend package for CanvasFlow.

Included:

- ComfyUI source code.
- Required `custom_nodes/` used by the local CanvasFlow setup.
- CanvasFlow compatibility nodes.

Excluded:

- Model weights under `models/`.
- Runtime input/output/temp files.
- Local user database and logs.
- Python virtual environments.

## Model Files

Download model files separately and place them in the matching ComfyUI folders.

Typical folders:

- `models/diffusion_models/`
- `models/text_encoders/`
- `models/vae/`
- `models/checkpoints/`
- `models/loras/`

This keeps the GitHub repository small while preserving the backend code and custom node setup.

## Start

Install dependencies in your preferred Python environment, then run:

```powershell
python main.py --listen 127.0.0.1 --port 8188
```

CanvasFlow can then connect to:

```text
http://127.0.0.1:8188
```
