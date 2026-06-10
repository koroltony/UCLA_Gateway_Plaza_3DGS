# UCLA Gateway Plaza 3D Gaussian Splatting (3DGS) Showcase

<img width="200" alt="frame_0913" src="https://github.com/user-attachments/assets/eb17a347-a19b-430f-bdac-f45adb7dbd5d" />
<img width="200" alt="frame_0633" src="https://github.com/user-attachments/assets/5864f021-be46-4516-b7fd-c5e3c62e882e" />
<img width="200" alt="frame_0417" src="https://github.com/user-attachments/assets/63dba387-9169-4249-9ab5-6061baebe304" />
<img width="200" alt="frame_0065" src="https://github.com/user-attachments/assets/b5cb5b5d-189e-4e41-ae02-82e8820846a0" />

An interactive presentation dashboard built with Streamlit to visualize and evaluate 3D Gaussian Splatting (3DGS) reconstruction fidelity. This project features dynamic frame-by-frame viewport comparisons, cinematic camera fly-throughs, and structural training mask tracking for both the primary urban street scene and a vehicle proof of concept.

## Live Interactive Presentation
The complete dashboard is hosted on the Streamlit Community Cloud and can be accessed dynamically via the link below:

**[Launch the Interactive Website!](https://uclagatewayplaza3dgs-f8wajulkkjqwy7nf4cusxg.streamlit.app/)**
---
**[Launch SuperSplat Viewer](https://superspl.at/scene/ccb8ad42)**

---

## Project Architecture & Contents

The dashboard is structured into four unified navigation modules designed to showcase various stages of our computer vision and simulation pipeline:

### 1. Interactive Viewport Comparison
* **Purpose:** Validates pixel-level reconstruction accuracy against the training baseline.
* **Functionality:** Features a centered, responsive **Juxtapose Slider** widget. Users can seamlessly scrub back and forth down to the pixel level to contrast the original ground-truth video captures against synthetic 3DGS viewports.

### 2. Plaza Reconstruction Media
* **Cinematic Camera Fly-Through:** A camera path trajectory rendered directly out of the optimized GS model, showcasing continuous spatial consistency across the unstaged outdoor crosswalk scene.
* **Dynamic Training Mask Visualizations:** Showcases the background semantic masks utilized during Nerfstudio training to isolate static rigid plaza geometry and filter transient noise (like moving pedestrians or lighting shifts).

### 3. Car Proof of Concept
* **Car Rendering Reconstruction:** A preliminary proof-of-concept utilizing highly overlapping frames, easy key-frame mapping, and a static environment executed before scaling up to the full UCLA plaza reconstruction.
* **Visual Asset Tracking:** Compares the standard unmasked fly-through (cleaned manually using Supersplat) against its corresponding isolated binary masking video sequence to evaluate geometry filtering quality.

### 4. Nvidia Isaac Simulation Integration
* **Fused Physical and Gaussian Representations:** Imports the completed 3DGS environment into the Nvidia Isaac engine, mapping the organic Gaussian reconstruction directly alongside traditional rigid 3D physical models to verify spatial accuracy.
* **Simulating Vehicle Dynamics:** Demonstrates the practical downstream robotics applications of the pipeline. This section tracks hybrid physics simulations, testing how autonomous vehicle agents interact with and navigate through the reconstructed 3DGS environment.
