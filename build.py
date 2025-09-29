"""
Helldivers 2: Cape Hiding Automation Script
============================================

This Blender Python script automates the process of hiding all capes in Helldivers 2
by collapsing each cape mesh to a single invisible point.

Prerequisites:
--------------
1. Blender 4.0+ with HD2SDK Community Edition plugin installed and configured
2. Helldivers 2 base game archive loaded in Blender
3. A new, empty patch created in Blender (via HD2SDK "New Patch" button)
4. A text file containing cape Archive IDs (one per line)

How to Use:
-----------
1. Prepare Cape ID File:
   - Create a plain text file (e.g., cape_ids.txt)
   - Copy all Archive ID values from "Helldivers 2 Archive Labeling - Capes.csv"
   - Paste them into the text file, one ID per line
   - Save the file

2. Configure Blender Workspace:
   - Launch Blender
   - Press 'N' to open the sidebar and select the "Modding" tab
   - Set the filepath to your Helldivers 2 Data folder
   - Click the star icon to load the base game archive
   - Click "New Patch" to create an empty patch

3. Load and Configure Script:
   - Switch to the "Scripting" workspace tab in Blender
   - Click "+ New" to create a new text block
   - Paste this entire script into the editor
   - Update CAPE_ID_FILE_PATH below to point to your cape_ids.txt file
   - Use absolute paths or paths relative to your Blender working directory

4. Run the Script:
   - Click the "Run Script" button (play icon) in the text editor
   - Monitor progress in the Blender System Console (Window > Toggle System Console)
   - The script will process each cape automatically

5. Finalize the Mod:
   - After the script completes, go to the "Modding" panel
   - Click "Write Patch" to save the final .patch_0 file
   - Deploy the patch file to your Helldivers 2 mod directory

Important Notes:
----------------
- This script uses placeholder SDK commands (bpy.ops.hd2.*) that may need adjustment
- Consult HD2SDK documentation for exact operator names
- You can copy exact Python commands by right-clicking SDK buttons and selecting
  "Copy Python Command"
- The script includes error handling to prevent Blender crashes
- Each cape is cleaned from the scene after processing to save memory

Expected Behavior:
------------------
- For each cape Archive ID:
  1. Loads the cape's archive
  2. Imports all meshes from that archive
  3. Collapses each mesh to a single point (merges all vertices at center)
  4. Saves the collapsed mesh to your patch
  5. Removes the processed objects from the scene
  6. Moves to the next cape

Troubleshooting:
----------------
- If SDK commands fail, check HD2SDK documentation for correct operator names
- If Blender crashes, process capes in smaller batches
- If imports fail, ensure the base archive is properly loaded
- Check the System Console for detailed error messages
"""

import bpy
import os

# ============================================================================
# CONFIGURATION
# ============================================================================

# Path to the text file containing cape Archive IDs (one per line)
# Update this to point to your cape_ids.txt file
# Examples:
#   - Relative: "./cape_ids.txt"
#   - Absolute: "C:/Users/YourName/Documents/cape_ids.txt"
CAPE_ID_FILE_PATH = "./cape_ids.txt"

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_cape_ids(filepath):
    """
    Reads cape archive IDs from a text file.

    Args:
        filepath (str): Path to the text file containing Archive IDs (one per line)

    Returns:
        list: List of cape Archive ID strings, or empty list if file not found

    Example file format:
        0fe88d9b08f6fe80
        1a23bc45de67fa89
        2b34cd56ef78ab90
    """
    if not os.path.exists(filepath):
        print(f"Error: The file was not found at '{filepath}'")
        print(f"Please check the CAPE_ID_FILE_PATH variable and ensure the file exists.")
        return []

    with open(filepath, 'r') as f:
        # Read each line, strip whitespace, and filter out empty lines
        ids = [line.strip() for line in f if line.strip()]

    print(f"Successfully loaded {len(ids)} cape IDs from '{filepath}'")
    return ids

def process_cape(archive_id):
    """
    Processes a single cape by loading, collapsing, and saving its mesh.

    This function automates the manual workflow of:
    1. Loading a cape's archive from the game files
    2. Importing all meshes from that archive
    3. Collapsing each mesh to a single point (making it invisible)
    4. Saving the modified mesh to the active patch
    5. Cleaning up the scene to free memory

    Args:
        archive_id (str): The Archive ID of the cape to process (e.g., "0fe88d9b08f6fe80")

    Returns:
        None

    Raises:
        Exception: If any step fails, the error is caught and logged, and cleanup is attempted

    Note:
        The bpy.ops.hd2.* commands are placeholders and may need adjustment based on
        your HD2SDK version. To find the correct commands:
        - Right-click buttons in the HD2SDK UI
        - Select "Copy Python Command"
        - Replace the placeholder commands with the actual ones
    """
    print(f"--- Processing Cape ID: {archive_id} ---")

    try:
        # STEP 1: Load the cape's archive
        # TODO: Replace with actual HD2SDK command for loading archives
        # Find the correct command by right-clicking the "Load Archive" button
        # in the HD2SDK UI and selecting "Copy Python Command"
        bpy.ops.hd2.load_archive(archive_id=archive_id)  # Placeholder command

        # STEP 2: Import all meshes from the loaded archive
        # TODO: Replace with actual HD2SDK command for importing meshes
        # This command should import all mesh assets from the currently loaded archive
        bpy.ops.hd2.import_all_meshes()  # Placeholder command

        # Track imported objects so we can operate on them
        # After import, newly added objects should be selected
        imported_objects = bpy.context.selected_objects[:]

        if not imported_objects:
            print(f"Warning: No meshes were imported for {archive_id}. Skipping.")
            return

        print(f"Found {len(imported_objects)} object(s) to process")

        # STEP 3: Collapse each imported mesh to a single point
        for obj in imported_objects:
            # Only process mesh objects (skip cameras, lights, etc.)
            if obj.type == 'MESH':
                print(f"  - Collapsing mesh: {obj.name}")

                # Set this object as the active object for operations
                bpy.context.view_layer.objects.active = obj

                # Enter Edit Mode to modify the mesh geometry
                bpy.ops.object.mode_set(mode='EDIT')

                # Select all vertices in the mesh
                bpy.ops.mesh.select_all(action='SELECT')

                # Merge all vertices to the center point
                # This collapses the entire mesh to a single vertex, making it invisible
                bpy.ops.mesh.merge(type='CENTER')

                # Return to Object Mode for further operations
                bpy.ops.object.mode_set(mode='OBJECT')

                # STEP 4: Save the modified mesh to the patch
                # TODO: Replace with actual HD2SDK command for saving meshes
                # This should write the collapsed mesh back to your active patch
                print(f"  - Saving collapsed mesh: {obj.name}")
                bpy.ops.hd2.save_mesh(mesh_id=obj.name)  # Placeholder command

        # STEP 5: Clean up the scene by removing processed objects
        # This frees memory and prepares for the next cape
        bpy.ops.object.delete({"selected_objects": imported_objects})
        print(f"✓ Successfully processed and cleaned up {archive_id}\n")

    except Exception as e:
        # Error handling: Log the error and attempt cleanup
        print(f"✗ Error occurred while processing {archive_id}: {e}")
        print(f"  Attempting cleanup...\n")

        # Ensure we're in Object Mode before cleanup
        # Edit Mode operations can fail if we're in the wrong mode
        if bpy.context.object and bpy.context.object.mode != 'OBJECT':
            try:
                bpy.ops.object.mode_set(mode='OBJECT')
            except:
                pass  # If mode switching fails, continue anyway

        # Clean up any leftover objects from the failed import
        try:
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete()
        except:
            pass  # If cleanup fails, continue to next cape

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main entry point for the cape hiding automation script.

    This function orchestrates the entire process:
    1. Loads cape Archive IDs from the configured file
    2. Validates that IDs were found
    3. Iterates through each cape and processes it
    4. Reports completion status

    Prerequisites:
        - Blender must have HD2SDK plugin installed and configured
        - Base game archive must be loaded
        - A new patch must be created before running this script

    Returns:
        None

    Example output:
        Successfully loaded 47 cape IDs from './cape_ids.txt'
        Found 47 cape IDs to process.
        Processing cape 1 of 47...
        --- Processing Cape ID: 0fe88d9b08f6fe80 ---
        Found 1 object(s) to process
          - Collapsing mesh: cape_mesh_01
          - Saving collapsed mesh: cape_mesh_01
        ✓ Successfully processed and cleaned up 0fe88d9b08f6fe80
        ...
        --- Automation Complete! ---
        All specified capes have been processed. You can now write the final patch.
    """
    print("=" * 60)
    print("Helldivers 2: Cape Hiding Automation")
    print("=" * 60)
    print()

    # Ensure prerequisites are met
    print("⚠ IMPORTANT: Before running this script, ensure:")
    print("  1. HD2SDK plugin is installed and configured")
    print("  2. Base game archive is loaded (click star icon in Modding panel)")
    print("  3. New patch is created (click 'New Patch' in Modding panel)")
    print()

    # Load cape IDs from the configured file
    cape_ids = get_cape_ids(CAPE_ID_FILE_PATH)

    if not cape_ids:
        print("✗ No cape IDs found. Please check the path and contents of your file.")
        print(f"  Current path: {CAPE_ID_FILE_PATH}")
        print("  Update CAPE_ID_FILE_PATH at the top of this script.")
        return

    # Display processing information
    total_capes = len(cape_ids)
    print(f"Found {total_capes} cape IDs to process.")
    print()
    print("Starting batch processing...")
    print("-" * 60)
    print()

    # Process each cape sequentially
    for i, cape_id in enumerate(cape_ids, start=1):
        print(f"[{i}/{total_capes}] Processing cape ID: {cape_id}")
        process_cape(cape_id)

    # Report completion
    print("=" * 60)
    print("✓ Automation Complete!")
    print("=" * 60)
    print()
    print("All specified capes have been processed.")
    print()
    print("Next steps:")
    print("  1. Go to the 'Modding' panel in Blender (press N)")
    print("  2. Click 'Write Patch' to save your .patch_0 file")
    print("  3. Deploy the patch file to your Helldivers 2 mod directory")
    print()

# Script entry point
# This ensures the script only runs when executed directly (not when imported)
if __name__ == "__main__":
    main()