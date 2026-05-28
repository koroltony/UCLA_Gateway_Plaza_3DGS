# UCLA Gateway Plaza 3D Gaussian Splatting (3DGS) Showcase

An interactive presentation dashboard built with Streamlit to visualize and evaluate 3D Gaussian Splatting (3DGS) reconstruction fidelity. This project features dynamic frame-by-frame viewport comparisons, cinematic camera fly-throughs, and structural training mask tracking for both the primary urban street scene and a vehicle proof of concept.

## Live Interactive Presentation
The complete dashboard is hosted on the Streamlit Community Cloud and can be accessed dynamically via the link below:

**[Launch the Live 3DGS Dashboard Workspace](https://uclagatewayplaza3dgs-f8wajulkkjqwy7nf4cusxg.streamlit.app/)**

---

## Project Architecture & Contents

The dashboard is structured into three unified navigation modules designed to showcase various stages of our computer vision pipeline:

### 1. Interactive Viewport Comparison
* **Purpose:** Validates pixel-level reconstruction accuracy against the training baseline.
* **Functionality:** Features a centered, responsive **Juxtapose Slider** widget. Users can seamlessly scrub back and forth down to the pixel level to contrast the original ground-truth video captures against synthetic 3DGS viewports.
* **Timeline Tracker:** A sequential timeline slider allows frame-by-frame scrubbing across several side-by-side examples to compare GS output vs ground-truth training frames

### 2. Plaza Reconstruction Media
* **Cinematic Camera Fly-Through:** A camera path trajectory rendered directly out of the optimized GS model, showcasing continuous spatial consistency.
* **Dynamic Training Mask Visualizations:** Showcases the background semantic masks (`empty_masked_final_small.mp4`) utilized during Nerfstudio training to isolate static rigid plaza geometry and filter transient noise.

### 3. Car Proof of Concept (POC)
* **Car Rendering Reconstruction:** A proof-of-concept using highly overlapping frames, easy key-frame mapping, and static environment done before the UCLA plaza reconstruction.
* **Visual Asset Tracking:** Includes a fly-through alongside its corresponding isolated binary masking video sequence.
