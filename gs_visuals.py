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
CAR_FLYTHROUGH = "./flythrough_car.mp4"
CAR_MASKING = "./car_mask_fixed.mp4"

# --- Create Navigation Tabs ---
tab1, tab2, tab3 = st.tabs([
    "Ground-Truth Comparison", 
    "UCLA Gateway Plaza Videos", 
    "Car Proof of Concept Videos"
])


# ==========================================
# TAB 1: Centered Split-Screen Image Slider
# ==========================================
with tab1:
    st.subheader("Frame-by-Frame Example Inspection")
    st.write("Click on a thumbnail to select a frame")
    
    # Gather paired image tracking sequences
    gt_images = sorted([f for f in os.listdir(GT_DIR) if f.endswith(('.png', '.jpg', '.jpeg')) if "gt" in f or "input" in f])
    render_images = sorted([f for f in os.listdir(RENDER_DIR) if f.endswith(('.png', '.jpg', '.jpeg')) if "render" in f or "frame" in f])

    if not gt_images or not render_images:
        gt_images = sorted([f for f in os.listdir(GT_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))])
        render_images = sorted([f for f in os.listdir(RENDER_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))])

    total_frames = min(len(gt_images), len(render_images))

    if total_frames == 0:
        st.error("No valid frame sequences discovered inside directory mappings.")
    else:
        # Initialize session state for tracking selected frame index
        if "selected_frame" not in st.session_state:
            st.session_state.selected_frame = 0

        # Create horizontal grid for thumbnails
        thumb_cols = st.columns(total_frames)
        
        for idx in range(total_frames):
            with thumb_cols[idx]:
                thumb_img = Image.open(os.path.join(GT_DIR, gt_images[idx]))
                st.image(thumb_img, use_container_width=True)
                if st.button(f"frame {idx + 1}", key=f"btn_frame_{idx}", use_container_width=True):
                    st.session_state.selected_frame = idx

        # Set active index from user selection
        frame_idx = st.session_state.selected_frame
        
        # Pull images out of targeted directory pointers
        img_gt = Image.open(os.path.join(GT_DIR, gt_images[frame_idx]))
        img_render = Image.open(os.path.join(RENDER_DIR, render_images[frame_idx]))

        st.caption(f"Currently tracking frame index: {frame_idx} | Source: {gt_images[frame_idx]}")

        # --- CENTERING MECHANISM ---
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
    # 1. Flythrough Section (Top & Prominent)
    st.markdown("## Cinematic Camera Fly-Through")
    st.write("Continuous trajectory path rendered out of the 3DGS Plaza reconstruction")
    if os.path.exists(PLAZA_FLYTHROUGH):
        st.video(PLAZA_FLYTHROUGH, autoplay=True, loop=True, muted=True)
    else:
        st.info(f"Drop your plaza fly-through video asset at `{PLAZA_FLYTHROUGH}` to render playback.")

    st.markdown("---") # Visual separator line

    # 2. Masking Section (Below Flythrough)
    st.markdown("## Dynamic Training Mask Visualizations")
    st.write("Semantic rendering masks applied to filter noise, eliminate transient elements, and isolate rigid geometry.")
    if os.path.exists(PLAZA_MASKING):
        st.video(PLAZA_MASKING, autoplay=True, loop=True, muted=True)
    else:
        st.info(f"Drop your plaza masking video asset at `{PLAZA_MASKING}` to render playback.")


# ==========================================
# TAB 3: Car POC (Flythrough Top, Masking Bottom)
# ==========================================
with tab3:
    st.subheader("Vehicle Proof of Concept")
    st.write("Simple static scenario with easy key-features for COLMAP initialization and GS Optimization")

    # 1. Car Flythrough (Top)
    st.markdown("## Car Render Fly-Through")
    if os.path.exists(CAR_FLYTHROUGH):
        st.video(CAR_FLYTHROUGH, autoplay=True, loop=True, muted=True)
    else:
        st.info(f"Drop your car fly-through video asset at `{CAR_FLYTHROUGH}` to render playback.")

    st.markdown("---")

    # 2. Car Masking (Below Flythrough)
    st.markdown("## Car Mask Visualizations")
    if os.path.exists(CAR_MASKING):
        st.video(CAR_MASKING, autoplay=True, loop=True, muted=True)
    else:
        st.info(f"Drop your car masking video asset at `{CAR_MASKING}` to render playback.")