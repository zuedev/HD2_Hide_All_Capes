# Helldivers 2: Hide All Capes Mod

A Blender-based mod for Helldivers 2 that hides all capes by collapsing their meshes to invisible points.

## Overview

This mod removes the visual appearance of all capes in Helldivers 2 by replacing each cape's 3D model with a collapsed mesh (a single invisible vertex). This is accomplished using Blender and the HD2SDK Community Edition plugin.

**Note:** This is a client-side visual mod. Other players will still see capes normally unless they also install this mod.

## Features

- Hides all capes in Helldivers 2
- Automated Python script for batch processing
- Easy-to-follow manual workflow
- Clean, non-destructive modding approach

## Prerequisites

Before you begin, ensure you have:

1. **Helldivers 2** installed on your system
2. **Blender 4.0 or higher** - [Download here](https://www.blender.org/download/)
3. **HD2SDK Community Edition Plugin** for Blender
4. **Principled Baker** and **Material Combiner** plugins for Blender
5. **Helldivers 2 Archive Labeling - Capes.csv** file (contains cape Archive IDs)

## Quick Start

### Option 1: Automated (Recommended)

1. Follow the [detailed guide](documentation.md) to set up Blender and HD2SDK
2. Create a `cape_ids.txt` file with all cape Archive IDs (one per line)
3. Open Blender and set up your workspace (load base archive, create new patch)
4. Open the Scripting tab and load `build.py`
5. Update the `CAPE_ID_FILE_PATH` variable to point to your `cape_ids.txt`
6. Run the script
7. Write the final patch file
8. Deploy to your Helldivers 2 mod directory

### Option 2: Manual

Follow the step-by-step instructions in [documentation.md](documentation.md) to process each cape manually.

## Files in This Repository

- **`build.py`** - Automated Blender Python script for batch processing all capes
- **`documentation.md`** - Complete step-by-step guide for creating the mod
- **`LICENSE`** - MIT License

## How It Works

The mod uses a technique called "mesh collapsing":

1. Load a cape's 3D model from the game files
2. Import the mesh into Blender
3. Select all vertices in the mesh
4. Merge all vertices to the center point
5. Save the collapsed mesh (now a single point) to a patch file
6. The game renders this single point, making the cape invisible

This process is repeated for every cape in the game.

## Installation

1. Follow the guide in [documentation.md](documentation.md) to create your patch file
2. Locate your Helldivers 2 mod directory (typically in the game installation folder)
3. Copy the generated `.patch_0` file (and any associated `.gpu_resources` or `.stream` files) to the mod directory
4. Launch Helldivers 2

## Troubleshooting

### Capes Still Visible
- Ensure all cape Archive IDs were processed
- Verify the patch file is in the correct directory
- Check game logs to confirm the patch loaded

### Blender Issues
- Save your patch frequently
- Process capes in smaller batches if Blender becomes slow
- Restart Blender if it freezes

### Script Errors
- Verify HD2SDK commands in `build.py` match your plugin version
- Right-click HD2SDK UI buttons and select "Copy Python Command" to get exact operator names
- Check the Blender System Console (Window > Toggle System Console) for detailed error messages

## Documentation

- **[Complete Modding Guide](documentation.md)** - Full walkthrough with screenshots and tips
- **[build.py](build.py)** - Well-documented automation script with inline comments

## Contributing

Contributions are welcome! Feel free to:

- Report issues
- Submit improvements to the documentation
- Update the `build.py` script for newer HD2SDK versions
- Share tips and tricks

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- HD2 Modding Community
- HD2SDK Community Edition developers
- Blender Foundation

## Disclaimer

This mod is for personal use only. Use at your own risk. Modding may violate the game's terms of service. The authors are not responsible for any consequences of using this mod.

---

**For detailed instructions, see [documentation.md](documentation.md)**
