import streamlit as st
import pickle as pk



html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Pizza Prize Prediction Machine Learning  Model</h2>
</div>
"""

def main():
    st.markdown(html_temp,unsafe_allow_html=True)
    #st.markdown(html_temp, unsafe_allow_html=True)
    # load the model
    model = pk.load(open("Pizza_Prize_Prediction", "rb"))
    Company = st.selectbox("Company Class", ("A", "B", "C", "D", "E"))
    if Company == "A":
        f1 = 0
    elif Company == "B":
        f1 = 1
    elif Company == "C":
        f1 = 2
    elif Company == "D":
        f1 = 3
    else:
        f1 = 4

    f2 = st.slider("Diameter", 8, 22)


    Topping = st.selectbox("Topping", (
    "chicken", "mushrooms", "mozzarella", "smoked beef", "tuna", "vegetables", "meat", "black papper", "sausage", "beef", "papperoni", "onion"))
    if Topping == "beef":
        f3 = 0
    elif Topping == "black papper":
        f3 = 1
    elif Topping == "chicken":
        f3 = 2
    elif Topping == "meat":
        f3 = 3
    elif Topping == "mozzarella":
        f3 = 4
    elif Topping == "mushrooms":
        f3 = 5
    elif Topping == "onion":
        f3 = 6
    elif Topping == "papperoni":
        f3 = 7
    elif Topping == "sausage":
        f3 = 8
    elif Topping == "smoked beef":
        f3 = 9
    elif Topping == "tuna":
        f3 = 10
    else:
        f3 = 11

    Variant = st.selectbox("Variant", (
        "classic", "meat_lovers", "double_mix", "crunchy", "new_york", "double_decker", "double_signature", "american_favorite", "BBQ_meat_fiesta",
        "super_supreme", "spicy_tuna", "BBQ_sausage","extravaganza","meat_eater","gournet_greek","italian_veggie","thai_veggie","american_classic","neptune_tuna",
    "spicy tuna"))
    if Variant == "BBQ_meat_fiesta":
        f4 = 0
    elif Variant == "BBQ_sausage":
        f4 = 1
    elif Variant == "american_classic":
        f4 = 2
    elif Variant == "american_favorite":
        f4 = 3
    elif Variant == "classic":
        f4 = 4
    elif Variant == "crunchy":
        f4 = 5
    elif Variant == "double_decker":
        f4 = 6
    elif Variant == "double_mix":
        f4 = 7
    elif Variant == "double_signature":
        f4 = 8
    elif Variant == "extravaganza":
        f4 = 9
    elif Variant == "gournet_greek":
        f4 = 10
    elif Variant == "italian_veggie":
        f4 = 11
    elif Variant == "meat_eater":
        f4 = 12
    elif Variant == "meat_lovers":
        f4 = 13
    elif Variant == "neptune_tuna":
        f4 = 14
    elif Variant == "new_york":
        f4 = 15
    elif Variant == "spicy tuna":
        f4 = 16
    elif Variant == "spicy_tuna":
        f4 = 17
    elif Variant == "super_supreme":
        f4 = 18
    else:
        f4 = 19

    Size = st.selectbox("Pizza Size", ("medium", "small", "large", "reguler","jumbo","XL"))
    if Size == "XL":
        f5 = 0
    elif Size == "jumbo":
        f5 = 1
    elif Size == "large":
        f5 = 2
    elif Size == "medium":
        f5 = 3
    elif Size == "reguler":
        f5 = 4
    else:
        f5 = 5

    Extra_sauce = st.selectbox("Extra Sauce", ("No", "Yes"))
    if Extra_sauce == "No":
        f6 = 0
    else:
        f6 = 1

    Extra_cheese = st.selectbox("Extra Cheese", ("No", "Yes"))
    if Extra_cheese == "No":
        f7 = 0
    else:
        f7 = 1

    if st.button("  Predict  "):
        pre = model.predict([[f1, f2, f3, f4, f5, f6, f7]])
        st.balloons()
        st.success("Pizza Prize = {}".format(round(pre[0], 2)))



main()

