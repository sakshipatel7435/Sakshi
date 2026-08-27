import streamlit as st
import pickle

class DummyModel:

    def predict(self, features):
        t1, t2 = (features[0][0], features[0][1])
        return ['Team 1'] if t1 > t2 else ['Team 2']
st.title('IPL Match Outcome Predictor')
try:
    with open('ipl_model.pkl', 'rb') as f:
        model = pickle.load(f)
    st.success("Model 'ipl_model.pkl' loaded successfully!")
except FileNotFoundError:
    st.error("Error: The model file 'ipl_model.pkl' was not found. Please ensure it is in the same directory.")
    model = None
except Exception as e:
    st.error(f'Error loading model: {e}')
    model = None
st.write('---')
if model:
    st.header('Fantasy Cricket Match Scenario')
    with st.form('match_prediction_form'):
        st.write('Enter the current match statistics to predict the winner:')
        team1_runs = st.number_input('Team 1 Runs', min_value=0, value=180)
        team2_runs = st.number_input('Team 2 Runs', min_value=0, value=150)
        wickets_left = st.number_input('Wickets Left (Team 2)', min_value=0, max_value=10, value=5)
        submit_button = st.form_submit_button(label='Predict Winner')
    if submit_button:
        input_data = [[team1_runs, team2_runs, wickets_left]]
        prediction = model.predict(input_data)[0]
        st.write('### Prediction Result')
        if prediction == 'Team 1':
            st.success(f'Predicted Winner: {prediction}')
        elif prediction == 'Team 2':
            st.info(f'Predicted Winner: {prediction}')
        else:
            st.write(f'Predicted Winner: {prediction}')