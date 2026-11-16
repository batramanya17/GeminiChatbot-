import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="The Everyday Style Edit",
    page_icon="👗",
    layout="centered",
)

MANUAL = """# Knowledge Summary: The Everyday Style Edit

Based on the uploaded Fashion Styling Guide PDF

## 1. Overview
The Everyday Style Edit is a practical fashion and styling guide designed to help students choose comfortable, fashionable and well-coordinated outfits for different situations.

It focuses on day-wise outfit planning, college and university outfits, rainy-day dressing, low-energy or bad-day outfits, colour combinations, outfit coordination, accessories, footwear, bags and confidence through comfortable dressing.

Main philosophy: Style should feel like you. Fashion should be simple, practical and comfortable rather than complicated.

## 2. Basic fashion styling principles
Use this three-step outfit formula:
1. Base: Choose jeans, trousers, skirts or a kurta.
2. Top: Select a fitted, relaxed or layered top depending on the bottom.
3. Finish: Add clean shoes, a bag and one accessory.

Essential wardrobe pieces:
- Dark-blue wide-leg jeans; black or beige trousers.
- White, cream, black and chocolate tops.
- Relaxed shirts; kurta sets.
- Lightweight cardigans and overshirts.
- Comfortable sneakers and flat sandals; neutral everyday bags.

Easy colour combinations:
- Brown + Cream: elegant.
- Blue Denim + White: classic.
- Sage + Beige: soft and minimal.
- Black + Light Blue: smart casual.
- Chocolate + Denim: trendy.
- Soft Pink + Grey: feminine and subtle.

## 3. Day-wise outfit planning
- Monday: Dark-blue wide-leg jeans + cream/white top + sneakers.
- Tuesday: Straight trousers + relaxed tee or striped shirt.
- Wednesday: Black/beige trousers + brown or pastel top.
- Thursday: Wide-leg jeans + fitted tee + open shirt.
- Friday: Dark denim + dressier top + clean flats.
- Saturday: Comfortable jeans/joggers + breathable tee.
- Sunday: Kurta set, relaxed co-ord or comfortable trousers.

The purpose is to create variety without purchasing new clothes every day.

## 4. College-day styling
College outfits should balance comfort, practicality and appearance.
- Classic campus: Wide-leg denim, plain top, sneakers and backpack.
- Presentation/Viva: Tailored trousers, tucked-in shirt, loafers or flats and watch.
- Long college day: Comfortable jeans, breathable tee, overshirt and cushioned sneakers.
- Events/Fests/Project Expo: Coordinated top and trousers, kurta set or dark jeans with a dressier top.

College styling rules:
- Check the timetable and weather beforehand.
- Wear shoes suitable for walking.
- Keep your bag organised.
- Carry a lightweight layer.
- Choose clothes that allow comfortable movement.

## 5. Rainy-day fashion
Prioritise quick-drying fabrics, easy-to-clean clothing and footwear with good grip.

Recommended looks:
1. Cropped trousers + cotton tee + waterproof jacket + water-resistant sneakers.
2. Dark jeans + tucked tee + rain jacket + secure sandals.
3. Simple kurta + ankle-length pants + quick-dry layer + practical flats.

Wear darker bottoms, shorter hems, breathable tops, lightweight layers, quick-drying fabrics and secure footwear.

Avoid floor-length wide trousers, delicate suede, slippery footwear, very long palazzos and heavy fabrics that remain wet.

Rainy-day essentials: compact umbrella, tissues, waterproof phone pouch, spare hair tie and bag cover.

## 6. Outfits for bad or low-energy days
- No-thinking outfit: Comfortable jeans + plain tee + sneakers + everyday bag.
- Comfort-first outfit: Relaxed trousers + oversized shirt + comfortable flats.
- Quick polished outfit: Black/beige trousers + brown/cream top + watch + neat hair.

Five-minute styling reset:
1. Pick comfortable, clean clothes.
2. Choose one colour family.
3. Brush or tie your hair.
4. Add one accessory.
5. Take your bag and go.

Comfort is also a fashion choice.

## 7. Important styling techniques
- Full tuck: creates a sharper appearance.
- Front tuck: adds relaxed waist definition.
- No tuck: creates an oversized look.
- Open-shirt layering: adds dimension to simple outfits.
- Accessories: add a finishing touch.
- Clean sneakers: make casual outfits look polished.
- Loafers/flats: make trousers look smarter.

Bag styling:
- Backpack: best for busy college days.
- Structured tote: best for presentations and shorter days.

Hairstyle ideas: claw clip, low ponytail, braid or open hair.

## 8. Outfit problem-solving
- Outfit looks oversized: add a front tuck or structured bottom.
- Outfit looks too plain: add a belt, watch or open shirt.
- Outfit looks too dressy: switch to sneakers.
- Weather changes: carry a lightweight layer.

## 9. Weekly outfit preparation
Plan outfits the night before to reduce morning stress:
- Monday: Dark denim + light top.
- Tuesday: Trousers + relaxed shirt.
- Wednesday: Tailored bottom + brown/pastel top.
- Thursday: Denim + tee + overshirt.
- Friday: Dressier top + denim/trousers.
- Saturday: Relaxed casual set.
- Sunday: Kurta/co-ord/comfort look.

## 10. Core knowledge for a Fashion Stylist Chatbot
The chatbot should help with outfit recommendations, day-wise styling, college fashion, weather-based styling, mood-based styling, colour coordination, body-proportion and fit suggestions, accessories, outfit troubleshooting and wardrobe planning.

Final knowledge statement:
Good fashion is not about owning expensive clothes or following every trend. It is about understanding outfit combinations, choosing suitable colours, balancing proportions, dressing according to weather and occasion, and feeling confident in what you wear.

Main objective: Act as a personal everyday fashion stylist that recommends what to wear, how to style it, what to avoid and how to make existing wardrobe pieces look fashionable.
"""

SYSTEM_INSTRUCTION = """
You are The Everyday Style Edit, a friendly, practical personal fashion stylist.
Use the supplied fashion manual as your primary knowledge source.
Give clear, specific outfit suggestions and explain how to style each look,
including footwear, accessories, bags and optional hairstyles when relevant.
Consider occasion, weather, comfort, colour coordination and the user's stated
wardrobe. Encourage reusing existing clothes rather than unnecessary shopping.
If key context is missing, ask one concise follow-up question. Do not assume
the user's body shape, measurements, gender or wardrobe. Give body-proportion
advice respectfully and avoid body-shaming or presenting one body type as ideal.
If a question goes beyond the manual, say so briefly and offer general fashion
guidance without pretending it came from the guide. Keep answers warm and easy
to follow, with practical outfit combinations.
"""

st.title("👗 The Everyday Style Edit")
st.caption("Your personal everyday fashion stylist")
st.write(
    "Ask what to wear for college, rainy days, presentations, low-energy days, "
    "colour combinations, or how to style pieces already in your wardrobe."
)

with st.sidebar:
    st.header("About this stylist")
    st.write(
        "Recommendations are based on the Everyday Style Edit fashion guide. "
        "Tell the chatbot your occasion, weather and available clothing for "
        "more useful suggestions."
    )
    model = st.text_input(
        "Gemini model",
        value=st.secrets.get("GEMINI_MODEL", "gemini-2.5-flash"),
        help="You can change the default model in .streamlit/secrets.toml.",
    )
    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

api_key = st.secrets.get("GEMINI_API_KEY", "")
if not api_key or api_key == "YOUR_GEMINI_API_KEY":
    st.warning(
        "Add your Gemini API key to `.streamlit/secrets.toml` before starting "
        "the app. See README.md for setup instructions."
    )
    st.stop()

try:
    client = genai.Client(api_key=api_key)
except Exception as exc:
    st.error(f"Could not initialise the Gemini client: {exc}")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What should I wear today?")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Build a compact conversation context while keeping the fashion manual available.
    conversation = []
    for item in st.session_state.messages[-12:]:
        conversation.append(f'{item["role"].upper()}: {item["content"]}')

    contents = (
        "FASHION KNOWLEDGE MANUAL:\n"
        + MANUAL
        + "\n\nCONVERSATION:\n"
        + "\n".join(conversation)
        + "\n\nRespond to the latest user message."
    )

    with st.chat_message("assistant"):
        with st.spinner("Putting together your look..."):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=0.7,
                    ),
                )
                answer = response.text or "I couldn't generate a response. Please try again."
            except Exception as exc:
                answer = (
                    "Sorry, I couldn't reach Gemini. Check your API key, model name "
                    f"and internet connection, then try again.\n\nTechnical detail: `{exc}`"
                )
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
