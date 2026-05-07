import streamlit as st
import time

# -------------------------------------------------
# PAGE SETTINGS
# -------------------------------------------------
st.set_page_config(
    page_title="Smart Traffic Simulation",
    layout="wide"
)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.markdown("""
<h1 style='text-align:center; color:#00FFAA;'>
🚦 Smart Traffic Control Dashboard
</h1>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR CONTROLS
# -------------------------------------------------
st.sidebar.header("⚙️ Traffic Controls")

v1 = st.sidebar.slider(
    "🚗 Vehicles at Signal 1",
    0, 50, 15
)

v2 = st.sidebar.slider(
    "🚗 Vehicles at Signal 2",
    0, 50, 10
)

distance = st.sidebar.slider(
    "📏 Distance Between Signals (m)",
    50, 500, 200
)

speed = st.sidebar.slider(
    "🚗 Vehicle Speed (m/s)",
    5, 25, 10
)

start = st.sidebar.button("▶ Start Simulation")

# -------------------------------------------------
# SMART TIMING LOGIC
# -------------------------------------------------
g1 = 5 + v1
g2 = 5 + v2

delay = distance / speed

# -------------------------------------------------
# SIGNAL FUNCTION
# -------------------------------------------------
def show_signal(name, active):

    red = "⚫"
    yellow = "⚫"
    green = "⚫"

    if active == "red":
        red = "🔴"

    elif active == "yellow":
        yellow = "🟡"

    elif active == "green":
        green = "🟢"

    st.markdown(f"""
    <div style="
        background:#1e1e1e;
        padding:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:0px 0px 15px #444;
    ">

    <h2 style='color:white;'>{name}</h2>

    <div style='font-size:55px;'>{red}</div>
    <div style='font-size:55px;'>{yellow}</div>
    <div style='font-size:55px;'>{green}</div>

    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# PLACEHOLDERS
# -------------------------------------------------
col1, col2 = st.columns(2)

signal1_box = col1.empty()
signal2_box = col2.empty()

road_box = st.empty()
status_box = st.empty()

# -------------------------------------------------
# ROAD DESIGN
# -------------------------------------------------
def draw_road(car_position):

    spaces = "&nbsp;" * car_position

    road_box.markdown(f"""
    <div style="
        background:#333;
        height:100px;
        border-radius:10px;
        position:relative;
        margin-top:20px;
    ">

    <div style="
        position:absolute;
        top:25px;
        left:20px;
        font-size:40px;
        color:white;
    ">
    {spaces}🚗
    </div>

    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# CAR MOVEMENT
# -------------------------------------------------
def move_car():

    for i in range(0, 120, 5):

        draw_road(i)

        time.sleep(0.05)

# -------------------------------------------------
# SIMULATION
# -------------------------------------------------
if start:

    # ---------------- SIGNAL 1 GREEN ----------------
    for t in range(g1, 0, -1):

        with signal1_box:
            show_signal("🚦 Signal 1", "green")

        with signal2_box:
            show_signal("🚦 Signal 2", "red")

        status_box.success(f"🟢 Signal 1 GREEN : {t}s")

        move_car()

    # ---------------- SIGNAL 1 YELLOW ----------------
    for t in range(3, 0, -1):

        with signal1_box:
            show_signal("🚦 Signal 1", "yellow")

        with signal2_box:
            show_signal("🚦 Signal 2", "red")

        status_box.warning(f"🟡 Signal 1 YELLOW : {t}s")

        time.sleep(1)

    # ---------------- DELAY ----------------
    status_box.info(
        f"🚗 Vehicles moving to Signal 2 "
        f"(Delay = {delay:.1f}s)"
    )

    time.sleep(delay)

    # ---------------- SIGNAL 2 GREEN ----------------
    for t in range(g2, 0, -1):

        with signal2_box:
            show_signal("🚦 Signal 2", "green")

        with signal1_box:
            show_signal("🚦 Signal 1", "red")

        status_box.success(f"🟢 Signal 2 GREEN : {t}s")

        move_car()

    # ---------------- SIGNAL 2 YELLOW ----------------
    for t in range(3, 0, -1):

        with signal2_box:
            show_signal("🚦 Signal 2", "yellow")

        with signal1_box:
            show_signal("🚦 Signal 1", "red")

        status_box.warning(f"🟡 Signal 2 YELLOW : {t}s")

        time.sleep(1)

    status_box.success("✅ Traffic Cycle Completed")

# -------------------------------------------------
# STATISTICS PANEL
# -------------------------------------------------
st.divider()

st.subheader("📊 Live Traffic Statistics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("🚗 Signal 1 Vehicles", v1)
c2.metric("🚗 Signal 2 Vehicles", v2)

c3.metric("🟢 Signal 1 Time", f"{g1}s")
c4.metric("🟢 Signal 2 Time", f"{g2}s")

st.write(f"📏 Distance Between Signals : {distance} m")
st.write(f"🚗 Vehicle Speed : {speed} m/s")
st.write(f"⏱️ Coordination Delay : {delay:.1f}s")

st.info(
    "Smart coordination helps vehicles move "
    "smoothly from Signal 1 to Signal 2 "
    "without unnecessary stopping."
)