# Helldivers 2: Hide All Capes Mod Guide

This guide will walk you through creating a mod that hides all capes in Helldivers 2 by replacing each cape's 3D model with a collapsed mesh (a single invisible point).

## Prerequisites

Before starting, ensure you have:

1. **Helldivers 2** installed on your system
2. **Blender 4.0 or higher**
3. **HD2SDK Community Edition Plugin** for Blender
4. **Principled Baker** and **Material Combiner** plugins for Blender
5. The **Helldivers 2 Archive Labeling - Capes.csv** file (contains cape Archive IDs)

## Step 1: Install and Configure Blender

### Install Blender Plugins

1. Download the required plugins:
   - HD2SDK Community Edition Plugin
   - Principled Baker
   - Material Combiner

2. Install plugins in Blender:
   - Open Blender and navigate to `Edit > Preferences`
   - Go to the **Add-ons** tab
   - Click **Install** and select each downloaded `.zip` file
   - Enable each plugin by checking the box next to its name
   - Click **Save Preferences**

### Configure HD2SDK Workspace

1. In Blender's 3D viewport, press `N` to open the sidebar
2. Select the **Modding** tab
3. In the **Settings** section:
   - Set the filepath to your Helldivers 2 `Data` folder
   - Click the star icon to load the Base Game Archive
   - Click **New Patch** to create a new patch file

## Step 2: Hiding a Single Cape (Practice Run)

Before processing all capes, it's helpful to understand the workflow by hiding a single cape first.

### Find the Cape Archive ID

1. Open the `Helldivers 2 Archive Labeling - Capes.csv` file
2. Find a cape you want to hide (e.g., "Foe Smasher" has Archive ID `0fe88d9b08f6fe80`)
3. Copy the Archive ID for the next step

### Import the Cape Model

1. In the Blender **Modding** panel (press `N` if not visible)
2. Paste the Archive ID into the archive loader
3. Click to load the archive
4. Navigate to the **Mesh** section
5. Select all meshes listed
6. Click **Import** to bring the cape model into your viewport

### Collapse the Mesh to Make It Invisible

1. Select the imported cape model in the viewport
2. Press `Tab` to enter **Edit Mode**
3. Press `A` to select all vertices
4. Press `M` to open the **Merge** menu
5. Select **At Center** (this is the fastest option)
6. Press `Tab` again to return to **Object Mode**

The mesh is now collapsed to a single point, making it invisible in-game.

### Save the Modified Mesh

1. With the collapsed mesh still selected, go to the **Modding** panel
2. In the **Mesh** section, find the **Write** or **Save** option
3. Save the mesh to your patch file
4. The original cape model will now be replaced with your invisible version in the patch

## Step 3: Process All Capes

Now that you understand the workflow, repeat the process for every cape in the game.

### Workflow for Each Cape

For each Archive ID in the `Helldivers 2 Archive Labeling - Capes.csv` file:

1. Load the cape's archive using its Archive ID
2. Import all meshes from the archive
3. Enter Edit Mode (`Tab`)
4. Select all vertices (`A`)
5. Merge at center (`M` → **At Center**)
6. Exit Edit Mode (`Tab`)
7. Save the modified mesh to your patch
8. Clear the scene and move to the next cape

### Tips for Efficiency

- **Keep Blender open** throughout the entire process
- **Don't close your patch** until all capes are processed
- **Work methodically** through the CSV file, checking off each completed cape
- **Save frequently** to avoid losing progress
- Consider creating a **checklist** of Archive IDs to track your progress

## Step 4: Finalize and Export the Patch

Once all cape meshes have been collapsed and saved:

### Write the Patch File

1. In the Blender **Modding** panel, locate the **Write Patch** section
2. Click **Write Patch** to compile all changes
3. This creates a `.patch_0` file containing all your modifications

### Deploy the Mod

1. Locate your Helldivers 2 mod directory:
   - This is typically in your game's installation folder under a `mods` or `patch` directory
   - Consult HD2 modding documentation for the exact path

2. Copy the generated `.patch_0` file (and any associated files like `.gpu_resources` or `.stream`) to the mod directory

3. Launch Helldivers 2 to test your mod

## Troubleshooting

### Capes Still Visible

- Ensure all cape Archive IDs from the CSV were processed
- Verify the patch file is in the correct directory
- Check that the patch file loaded correctly (consult game logs)

### Blender Crashes or Freezes

- Save your patch frequently
- Process capes in smaller batches
- Restart Blender if it becomes slow

### Missing Archive IDs

- Ensure you have the complete and up-to-date Capes CSV file
- Some capes may be added in game updates and require new Archive IDs

## Additional Resources

- **HD2 Modding Documentation**: Official modding guide for Helldivers 2
- **HD2SDK Community Edition**: Plugin documentation and support
- **Helldivers 2 Modding Community**: Forums and Discord for help and updates

---

**Note**: This mod only hides capes visually on your client. Other players will still see capes normally unless they also use this mod.
