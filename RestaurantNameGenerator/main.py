import streamlit as st
import langchain_helper
import time

# ─── Page configuration ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Restaurant Name Generator",
    page_icon="🍽️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS with brand colors ──────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Space Grotesk', sans-serif;
}

.stApp {
    background: #1A1A1A;
    min-height: 100vh;
    position: relative;
}

.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: 
        radial-gradient(circle at 20% 50%, rgba(0, 255, 255, 0.03) 0%, transparent 50%),
        radial-gradient(circle at 80% 80%, rgba(0, 100, 255, 0.03) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding: 3rem 2rem 4rem;
    max-width: 900px;
    z-index: 1;
    position: relative;
}

/* Hero Section */
.hero-section {
    text-align: center;
    margin-bottom: 2rem;
    animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

@keyframes pulse {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.hero-icon {
    font-size: 3rem;
    margin-bottom: 0.5rem;
    display: inline-block;
    animation: float 3s ease-in-out infinite;
}

.hero-badge {
    display: inline-block;
    background: linear-gradient(135deg, #00FFFF 0%, #0066FF 100%);
    padding: 0.25rem 1rem;
    border-radius: 50px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 1rem;
    color: #1A1A1A;
}

.hero-title {
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF 0%, #00FFFF 50%, #0066FF 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
}

.hero-subtitle {
    font-size: 1rem;
    color: #A0A0A0;
    font-weight: 400;
    max-width: 500px;
    margin: 0 auto;
}

/* Select Box Styling */
.stSelectbox label {
    color: #00FFFF !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    margin-bottom: 0.75rem !important;
}

.stSelectbox [data-baseweb="select"] {
    background: rgba(26, 26, 26, 0.8) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(0, 255, 255, 0.3) !important;
    transition: all 0.3s ease !important;
}

.stSelectbox [data-baseweb="select"]:hover {
    border-color: #00FFFF !important;
    box-shadow: 0 0 0 3px rgba(0, 255, 255, 0.1) !important;
}

.stSelectbox [data-baseweb="select"] > div {
    background: transparent !important;
    color: white !important;
}

/* Button Styling */
.stButton > button {
    background: linear-gradient(135deg, #00FFFF 0%, #0066FF 100%) !important;
    color: #1A1A1A !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    padding: 0.7rem 1.5rem !important;
    border: none !important;
    border-radius: 12px !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    letter-spacing: 0.03em !important;
    text-transform: uppercase !important;
    position: relative !important;
    overflow: hidden !important;
    cursor: pointer !important;
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

.stButton > button:hover::before {
    width: 300px;
    height: 300px;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 25px rgba(0, 255, 255, 0.3) !important;
}

/* Restaurant Name */
.restaurant-name {
    background: linear-gradient(135deg, #FFFFFF 0%, #00FFFF 50%, #0066FF 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 2.5rem;
    font-weight: 800;
    text-align: center;
    margin-bottom: 1.5rem;
    letter-spacing: -0.02em;
    animation: slideIn 0.6s ease-out;
}

/* Menu Items */
.menu-title {
    color: #00FFFF;
    font-size: 1rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 1.25rem;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    border-bottom: 2px solid #00FFFF;
    padding-bottom: 0.5rem;
}

.menu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 0.75rem;
    margin-top: 1rem;
}

.menu-item {
    background: linear-gradient(135deg, rgba(0, 255, 255, 0.1) 0%, rgba(0, 102, 255, 0.05) 100%);
    padding: 0.75rem 1rem;
    border-radius: 10px;
    color: #E0E0E0;
    font-weight: 500;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    text-align: center;
    border: 1px solid rgba(0, 255, 255, 0.2);
    backdrop-filter: blur(5px);
}

.menu-item:hover {
    background: linear-gradient(135deg, rgba(0, 255, 255, 0.2) 0%, rgba(0, 102, 255, 0.15) 100%);
    transform: translateX(5px) translateY(-2px);
    border-color: #00FFFF;
    color: #00FFFF;
}

/* Spinner */
.stSpinner > div {
    border-top-color: #00FFFF !important;
    border-right-color: #0066FF !important;
}

/* Alert */
.stAlert {
    background: rgba(0, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px) !important;
    border-radius: 12px !important;
    color: #00FFFF !important;
    border: 1px solid rgba(0, 255, 255, 0.3) !important;
}

/* Divider */
.custom-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0, 255, 255, 0.3), rgba(0, 102, 255, 0.3), transparent);
    margin: 1.5rem 0;
}

/* Stats Badge */
.stats-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(0, 255, 255, 0.1);
    padding: 0.5rem 1rem;
    border-radius: 50px;
    border: 1px solid rgba(0, 255, 255, 0.3);
    font-size: 0.8rem;
    color: #00FFFF;
    margin-top: 1rem;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 4rem;
    padding-top: 2rem;
    color: #666666;
    font-size: 0.8rem;
    border-top: 1px solid rgba(0, 255, 255, 0.1);
    letter-spacing: 0.05em;
}

.footer span {
    color: #00FFFF;
}

/* Caption styling */
.stCaption {
    color: #666666 !important;
    text-align: center !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Hero Section ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">✨ AI-POWERED GENERATOR</div>
    <div class="hero-icon">🍽️⚡</div>
    <div class="hero-title">Restaurant Name Generator</div>
    <div class="hero-subtitle">Create your perfect culinary brand with AI</div>
</div>
""", unsafe_allow_html=True)

# ─── Main Input Card ───────────────────────────────────────────────────────────────
with st.container():
    
    # Cuisine selector with custom styling
    cuisine = st.selectbox(
        "SELECT CUISINE TYPE",
        ("Nigerian", "Kenyan", "Ghanaian", "South African", "Malian", "Tanzanian", "Italian", "Mexican", "Arabic", "American", "Japanese", "Chinese", "Indian", "French", "Thai", "Spanish", "Mediterranean", "Vegan/Vegetarian", "Ethiopian", "Korean", "Vietnamese", "Caribbean", "Brazilian", "Greek", "Turkish", "Moroccan", "Fusion"),
        help="Choose the culinary direction for your restaurant"
    )
    
    # Generate button
    generate_clicked = st.button("🚀 GENERATE NOW", use_container_width=True)

# ─── Generate and Display Results ───────────────────────────────────────────────────
if generate_clicked and cuisine:
    with st.spinner("Crafting your unique restaurant experience..."):
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)
        
        if response:
            
            # Restaurant Name
            restaurant_name = response['restaurant_name'].strip()
            st.markdown(f'<div class="restaurant-name"> {restaurant_name} </div>', unsafe_allow_html=True)
            
            st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
            
            # Menu Items
            st.markdown('<div class="menu-title">📋 SIGNATURE MENU</div>', unsafe_allow_html=True)
            
            menu_items = response['menu_items'].strip().split(",")
            
            # Display menu items in an interactive grid
            menu_html = '<div class="menu-grid">'
            for idx, item in enumerate(menu_items):
                item = item.strip()
                if item:
                    # Add emoji based on cuisine type
                    emoji = "🍽️"
                    if "Nigerian" in cuisine:
                        emoji = "🍛"
                    elif "Italian" in cuisine:
                        emoji = "🍝"
                    elif "Mexican" in cuisine:
                        emoji = "🌮"
                    elif "Arabic" in cuisine:
                        emoji = "🥙"
                    elif "American" in cuisine:
                        emoji = "🍔"
                    menu_html += f'<div class="menu-item">{emoji} {item}</div>'
            menu_html += '</div>'
            
            st.markdown(menu_html, unsafe_allow_html=True)
            
            # Stats badge
            st.markdown(f"""
            <div class="stats-badge">
                ⚡ {len([x for x in menu_items if x.strip()])} curated menu items
                <span style="color: #0066FF;">•</span>
                🎨 {cuisine} cuisine
            </div>
            """, unsafe_allow_html=True)
            
elif generate_clicked and not cuisine:
    st.warning("⚠️ Please select a cuisine type to generate your restaurant name and menu.")

# ─── Footer ─────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <span>⚡ Powered by Chibuike Dominion</span> | <span>Built as my personal project</span> | <span>🍽️ Create your culinary identity</span>
</div>
""", unsafe_allow_html=True)
