"""Sash design system: colors, typography, and shared styles."""

# Color palette
COLOR_PRIMARY = "#4F46E5"  # Indigo 600
COLOR_PRIMARY_LIGHT = "#818CF8"  # Indigo 400
COLOR_PRIMARY_DARK = "#3730A3"  # Indigo 800

COLOR_SECONDARY = "#0EA5E9"  # Sky 500
COLOR_SECONDARY_LIGHT = "#38BDF8"  # Sky 400

COLOR_SUCCESS = "#10B981"  # Emerald 500
COLOR_WARNING = "#F59E0B"  # Amber 500
COLOR_ERROR = "#EF4444"  # Red 500
COLOR_INFO = "#3B82F6"  # Blue 500

COLOR_BACKGROUND = "#F9FAFB"  # Gray 50
COLOR_SURFACE = "#FFFFFF"  # White
COLOR_BORDER = "#E5E7EB"  # Gray 200
COLOR_TEXT = "#1F2937"  # Gray 800
COLOR_TEXT_MUTED = "#6B7280"  # Gray 500

# Typography
FONT_FAMILY = (
    "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
)
FONT_MONO = "'JetBrains Mono', 'Fira Code', monospace"

# Spacing
SPACING_XS = "0.25rem"
SPACING_SM = "0.5rem"
SPACING_MD = "1rem"
SPACING_LG = "1.5rem"
SPACING_XL = "2rem"

# Border radius
RADIUS_SM = "0.25rem"
RADIUS_MD = "0.5rem"
RADIUS_LG = "0.75rem"
RADIUS_FULL = "9999px"

# Shadows
SHADOW_SM = "0 1px 2px 0 rgb(0 0 0 / 0.05)"
SHADOW_MD = "0 4px 6px -1px rgb(0 0 0 / 0.1)"
SHADOW_LG = "0 10px 15px -3px rgb(0 0 0 / 0.1)"


def get_custom_css() -> str:
    """Return custom CSS for Sash design system."""
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap');
    
    /* Global styles */
    .stApp {{
        background-color: {COLOR_BACKGROUND};
        font-family: {FONT_FAMILY};
    }}
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {{
        font-family: {FONT_FAMILY};
        color: {COLOR_TEXT};
        font-weight: 600;
    }}
    
    /* Cards and surfaces */
    .sash-card {{
        background-color: {COLOR_SURFACE};
        border: 1px solid {COLOR_BORDER};
        border-radius: {RADIUS_LG};
        padding: {SPACING_LG};
        box-shadow: {SHADOW_SM};
        margin-bottom: {SPACING_MD};
    }}
    
    /* Status badges */
    .status-badge {{
        display: inline-block;
        padding: {SPACING_XS} {SPACING_SM};
        border-radius: {RADIUS_FULL};
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.025em;
    }}
    
    .status-success {{
        background-color: #D1FAE5;
        color: {COLOR_SUCCESS};
    }}
    
    .status-warning {{
        background-color: #FEF3C7;
        color: {COLOR_WARNING};
    }}
    
    .status-error {{
        background-color: #FEE2E2;
        color: {COLOR_ERROR};
    }}
    
    .status-info {{
        background-color: #DBEAFE;
        color: {COLOR_INFO};
    }}
    
    /* Buttons */
    .stButton > button {{
        border-radius: {RADIUS_MD};
        font-weight: 500;
        transition: all 0.2s ease;
    }}
    
    /* Metric cards */
    .metric-card {{
        background: linear-gradient(135deg, {COLOR_PRIMARY} 0%, {COLOR_PRIMARY_DARK} 100%);
        color: white;
        padding: {SPACING_LG};
        border-radius: {RADIUS_LG};
        box-shadow: {SHADOW_MD};
    }}
    
    .metric-value {{
        font-size: 2.5rem;
        font-weight: 700;
        line-height: 1;
    }}
    
    .metric-label {{
        font-size: 0.875rem;
        opacity: 0.9;
        margin-top: {SPACING_SM};
    }}
    
    /* Code blocks */
    .stCode {{
        border-radius: {RADIUS_MD};
        font-family: {FONT_MONO};
    }}
    
    /* Sidebar */
    .css-1d391kg {{
        background-color: {COLOR_SURFACE};
        border-right: 1px solid {COLOR_BORDER};
    }}
    
    /* Loading state */
    .loading-placeholder {{
        background: linear-gradient(90deg, {COLOR_BORDER} 25%, {COLOR_BACKGROUND} 50%, {COLOR_BORDER} 75%);
        background-size: 200% 100%;
        animation: loading 1.5s infinite;
        border-radius: {RADIUS_MD};
        height: 100px;
    }}
    
    @keyframes loading {{
        0% {{ background-position: 200% 0; }}
        100% {{ background-position: -200% 0; }}
    }}
    
    /* Empty state */
    .empty-state {{
        text-align: center;
        padding: {SPACING_XL};
        color: {COLOR_TEXT_MUTED};
    }}
    
    .empty-state-icon {{
        font-size: 3rem;
        margin-bottom: {SPACING_MD};
    }}
    
    /* Responsive grid */
    .responsive-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: {SPACING_LG};
    }}
    </style>
    """
