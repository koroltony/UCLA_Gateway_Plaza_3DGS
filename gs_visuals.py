import os
import streamlit as st
from PIL import Image
from streamlit_image_comparison import image_comparison

# Set page layout to WIDE so media elements have plenty of breathing room
st.set_page_config(page_title="3DGS Project Dashboard", layout="wide")

st.title("UCLA Gateway Plaza 3DGS Reconstruction")
st.write("Interactive demonstration of 3DGS applied to an unstaged outdoor crosswalk scene")

# --- Define Media Resource Paths ---
# Plaza Assets
GT_DIR = "./ground_truth"
RENDER_DIR = "./rendering"
PLAZA_FLYTHROUGH = "./empty_masked_final_small.mp4"
PLAZA_MASKING = "./mask_visualization_small.mp4"

# Car POC Assets
CAR_FLYTHROUGH = "./car_flythrough_blurred_f.mp4"
CAR2_VIDEO = "./car2_blurred_f.mp4"
CAR_MASKING = "./car_mask_blurred_f.mp4"
MASK_COMP1 = "./mask_comp1.jpg"
MASK_COMP2 = "./mask_comp2.jpg"

# Isaac Assets
RECONSTRUCTION_ISAAC = "./Reconstruction_in_Isaac.jpg"
PHYSICAL_MODEL = "./3D_physical_model.jpg"
ISAAC_MOVING_CAR = "./Isaac_Moving_Car_final.mp4"
HYBRID_ISAAC = "./hybrid_isaac_final.mp4"

# --- Helper Functions (Caching Removed) ---
def get_sorted_frames(directory, filter_keywords):
    if not os.path.exists(directory):
        return []
    # FIXED: Added .png extension check to prevent "No valid frame sequences discovered" error
    all_files = sorted([f for f in os.listdir(directory) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    filtered = [f for f in all_files if any(k in f for k in filter_keywords)]
    return filtered if filtered else all_files

def load_image(file_path):
    # Directly loading without memory caching
    return Image.open(file_path)

# --- Create Navigation Tabs ---
tab1, tab2, tab3, tab4 = st.tabs([
    "Ground-Truth Comparison", 
    "UCLA Gateway Plaza Videos", 
    "Car Proof of Concept Videos",
    "Nvidia Isaac Simulation"
])


# ==========================================
# TAB 1: Centered Split-Screen Image Slider
# ==========================================
with tab1:
    st.subheader("Frame-by-Frame Example Inspection")
    st.write("Click on a thumbnail to select a frame")
    
    gt_images = get_sorted_frames(GT_DIR, ["gt", "input", "frame"])
    render_images = get_sorted_frames(RENDER_DIR, ["render", "frame"])
    total_frames = min(len(gt_images), len(render_images))

    if total_frames == 0:
        st.error("No valid frame sequences discovered inside directory mappings.")
    else:
        if "selected_frame" not in st.session_state:
            st.session_state.selected_frame = 0

        thumb_cols = st.columns(total_frames)
        
        for idx in range(total_frames):
            with thumb_cols[idx]:
                thumb_img = load_image(os.path.join(GT_DIR, gt_images[idx]))
                st.image(thumb_img, width='stretch')
                if st.button(f"frame {idx + 1}", key=f"btn_frame_{idx}", width='stretch'):
                    st.session_state.selected_frame = idx

        frame_idx = st.session_state.selected_frame
        
        img_gt = load_image(os.path.join(GT_DIR, gt_images[frame_idx]))
        img_render = load_image(os.path.join(RENDER_DIR, render_images[frame_idx]))

        st.caption(f"Currently tracking frame index: {frame_idx} | Source: {gt_images[frame_idx]}")

        left_spacer, center_col, right_spacer = st.columns([1, 3, 1])
        
        with center_col:
            image_comparison(
                img1=img_gt,
                img2=img_render,
                label1="Ground Truth Video",
                label2="3DGS Render",
                starting_position=50,
                show_labels=True,
                make_responsive=True,
                in_memory=True
            )


# ==========================================
# TAB 2: Plaza Media (Flythrough Top, Masking Bottom)
# ==========================================
with tab2:
    st.markdown("## Cinematic Camera Fly-Through")
    st.write("Continuous trajectory path rendered out of the 3DGS Plaza reconstruction")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists(PLAZA_FLYTHROUGH):
            st.video(PLAZA_FLYTHROUGH, autoplay=True, loop=True, muted=True)
        else:
            st.info(f"Drop your plaza fly-through video asset at `{PLAZA_FLYTHROUGH}` to render playback.")

    st.markdown("---")

    st.markdown("## Dynamic Training Mask Visualizations")
    st.write("Semantic rendering masks applied to filter noise, eliminate transient elements, and isolate rigid geometry.")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists(PLAZA_MASKING):
            st.video(PLAZA_MASKING, autoplay=True, loop=True, muted=True)
        else:
            st.info(f"Drop your plaza masking video asset at `{PLAZA_MASKING}` to render playback.")


# ==========================================
# TAB 3: Car POC (Flythrough Top, Car 2 Middle, Masking Bottom)
# ==========================================
with tab3:
    st.subheader("Vehicle Proof of Concept")
    st.write("Simple static scenario with easy key-features for COLMAP initialization and GS Optimization")

    st.markdown("## Car Render Fly-Through")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists(CAR_FLYTHROUGH):
            st.video(CAR_FLYTHROUGH, autoplay=True, loop=True, muted=True)
        else:
            st.info(f"Drop your car fly-through video asset at `{CAR_FLYTHROUGH}` to render playback.")

    st.markdown("---")

    st.markdown("## Secondary Car Render")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists(CAR2_VIDEO):
            st.video(CAR2_VIDEO, autoplay=True, loop=True, muted=True)
        else:
            st.info(f"Drop your second car video asset at `{CAR2_VIDEO}` to render playback.")
        
    st.markdown("---")

    st.markdown("## Car Mask Visualizations")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists(CAR_MASKING):
            st.video(CAR_MASKING, autoplay=True, loop=True, muted=True)
        else:
            st.info(f"Drop your car masking video asset at `{CAR_MASKING}` to render playback.")

    st.markdown("---")

    st.markdown("## Car Mask Comparison Images")
    if os.path.exists(MASK_COMP1) and os.path.exists(MASK_COMP2):
        img_col1, img_col2 = st.columns(2)
        with img_col1:
            img1 = load_image(MASK_COMP1)
            st.image(img1, caption="Unmasked - Cleaned in Supersplat", width='stretch')
        with img_col2:
            img2 = load_image(MASK_COMP2)
            st.image(img2, caption="Masked", width='stretch')
    else:
        st.info(f"Verify that both `{MASK_COMP1}` and `{MASK_COMP2}` are located in your root directory to show static image comparison views side-by-side.")


# ==========================================
# TAB 4: Nvidia Isaac Simulation
# ==========================================
with tab4:
    st.markdown("## Fused Physical and Gaussian Representations")
    st.write("Comparing the reconstructed scene with the physical 3D model representation.")
    
    isaac_col1, isaac_col2 = st.columns(2)
    with isaac_col1:
        if os.path.exists(RECONSTRUCTION_ISAAC):
            recon_img = load_image(RECONSTRUCTION_ISAAC)
            st.image(recon_img, caption="Reconstruction in Isaac", width='stretch')
        else:
            st.info(f"Missing image asset at `{RECONSTRUCTION_ISAAC}`")
            
    with isaac_col2:
        if os.path.exists(PHYSICAL_MODEL):
            phys_img = load_image(PHYSICAL_MODEL)
            st.image(phys_img, caption="3D Physical Model", width='stretch')
        else:
            st.info(f"Missing image asset at `{PHYSICAL_MODEL}`")

    st.markdown("---")

   
    st.markdown("## Simulating Vehicle Dynamics")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists(ISAAC_MOVING_CAR):
            st.video(ISAAC_MOVING_CAR, autoplay=True, loop=True, muted=True)
        else:
            st.info(f"Drop your moving car simulation video asset at `{ISAAC_MOVING_CAR}` to render playback.")
        
    st.markdown("---")

    st.markdown("## Isaac Environment Tour")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists(HYBRID_ISAAC):
            st.video(HYBRID_ISAAC, autoplay=True, loop=True, muted=True)
        else:
            st.info(f"Drop your hybrid simulation video asset at `{HYBRID_ISAAC}` to render playback.")