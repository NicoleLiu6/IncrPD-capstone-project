
import streamlit as st

# Function to calculate TBW based on gender and weight
def calculate_tbw(gender, weight):
    if gender == "Male":
        return weight * 0.6
    else:
        return weight * 0.55

# Function to calculate the required dialysate volume for a target Kt/V
def calculate_volume_required(target_ktv, dialysate_urea, serum_urea, tbw):
    volume_required = (target_ktv * tbw * serum_urea) / dialysate_urea
    return round(volume_required, 1)  # Round to 1 decimal place

# Function to calculate volume saved by using IncrePD
def calculate_volume_saved(full_pd_volume, incre_pd_volume):
    volume_saved = full_pd_volume - incre_pd_volume
    return round(volume_saved, 1)  # Round to 1 decimal place

# Main app function
def main():
    st.title("Incre PD Calculator")

    # Page selection in the sidebar
    page = st.sidebar.selectbox("Select Page", ["IncrPD Health Parameters", "Symptom Assessment", "Full PD vs IncrPD Comparison"])

    if page == "IncrPD Health Parameters":
        st.sidebar.header("User Input Parameters - IncrPD Health Parameters")

        # User inputs for IncrPD Health Parameters page
        weight = st.sidebar.slider("Weight (kg)", 50, 100, 70, 1)
        gender = st.sidebar.radio("Gender", ["Male", "Female"])
        urine_vol = st.sidebar.number_input("24-hour Urine Volume (L/day)", value=2.0, min_value=0.1, max_value=5.0, step=0.1)
        urine_urea = st.sidebar.number_input("24-hour Urine Urea (MMOL/L)", value=289.0, min_value=10.0, max_value=500.0, step=10.0)
        serum_urea = st.sidebar.number_input("Serum Urea (MMOL/L)", value=29.0, min_value=1.0, max_value=800.0, step=0.1)

        # Calculate TBW and Residual Kidney Function (RKF - Urea Clearance)
        tbw = calculate_tbw(gender, weight)
        rkf_urea_clearance = (urine_urea / serum_urea * urine_vol) / tbw
        volume_needed_per_day = (0.25 - rkf_urea_clearance) * tbw

        # Display results for IncrPD Health Parameters
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Residual Kidney Function (RKF) – Urea Clearance (L/day):")
            st.metric(label="RKF (Urea Clearance)", value=f"{rkf_urea_clearance:.1f} L/day")

        with col2:
            st.subheader("Volume Needed per day (L/day):")
            st.metric(label="Volume Needed", value=f"{volume_needed_per_day:.1f} L")

        # Store the IncrePD value for later use on the third page
        st.session_state.increpd = round(volume_needed_per_day, 1)

    elif page == "Symptom Assessment":
        st.sidebar.header("User Input Parameters - Symptom Assessment")

        # User inputs for symptom assessment page
        nausea = st.sidebar.radio("Nausea (0=No, 1=Yes)", [0, 1])
        vomiting = st.sidebar.radio("Vomiting (0=No, 1=Yes)", [0, 1])
        pruritus = st.sidebar.radio("Pruritus (0=No, 1=Yes)", [0, 1])
        appetite = st.sidebar.radio("Appetite (0=No, 1=Yes)", [0, 1])
        sleep = st.sidebar.radio("Sleep (0=No, 1=Yes)", [0, 1])
        sudden_weight_loss = st.sidebar.radio("Sudden Weight Loss (0=No, 1=Yes)", [0, 1])
        pitting_oedema = st.sidebar.slider("Pitting Oedema (0=No, 1=Mild, 2=Moderate, 3=Severe)", 0, 3, 0)

        # Calculate total symptom score
        total_score = nausea + vomiting + pruritus + appetite + sleep + sudden_weight_loss + pitting_oedema

        # Display results for symptom assessment
        st.subheader("Total Symptom Score:")
        st.metric(label="Score", value=f"{total_score} / 9")

    elif page == "Full PD vs IncrPD Comparison":
        st.sidebar.header("User Input Parameters - Full PD vs IncrPD Comparison")

        # Highlight and display IncrePD at the top of the page with color
        st.markdown('<h2 style="color:blue;">**IncrePD Volume (L/day)**</h2>', unsafe_allow_html=True)
        st.markdown("You can manually adjust the IncrePD volume below:")

    # Retrieve IncrePD value from the first page with an option to modify it manually
        default_increpd = st.session_state.increpd if "increpd" in st.session_state else 8.0
        incre_pd_volume = st.number_input("IncrePD Dialysate Volume (L/day)", value=float(default_increpd), step=0.1)

    # User inputs for Full PD vs IncrPD Comparison page
        weight = st.sidebar.slider("Weight (kg)", 50, 100, 70, 1)
        gender = st.sidebar.radio("Gender", ["Male", "Female"])
        dialysate_urea = st.sidebar.number_input("Dialysate Urea (MMOL/L)", value=100.0, min_value=1.0, max_value=800.0, step=0.1)
        serum_urea = st.sidebar.number_input("Serum Urea (MMOL/L)", value=29.0, min_value=1.0, max_value=800.0, step=0.1)

    # Calculate TBW and required dialysate volume for target Kt/V of 1.77
        tbw = calculate_tbw(gender, weight)
        target_ktv = 1.77
        full_pd_volume = calculate_volume_required(target_ktv, dialysate_urea, serum_urea, tbw)

        volume_saved = calculate_volume_saved(full_pd_volume, incre_pd_volume)

    # Calculate water and plastic saved
        bags_saved = volume_saved / 2  # Each 2L saved equals 1 bag saved
        plastic_saved = bags_saved * 0.155  # Each bag weighs 0.155 kg of plastic
        water_saved = (bags_saved * 35) + volume_saved  # 35L of water saved per bag during manufacturing + volume saved

    # Display results
        st.subheader("Full PD Volume Required (Kt/V of 1.77) (L/day):")
        st.metric(label="Full PD Volume Required", value=f"{full_pd_volume:.1f} L")

        st.subheader("Volume Saved by IncrePD (L/day):")
        st.metric(label="Volume Saved", value=f"{volume_saved:.1f} L")

    # Display water and plastic savings
        st.subheader("Environmental Impact of Volume Saved:")
        st.metric(label="Water Saved (L/day)", value=f"{water_saved:.1f} L")
        st.metric(label="Plastic Saved (kg/day)", value=f"{plastic_saved:.3f} kg")

if __name__ == "__main__":
    main()
    
