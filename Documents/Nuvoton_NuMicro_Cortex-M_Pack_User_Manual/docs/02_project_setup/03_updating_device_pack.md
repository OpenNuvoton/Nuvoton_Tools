## Updating the Device Pack

The Nuvoton device pack (DFP) defines the flash and SRAM regions, flash algorithms and SVD files of each
device. Update it when a newer pack is released or when flashing reports a region that is not writable.

1. Open `cbuild-pack.yml` in the project folder and change the pack version to the latest one.

   <p>
       <img src="../../media/pack_update1.png" alt="pack_update1.png" width="433">
   </p>

2. Click **Refresh** in the **CMSIS** view to reload the pack, then rebuild the solution.

   <p>
       <img src="../../media/pack_update2.png" alt="pack_update2.png" width="409">
   </p>
