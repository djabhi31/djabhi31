import os
from PIL import Image, ImageEnhance
import xml.etree.ElementTree as ET

def generate_svgs():
    avatar_path = 'avatar.png'
    if not os.path.exists(avatar_path):
        raise FileNotFoundError(f"Avatar file not found at {avatar_path}")
        
    img = Image.open(avatar_path).convert('L')
    tw, th = 48, 28
    # Crop to head & upper chest
    img_crop = img.crop((35, 15, 425, 445))
    img_resized = img_crop.resize((tw, th), Image.Resampling.LANCZOS)
    enhancer = ImageEnhance.Contrast(img_resized)
    img_enhanced = enhancer.enhance(1.45)

    def map_pixel(val):
        if val > 195:
            return ' '
        elif val > 165:
            return '.'
        elif val > 135:
            return ':'
        elif val > 105:
            return '+'
        elif val > 75:
            return '*'
        elif val > 45:
            return '#'
        elif val > 20:
            return '%'
        else:
            return '@'

    start_y = 132
    dy = 8.2
    tspan_dark_lines = []
    tspan_light_lines = []

    for i in range(th):
        line = ''
        for x in range(tw):
            p = img_enhanced.getpixel((x, i))
            line += map_pixel(p)
        line_esc = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        y_pos = start_y + i * dy
        tspan_dark_lines.append(f'        <tspan x="250" y="{y_pos:.1f}">{line_esc}</tspan>')
        tspan_light_lines.append(f'        <tspan x="250" y="{y_pos:.1f}">{line_esc}</tspan>')

    tspans_dark_str = '\n'.join(tspan_dark_lines)
    tspans_light_str = '\n'.join(tspan_light_lines)

    # Generate 24 animated Equalizer bars
    eq_dark_bars = []
    eq_light_bars = []
    base_x = 61
    base_y = 438

    # Preset natural audio wave patterns for 24 bars
    patterns = [
        # bass
        [4, 22, 10, 26, 8, 4, 0.75],
        [6, 26, 14, 28, 10, 6, 0.85],
        [8, 28, 16, 26, 12, 8, 0.70],
        [4, 24, 8, 28, 14, 4, 0.90],
        [10, 28, 12, 26, 8, 10, 0.80],
        [6, 26, 14, 28, 10, 6, 0.65],
        [8, 24, 16, 22, 12, 8, 0.75],
        [4, 20, 10, 26, 8, 4, 0.85],
        # mids
        [8, 24, 12, 26, 10, 8, 0.60],
        [10, 26, 14, 24, 8, 10, 0.70],
        [6, 22, 10, 28, 14, 6, 0.55],
        [12, 28, 16, 24, 10, 12, 0.65],
        [8, 26, 12, 28, 8, 8, 0.75],
        [10, 24, 14, 22, 10, 10, 0.60],
        [6, 20, 8, 26, 12, 6, 0.70],
        [8, 26, 14, 22, 8, 8, 0.55],
        # highs
        [4, 18, 8, 22, 10, 4, 0.50],
        [6, 20, 10, 18, 6, 6, 0.60],
        [4, 16, 8, 22, 8, 4, 0.45],
        [6, 22, 12, 18, 10, 6, 0.55],
        [4, 18, 6, 20, 8, 4, 0.48],
        [6, 16, 10, 14, 6, 6, 0.52],
        [4, 14, 6, 18, 8, 4, 0.42],
        [4, 12, 6, 16, 8, 4, 0.46]
    ]

    for idx, p in enumerate(patterns):
        bx = base_x + idx * 16
        h_vals = f"{p[0]};{p[1]};{p[2]};{p[3]};{p[4]};{p[0]}"
        y_vals = f"{base_y - p[0]};{base_y - p[1]};{base_y - p[2]};{base_y - p[3]};{base_y - p[4]};{base_y - p[0]}"
        dur = f"{p[5]:.2f}s"
        
        # Dark bar
        bar_d = f'''        <rect x="{bx}" y="{base_y - p[0]}" width="10" height="{p[0]}" rx="3" fill="url(#eqGradDark)">
          <animate attributeName="height" values="{h_vals}" dur="{dur}" repeatCount="indefinite"/>
          <animate attributeName="y" values="{y_vals}" dur="{dur}" repeatCount="indefinite"/>
        </rect>'''
        eq_dark_bars.append(bar_d)

        # Light bar
        bar_l = f'''        <rect x="{bx}" y="{base_y - p[0]}" width="10" height="{p[0]}" rx="3" fill="url(#eqGradLight)">
          <animate attributeName="height" values="{h_vals}" dur="{dur}" repeatCount="indefinite"/>
          <animate attributeName="y" values="{y_vals}" dur="{dur}" repeatCount="indefinite"/>
        </rect>'''
        eq_light_bars.append(bar_l)

    eq_dark_str = '\n'.join(eq_dark_bars)
    eq_light_str = '\n'.join(eq_light_bars)

    # 2. Build enhanced dark.svg
    dark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610" role="img" aria-label="Abhilash Ghosh (@djabhi31) - Full-Stack Engineer, 3D Web &amp; Creative Technologist">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="bgGlow1" cx="18%" cy="15%" r="65%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#030712" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlow2" cx="85%" cy="85%" r="60%">
      <stop offset="0%" stop-color="#7C3AED" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#030712" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlow3" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#059669" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#030712" stop-opacity="0"/>
    </radialGradient>

    <!-- Accent Linear Gradients -->
    <linearGradient id="neonCyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#22D3EE"/>
      <stop offset="100%" stop-color="#06B6D4"/>
    </linearGradient>
    <linearGradient id="neonViolet" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C084FC"/>
      <stop offset="50%" stop-color="#A855F7"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>
    <linearGradient id="neonGreen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34D399"/>
      <stop offset="100%" stop-color="#10B981"/>
    </linearGradient>
    
    <!-- Laser Border Beam Gradient -->
    <linearGradient id="laserBeam" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22D3EE"/>
      <stop offset="35%" stop-color="#818CF8"/>
      <stop offset="70%" stop-color="#C084FC"/>
      <stop offset="100%" stop-color="#34D399"/>
    </linearGradient>

    <!-- Base Frame Border Gradient -->
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#818CF8" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#C084FC" stop-opacity="0.40"/>
    </linearGradient>
    <linearGradient id="cardBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.65"/>
    </linearGradient>

    <!-- Scanline Laser Gradient -->
    <linearGradient id="scanlineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0"/>
      <stop offset="50%" stop-color="#22D3EE" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0"/>
    </linearGradient>

    <!-- Audio Equalizer Gradient -->
    <linearGradient id="eqGradDark" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#06B6D4"/>
      <stop offset="45%" stop-color="#3B82F6"/>
      <stop offset="75%" stop-color="#A855F7"/>
      <stop offset="100%" stop-color="#F43F5E"/>
    </linearGradient>

    <!-- Telemetry Meter Gradients -->
    <linearGradient id="cyanMeter" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#22D3EE"/>
    </linearGradient>
    <linearGradient id="violetMeter" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#C084FC"/>
    </linearGradient>
    <linearGradient id="greenMeter" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#34D399"/>
    </linearGradient>

    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#818CF8"/>
      <stop offset="100%" stop-color="#C084FC"/>
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="gridPattern" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#334155" stroke-width="0.75" stroke-opacity="0.24"/>
    </pattern>
  </defs>

  <style>
    .mono {{ font-family: ui-monospace, SFMono-Regular, "Liberation Mono", Menlo, Consolas, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }}
    .ascii {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 7.5px; font-weight: 700; letter-spacing: 0.8px; fill: #38BDF8; }}
  </style>

  <!-- Root Canvas Background -->
  <rect width="1180" height="610" rx="22" fill="#030712"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlow1)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlow2)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlow3)"/>
  <rect width="1180" height="610" rx="22" fill="url(#gridPattern)"/>

  <!-- Outer Glass Frame Base Border -->
  <rect x="2" y="2" width="1176" height="606" rx="21" fill="none" stroke="url(#borderGrad)" stroke-width="1.5"/>

  <!-- ==================== ANIMATION 1: LASER BORDER SHIMMER ==================== -->
  <rect x="2" y="2" width="1176" height="606" rx="21" fill="none" stroke="url(#laserBeam)" stroke-width="2.5" stroke-dasharray="160 580">
    <animate attributeName="stroke-dashoffset" values="0;-740" dur="4.5s" repeatCount="indefinite"/>
  </rect>

  <!-- ==================== LEFT COLUMN: VISUAL / IDENTITY ==================== -->
  <g id="left-column">
    <!-- Left Card Background -->
    <rect x="28" y="28" width="444" height="554" rx="16" fill="#0B1220" fill-opacity="0.84" stroke="url(#cardBorder)" stroke-width="1.2"/>

    <!-- Terminal Window Bar -->
    <circle cx="50" cy="52" r="5" fill="#EF4444"/>
    <circle cx="66" cy="52" r="5" fill="#F59E0B"/>
    <circle cx="82" cy="52" r="5" fill="#10B981"/>
    <text x="104" y="56" class="mono" font-size="11.5" fill="#94A3B8" font-weight="500">djabhi31@developer:~ (terminal.hud)</text>
    
    <!-- Status Pill -->
    <rect x="364" y="42" width="92" height="20" rx="10" fill="#10B981" fill-opacity="0.12" stroke="#10B981" stroke-width="1"/>
    <circle cx="376" cy="52" r="3.5" fill="#10B981">
      <animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="386" y="56" class="mono" font-size="10" fill="#34D399" font-weight="600">ONLINE</text>

    <!-- Header Divider -->
    <line x1="28" y1="74" x2="472" y2="74" stroke="#1E293B" stroke-width="1"/>

    <!-- Biometric ID Header -->
    <text x="44" y="93" class="mono" font-size="10" fill="#38BDF8" font-weight="600" letter-spacing="1">VISUAL.MAP // BIOMETRIC-ID</text>
    <text x="456" y="93" text-anchor="end" class="mono" font-size="9" fill="#10B981" font-weight="600">● TARGET LOCK: 99.4%</text>

    <!-- ASCII Portrait Container Box -->
    <rect x="42" y="104" width="416" height="258" rx="10" fill="#040914" fill-opacity="0.94" stroke="#1E293B" stroke-width="1"/>

    <!-- ==================== ANIMATION 2: HUD RETICLE & CROSSHAIRS ==================== -->
    <path d="M 50 118 L 50 112 L 56 112" stroke="#22D3EE" stroke-width="1.8" fill="none"/>
    <path d="M 450 118 L 450 112 L 444 112" stroke="#22D3EE" stroke-width="1.8" fill="none"/>
    <path d="M 50 348 L 50 354 L 56 354" stroke="#22D3EE" stroke-width="1.8" fill="none"/>
    <path d="M 450 348 L 450 354 L 444 354" stroke="#22D3EE" stroke-width="1.8" fill="none"/>

    <!-- HUD Telemetry Tags on Portrait -->
    <text x="56" y="124" class="mono" font-size="8" fill="#38BDF8" opacity="0.9">[COORDS: 22.57°N, 88.36°E]</text>
    <text x="444" y="124" text-anchor="end" class="mono" font-size="8" fill="#A855F7" opacity="0.9">CALCUTTA UNIV</text>

    <!-- ASCII Character Stream -->
    <text class="ascii" text-anchor="middle">
{tspans_dark_str}
    </text>

    <!-- ==================== ANIMATION 3: HOLOGRAM SCANLINE SWEEP ==================== -->
    <line x1="43" y1="106" x2="457" y2="106" stroke="url(#scanlineGrad)" stroke-width="2.5" opacity="0.85">
      <animate attributeName="y1" values="106;358;106" dur="4.5s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="106;358;106" dur="4.5s" repeatCount="indefinite"/>
    </line>

    <!-- Subtle Glitch / Signal Flicker Box Overlay -->
    <rect x="42" y="104" width="416" height="258" rx="10" fill="#22D3EE" opacity="0">
      <animate attributeName="opacity" values="0;0.05;0;0.03;0;0;0.06;0" keyTimes="0;0.12;0.14;0.45;0.47;0.82;0.84;1" dur="6s" repeatCount="indefinite"/>
    </rect>

    <!-- ==================== ANIMATION 4: BOUNCING AUDIO EQUALIZER (DJ ABHI) ==================== -->
    <g id="audio-equalizer">
      <rect x="42" y="372" width="416" height="74" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
      <circle cx="56" cy="386" r="3.5" fill="#F43F5E">
        <animate attributeName="opacity" values="1;0.4;1" dur="1s" repeatCount="indefinite"/>
      </circle>
      <text x="66" y="390" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="600">AUDIO.ENGINE // DJ ABHI SPECTRUM</text>
      <text x="444" y="390" text-anchor="end" class="mono" font-size="8.5" fill="#22D3EE" font-weight="600">140 BPM [STEREO]</text>

      <!-- 24 Bouncing Equalizer Bars -->
{eq_dark_str}
    </g>

    <!-- Terminal Command Line Prompt -->
    <rect x="42" y="456" width="416" height="74" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
    <text x="56" y="475" class="mono" font-size="10.5" fill="#38BDF8" font-weight="600">~/profile $ <tspan fill="#F8FAFC">./launch --sound --systems</tspan></text>
    <text x="56" y="494" class="mono" font-size="9.5" fill="#94A3B8">[OK] 3D_WEBGL: 60FPS · TELEMETRY: REAL-TIME</text>
    <text x="56" y="512" class="mono" font-size="9.5" fill="#94A3B8">[OK] AUDIO_BASS: ONLINE · COMMUNITY: 38K+</text>
    <rect x="345" y="501" width="7" height="13" fill="#38BDF8">
      <animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite"/>
    </rect>

    <!-- Quick Meta Pill -->
    <text x="250" y="555" text-anchor="middle" class="mono" font-size="9" fill="#475569" letter-spacing="1.2">ABHILASH GHOSH // SYSTEM BIO-IDENTITY CORE</text>
  </g>

  <!-- ==================== RIGHT COLUMN: SYSTEM.INFO ==================== -->
  <g id="right-column">
    <!-- Right Card Background -->
    <rect x="490" y="28" width="662" height="554" rx="16" fill="#0B1220" fill-opacity="0.84" stroke="url(#cardBorder)" stroke-width="1.2"/>

    <!-- Terminal Bar -->
    <circle cx="512" cy="52" r="5" fill="#EF4444"/>
    <circle cx="528" cy="52" r="5" fill="#F59E0B"/>
    <circle cx="544" cy="52" r="5" fill="#10B981"/>
    <text x="564" y="56" class="mono" font-size="11.5" fill="#94A3B8" font-weight="500">SYSTEM.INFO // EXECUTIVE_CORE</text>
    <rect x="1038" y="42" width="98" height="20" rx="10" fill="#38BDF8" fill-opacity="0.12" stroke="#38BDF8" stroke-width="1"/>
    <text x="1087" y="56" text-anchor="middle" class="mono" font-size="9.5" fill="#38BDF8" font-weight="600">RELEASE v4.2</text>

    <!-- Header Divider -->
    <line x1="490" y1="74" x2="1152" y2="74" stroke="#1E293B" stroke-width="1"/>

    <!-- 1. Identity & Animated Role Section -->
    <g transform="translate(510, 88)">
      <text x="0" y="14" class="mono" font-size="10.5" fill="#38BDF8" font-weight="600">djabhi31@station:~$ whoami</text>
      
      <!-- Name -->
      <text x="0" y="44" class="sans" font-size="25" font-weight="800" fill="url(#textGrad)" letter-spacing="0.5">ABHILASH GHOSH</text>
      <text x="250" y="42" class="mono" font-size="13" fill="#64748B">(@djabhi31)</text>

      <!-- Animated Rotating Role (4 states cycling smoothly every 16s) -->
      <g transform="translate(0, 68)">
        <text class="mono" font-size="13" font-weight="600" fill="#22D3EE">
          <tspan>&gt; ROLE: </tspan>
        </text>

        <!-- Role 1: 0s-4s -->
        <text x="68" y="0" class="mono" font-size="13" font-weight="600" fill="#F8FAFC" opacity="0">
          Full-Stack &amp; 3D Web Engineer <tspan fill="#38BDF8">▋</tspan>
          <animate attributeName="opacity" values="1;1;0;0;0;0;0;1" keyTimes="0;0.22;0.25;0.5;0.75;0.97;0.99;1" dur="16s" repeatCount="indefinite"/>
        </text>

        <!-- Role 2: 4s-8s -->
        <text x="68" y="0" class="mono" font-size="13" font-weight="600" fill="#A855F7" opacity="0">
          Creative Technologist &amp; Music Producer <tspan fill="#A855F7">▋</tspan>
          <animate attributeName="opacity" values="0;0;1;1;0;0;0;0" keyTimes="0;0.23;0.26;0.47;0.5;0.75;0.97;1" dur="16s" repeatCount="indefinite"/>
        </text>

        <!-- Role 3: 8s-12s -->
        <text x="68" y="0" class="mono" font-size="13" font-weight="600" fill="#34D399" opacity="0">
          Founder of Mermaidz Records &amp; ExcuseVerse <tspan fill="#34D399">▋</tspan>
          <animate attributeName="opacity" values="0;0;0;0;1;1;0;0" keyTimes="0;0.48;0.51;0.72;0.75;0.9;0.97;1" dur="16s" repeatCount="indefinite"/>
        </text>

        <!-- Role 4: 12s-16s -->
        <text x="68" y="0" class="mono" font-size="13" font-weight="600" fill="#38BDF8" opacity="0">
          Geospatial &amp; Real-Time Systems Architect <tspan fill="#38BDF8">▋</tspan>
          <animate attributeName="opacity" values="0;0;0;0;0;0;1;1" keyTimes="0;0.48;0.5;0.73;0.76;0.96;0.98;1" dur="16s" repeatCount="indefinite"/>
        </text>
      </g>

      <!-- Identity Pills -->
      <g transform="translate(0, 84)">
        <rect x="0" y="0" width="144" height="22" rx="11" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <text x="72" y="15" text-anchor="middle" class="mono" font-size="9.5" fill="#94A3B8">📍 Kolkata, India</text>

        <rect x="152" y="0" width="168" height="22" rx="11" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <text x="236" y="15" text-anchor="middle" class="mono" font-size="9.5" fill="#A855F7">🎧 DJ ABHI-Maheshtala</text>

        <rect x="328" y="0" width="154" height="22" rx="11" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <text x="405" y="15" text-anchor="middle" class="mono" font-size="9.5" fill="#38BDF8">🎓 M.Com (Calcutta Univ)</text>

        <rect x="490" y="0" width="132" height="22" rx="11" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <text x="556" y="15" text-anchor="middle" class="mono" font-size="9.5" fill="#34D399">⚡ 38K+ YouTube</text>
      </g>
    </g>

    <!-- 2. Featured Projects Grid (2x2) -->
    <g transform="translate(510, 202)">
      <text x="0" y="0" class="mono" font-size="10" fill="#38BDF8" font-weight="600" letter-spacing="1">// PRODUCTION BUILDS &amp; PLATFORMS</text>
      
      <!-- Project 1: EarthSphere -->
      <g transform="translate(0, 8)">
        <rect x="0" y="0" width="304" height="52" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="16" cy="17" r="4" fill="#38BDF8">
          <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
        </circle>
        <text x="28" y="20" class="sans" font-size="11.5" font-weight="700" fill="#F8FAFC">EarthSphere</text>
        <rect x="110" y="9" width="58" height="14" rx="7" fill="#0284C7" fill-opacity="0.25"/>
        <text x="139" y="19" text-anchor="middle" class="mono" font-size="7.5" fill="#38BDF8" font-weight="600">LIVE PROD</text>
        <text x="14" y="34" class="sans" font-size="9" fill="#94A3B8">Real-time planetary event intelligence via NASA EONET</text>
        <text x="14" y="45" class="mono" font-size="8" fill="#38BDF8">Next.js 15 · Three.js · WebGL · MapLibre GL</text>
      </g>

      <!-- Project 2: God's Eye View -->
      <g transform="translate(318, 8)">
        <rect x="0" y="0" width="304" height="52" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="16" cy="17" r="4" fill="#A855F7">
          <animate attributeName="opacity" values="1;0.4;1" dur="2.3s" repeatCount="indefinite"/>
        </circle>
        <text x="28" y="20" class="sans" font-size="11.5" font-weight="700" fill="#F8FAFC">God's Eye View</text>
        <rect x="130" y="9" width="62" height="14" rx="7" fill="#7C3AED" fill-opacity="0.25"/>
        <text x="161" y="19" text-anchor="middle" class="mono" font-size="7.5" fill="#C084FC" font-weight="600">AZURE CLOUD</text>
        <text x="14" y="34" class="sans" font-size="9" fill="#94A3B8">Real-time 3D planetary intelligence console</text>
        <text x="14" y="45" class="mono" font-size="8" fill="#A855F7">Microsoft Azure · WebGL · 3D Engine · Cloud</text>
      </g>

      <!-- Project 3: ExcuseVerse -->
      <g transform="translate(0, 66)">
        <rect x="0" y="0" width="304" height="52" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="16" cy="17" r="4" fill="#F59E0B">
          <animate attributeName="opacity" values="1;0.4;1" dur="1.8s" repeatCount="indefinite"/>
        </circle>
        <text x="28" y="20" class="sans" font-size="11.5" font-weight="700" fill="#F8FAFC">ExcuseVerse</text>
        <rect x="110" y="9" width="54" height="14" rx="7" fill="#D97706" fill-opacity="0.25"/>
        <text x="137" y="19" text-anchor="middle" class="mono" font-size="7.5" fill="#FBBF24" font-weight="600">AI APP</text>
        <text x="14" y="34" class="sans" font-size="9" fill="#94A3B8">AI situational generator with 2,500+ dynamic excuses</text>
        <text x="14" y="45" class="mono" font-size="8" fill="#FBBF24">AI Integration · Next.js · Multi-Lingual UX</text>
      </g>

      <!-- Project 4: Mermaidz Records -->
      <g transform="translate(318, 66)">
        <rect x="0" y="0" width="304" height="52" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="16" cy="17" r="4" fill="#10B981">
          <animate attributeName="opacity" values="1;0.4;1" dur="2.1s" repeatCount="indefinite"/>
        </circle>
        <text x="28" y="20" class="sans" font-size="11.5" font-weight="700" fill="#F8FAFC">Mermaidz Records</text>
        <rect x="144" y="9" width="56" height="14" rx="7" fill="#059669" fill-opacity="0.25"/>
        <text x="172" y="19" text-anchor="middle" class="mono" font-size="7.5" fill="#34D399" font-weight="600">LABEL</text>
        <text x="14" y="34" class="sans" font-size="9" fill="#94A3B8">Music publishing &amp; distribution brand for indie artists</text>
        <text x="14" y="45" class="mono" font-size="8" fill="#34D399">150+ Global Stores · Royalties &amp; Rights</text>
      </g>
    </g>

    <!-- ==================== ANIMATION 5: SYSTEM TELEMETRY WORKLOAD METERS ==================== -->
    <g transform="translate(510, 332)">
      <text x="0" y="0" class="mono" font-size="10" fill="#38BDF8" font-weight="600" letter-spacing="1">// SYSTEM TELEMETRY &amp; WORKLOADS</text>
      
      <!-- Meter 1: 3D WebGL Engine -->
      <g transform="translate(0, 10)">
        <text x="0" y="0" class="mono" font-size="8.5" fill="#94A3B8">3D WebGL Engine &amp; Shaders (Three.js)</text>
        <text x="622" y="0" text-anchor="end" class="mono" font-size="8.5" fill="#22D3EE" font-weight="600">60 FPS // GPU 95%</text>
        <rect x="0" y="5" width="622" height="6" rx="3" fill="#070D1A" stroke="#1E293B" stroke-width="0.75"/>
        <rect x="0" y="5" width="580" height="6" rx="3" fill="url(#cyanMeter)">
          <animate attributeName="width" values="460;590;530;590" dur="3.5s" repeatCount="indefinite"/>
        </rect>
      </g>

      <!-- Meter 2: NASA EONET Radar -->
      <g transform="translate(0, 32)">
        <text x="0" y="0" class="mono" font-size="8.5" fill="#94A3B8">NASA EONET Real-Time Planetary Radar</text>
        <text x="622" y="0" text-anchor="end" class="mono" font-size="8.5" fill="#C084FC" font-weight="600">SYNC: 100% // 24H STREAM</text>
        <rect x="0" y="5" width="622" height="6" rx="3" fill="#070D1A" stroke="#1E293B" stroke-width="0.75"/>
        <rect x="0" y="5" width="520" height="6" rx="3" fill="url(#violetMeter)">
          <animate attributeName="width" values="360;530;440;530" dur="4.2s" repeatCount="indefinite"/>
        </rect>
      </g>

      <!-- Meter 3: Audio Workstation -->
      <g transform="translate(0, 54)">
        <text x="0" y="0" class="mono" font-size="8.5" fill="#94A3B8">Audio Workstation // Bass &amp; EDM Master (FL Studio)</text>
        <text x="622" y="0" text-anchor="end" class="mono" font-size="8.5" fill="#34D399" font-weight="600">140 BPM // MASTERED</text>
        <rect x="0" y="5" width="622" height="6" rx="3" fill="#070D1A" stroke="#1E293B" stroke-width="0.75"/>
        <rect x="0" y="5" width="560" height="6" rx="3" fill="url(#greenMeter)">
          <animate attributeName="width" values="410;575;490;575" dur="2.8s" repeatCount="indefinite"/>
        </rect>
      </g>
    </g>

    <!-- 4. Technical Stack Pills Grid -->
    <g transform="translate(510, 412)">
      <text x="0" y="0" class="mono" font-size="10" fill="#38BDF8" font-weight="600" letter-spacing="1">// TECHNICAL ARSENAL &amp; CORE STACK</text>
      
      <!-- Row 1 -->
      <g transform="translate(0, 8)">
        <!-- Next.js 15 -->
        <rect x="0" y="0" width="98" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="10" cy="11" r="3" fill="#38BDF8"/>
        <text x="20" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">Next.js 15</text>

        <!-- React 19 -->
        <rect x="105" y="0" width="96" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="115" cy="11" r="3" fill="#22D3EE"/>
        <text x="125" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">React 19</text>

        <!-- Three.js -->
        <rect x="208" y="0" width="94" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="218" cy="11" r="3" fill="#A855F7"/>
        <text x="228" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">Three.js</text>

        <!-- WebGL -->
        <rect x="309" y="0" width="86" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="319" cy="11" r="3" fill="#EC4899"/>
        <text x="329" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">WebGL</text>

        <!-- TypeScript -->
        <rect x="402" y="0" width="104" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="412" cy="11" r="3" fill="#3B82F6"/>
        <text x="422" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">TypeScript</text>

        <!-- Python -->
        <rect x="513" y="0" width="88" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="523" cy="11" r="3" fill="#EAB308"/>
        <text x="533" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">Python</text>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 36)">
        <!-- TailwindCSS -->
        <rect x="0" y="0" width="112" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="10" cy="11" r="3" fill="#06B6D4"/>
        <text x="20" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">TailwindCSS</text>

        <!-- Azure -->
        <rect x="119" y="0" width="118" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="129" cy="11" r="3" fill="#0284C7"/>
        <text x="139" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">Microsoft Azure</text>

        <!-- MapLibre GL -->
        <rect x="244" y="0" width="112" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="254" cy="11" r="3" fill="#10B981"/>
        <text x="264" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">MapLibre GL</text>

        <!-- GitHub Actions -->
        <rect x="363" y="0" width="124" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="373" cy="11" r="3" fill="#818CF8"/>
        <text x="383" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">GitHub Actions</text>

        <!-- FL Studio -->
        <rect x="494" y="0" width="106" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="504" cy="11" r="3" fill="#F97316"/>
        <text x="514" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">FL Studio</text>
      </g>
    </g>

    <!-- 5. Terminal Connect & Footer Bar -->
    <g transform="translate(510, 482)">
      <rect x="0" y="0" width="622" height="62" rx="10" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
      <circle cx="18" cy="18" r="3" fill="#38BDF8"/>
      <text x="28" y="21" class="mono" font-size="10" fill="#38BDF8" font-weight="600">&gt; ECOSYSTEM &amp; CONNECT MATRIX</text>
      
      <text x="28" y="38" class="mono" font-size="9" fill="#F8FAFC">
        <tspan fill="#64748B">WEB:</tspan> abhilashghosh.pages.dev <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">YT:</tspan> @djabhimaheshtala (38K+) <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">SPOTIFY:</tspan> DJ ABHI
      </text>
      
      <text x="28" y="52" class="mono" font-size="9" fill="#F8FAFC">
        <tspan fill="#64748B">GH:</tspan> github.com/djabhi31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">X:</tspan> @DjAbhi31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">IG:</tspan> @djabhi.31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">MAIL:</tspan> abhilashghosh31@gmail.com
      </text>
    </g>

    <!-- Bottom Meta Tagline -->
    <text x="821" y="562" text-anchor="middle" class="mono" font-size="8.5" fill="#475569" letter-spacing="1.2">SYSTEM STATUS: FULLY OPERATIONAL // KERNEL RUNNING</text>
  </g>
</svg>'''

    # 3. Build enhanced light.svg
    light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610" role="img" aria-label="Abhilash Ghosh (@djabhi31) - Full-Stack Engineer, 3D Web &amp; Creative Technologist">
  <defs>
    <!-- Background Gradients (Light) -->
    <radialGradient id="bgGlowLight1" cx="18%" cy="15%" r="65%">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#F8FAFC" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlowLight2" cx="85%" cy="85%" r="60%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="#F8FAFC" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlowLight3" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="#F8FAFC" stop-opacity="0"/>
    </radialGradient>

    <!-- Accent Linear Gradients -->
    <linearGradient id="laserBeamLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="35%" stop-color="#4F46E5"/>
      <stop offset="70%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>

    <linearGradient id="borderGradLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB" stop-opacity="0.35"/>
      <stop offset="50%" stop-color="#6366F1" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#9333EA" stop-opacity="0.3"/>
    </linearGradient>
    <linearGradient id="cardBorderLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#CBD5E1"/>
      <stop offset="100%" stop-color="#E2E8F0"/>
    </linearGradient>

    <!-- Scanline Laser Gradient (Light) -->
    <linearGradient id="scanlineGradLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563EB" stop-opacity="0"/>
      <stop offset="50%" stop-color="#2563EB" stop-opacity="0.65"/>
      <stop offset="100%" stop-color="#2563EB" stop-opacity="0"/>
    </linearGradient>

    <!-- Audio Equalizer Gradient (Light) -->
    <linearGradient id="eqGradLight" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="50%" stop-color="#2563EB"/>
      <stop offset="80%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#E11D48"/>
    </linearGradient>

    <!-- Telemetry Meter Gradients (Light) -->
    <linearGradient id="blueMeterLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1D4ED8"/>
      <stop offset="100%" stop-color="#3B82F6"/>
    </linearGradient>
    <linearGradient id="violetMeterLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6D28D9"/>
      <stop offset="100%" stop-color="#A855F7"/>
    </linearGradient>
    <linearGradient id="greenMeterLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#047857"/>
      <stop offset="100%" stop-color="#10B981"/>
    </linearGradient>

    <linearGradient id="textGradLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="50%" stop-color="#4338CA"/>
      <stop offset="100%" stop-color="#6B21A8"/>
    </linearGradient>

    <!-- Grid Pattern (Light) -->
    <pattern id="gridPatternLight" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#94A3B8" stroke-width="0.75" stroke-opacity="0.22"/>
    </pattern>

    <!-- Card Shadow -->
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <style>
    .mono {{ font-family: ui-monospace, SFMono-Regular, "Liberation Mono", Menlo, Consolas, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }}
    .ascii-light {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 7.5px; font-weight: 700; letter-spacing: 0.8px; fill: #1E293B; }}
  </style>

  <!-- Root Canvas Background -->
  <rect width="1180" height="610" rx="22" fill="#F8FAFC"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlowLight1)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlowLight2)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlowLight3)"/>
  <rect width="1180" height="610" rx="22" fill="url(#gridPatternLight)"/>

  <!-- Outer Glass Frame Base Border -->
  <rect x="2" y="2" width="1176" height="606" rx="21" fill="none" stroke="url(#borderGradLight)" stroke-width="1.5"/>

  <!-- ==================== ANIMATION 1: LASER BORDER SHIMMER ==================== -->
  <rect x="2" y="2" width="1176" height="606" rx="21" fill="none" stroke="url(#laserBeamLight)" stroke-width="2.5" stroke-dasharray="160 580">
    <animate attributeName="stroke-dashoffset" values="0;-740" dur="4.5s" repeatCount="indefinite"/>
  </rect>

  <!-- ==================== LEFT COLUMN: VISUAL / IDENTITY ==================== -->
  <g id="left-column">
    <!-- Left Card Background -->
    <rect x="28" y="28" width="444" height="554" rx="16" fill="#FFFFFF" fill-opacity="0.95" stroke="url(#cardBorderLight)" stroke-width="1.2" filter="url(#cardShadow)"/>

    <!-- Terminal Window Bar -->
    <circle cx="50" cy="52" r="5" fill="#EF4444"/>
    <circle cx="66" cy="52" r="5" fill="#F59E0B"/>
    <circle cx="82" cy="52" r="5" fill="#10B981"/>
    <text x="104" y="56" class="mono" font-size="11.5" fill="#475569" font-weight="600">djabhi31@developer:~ (terminal.hud)</text>
    
    <!-- Status Pill -->
    <rect x="364" y="42" width="92" height="20" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="1"/>
    <circle cx="376" cy="52" r="3.5" fill="#10B981">
      <animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="386" y="56" class="mono" font-size="10" fill="#065F46" font-weight="700">ONLINE</text>

    <!-- Header Divider -->
    <line x1="28" y1="74" x2="472" y2="74" stroke="#E2E8F0" stroke-width="1"/>

    <!-- Biometric ID Header -->
    <text x="44" y="93" class="mono" font-size="10" fill="#2563EB" font-weight="700" letter-spacing="1">VISUAL.MAP // BIO-TELEMETRY</text>
    <text x="456" y="93" text-anchor="end" class="mono" font-size="9" fill="#059669" font-weight="700">● TARGET LOCK: 99.4%</text>

    <!-- ASCII Portrait Container Box -->
    <rect x="42" y="104" width="416" height="258" rx="10" fill="#F1F5F9" fill-opacity="0.95" stroke="#CBD5E1" stroke-width="1"/>

    <!-- ==================== ANIMATION 2: HUD RETICLE & CROSSHAIRS ==================== -->
    <path d="M 50 118 L 50 112 L 56 112" stroke="#2563EB" stroke-width="1.8" fill="none"/>
    <path d="M 450 118 L 450 112 L 444 112" stroke="#2563EB" stroke-width="1.8" fill="none"/>
    <path d="M 50 348 L 50 354 L 56 354" stroke="#2563EB" stroke-width="1.8" fill="none"/>
    <path d="M 450 348 L 450 354 L 444 354" stroke="#2563EB" stroke-width="1.8" fill="none"/>

    <!-- HUD Telemetry Tags on Portrait -->
    <text x="56" y="124" class="mono" font-size="8" fill="#2563EB" font-weight="600">[COORDS: 22.57°N, 88.36°E]</text>
    <text x="444" y="124" text-anchor="end" class="mono" font-size="8" fill="#7C3AED" font-weight="600">CALCUTTA UNIV</text>

    <!-- ASCII Character Stream -->
    <text class="ascii-light" text-anchor="middle">
{tspans_light_str}
    </text>

    <!-- ==================== ANIMATION 3: HOLOGRAM SCANLINE SWEEP ==================== -->
    <line x1="43" y1="106" x2="457" y2="106" stroke="url(#scanlineGradLight)" stroke-width="2.5" opacity="0.75">
      <animate attributeName="y1" values="106;358;106" dur="4.5s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="106;358;106" dur="4.5s" repeatCount="indefinite"/>
    </line>

    <!-- Subtle Signal Flicker Box Overlay -->
    <rect x="42" y="104" width="416" height="258" rx="10" fill="#2563EB" opacity="0">
      <animate attributeName="opacity" values="0;0.04;0;0.02;0;0;0.05;0" keyTimes="0;0.12;0.14;0.45;0.47;0.82;0.84;1" dur="6s" repeatCount="indefinite"/>
    </rect>

    <!-- ==================== ANIMATION 4: BOUNCING AUDIO EQUALIZER (DJ ABHI) ==================== -->
    <g id="audio-equalizer">
      <rect x="42" y="372" width="416" height="74" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="56" cy="386" r="3.5" fill="#E11D48">
        <animate attributeName="opacity" values="1;0.4;1" dur="1s" repeatCount="indefinite"/>
      </circle>
      <text x="66" y="390" class="mono" font-size="9.5" fill="#0F172A" font-weight="700">AUDIO.ENGINE // DJ ABHI SPECTRUM</text>
      <text x="444" y="390" text-anchor="end" class="mono" font-size="8.5" fill="#2563EB" font-weight="700">140 BPM [STEREO]</text>

      <!-- 24 Bouncing Equalizer Bars -->
{eq_light_str}
    </g>

    <!-- Terminal Command Line Prompt -->
    <rect x="42" y="456" width="416" height="74" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <text x="56" y="475" class="mono" font-size="10.5" fill="#2563EB" font-weight="700">~/profile $ <tspan fill="#0F172A">./launch --sound --systems</tspan></text>
    <text x="56" y="494" class="mono" font-size="9.5" fill="#475569">[OK] 3D_WEBGL: 60FPS · TELEMETRY: REAL-TIME</text>
    <text x="56" y="512" class="mono" font-size="9.5" fill="#475569">[OK] AUDIO_BASS: ONLINE · COMMUNITY: 38K+</text>
    <rect x="345" y="501" width="7" height="13" fill="#2563EB">
      <animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite"/>
    </rect>

    <!-- Quick Meta Pill -->
    <text x="250" y="555" text-anchor="middle" class="mono" font-size="9" fill="#94A3B8" letter-spacing="1.2">ABHILASH GHOSH // SYSTEM BIO-IDENTITY CORE</text>
  </g>

  <!-- ==================== RIGHT COLUMN: SYSTEM.INFO ==================== -->
  <g id="right-column">
    <!-- Right Card Background -->
    <rect x="490" y="28" width="662" height="554" rx="16" fill="#FFFFFF" fill-opacity="0.95" stroke="url(#cardBorderLight)" stroke-width="1.2" filter="url(#cardShadow)"/>

    <!-- Terminal Bar -->
    <circle cx="512" cy="52" r="5" fill="#EF4444"/>
    <circle cx="528" cy="52" r="5" fill="#F59E0B"/>
    <circle cx="544" cy="52" r="5" fill="#10B981"/>
    <text x="564" y="56" class="mono" font-size="11.5" fill="#475569" font-weight="600">SYSTEM.INFO // EXECUTIVE_CORE</text>
    <rect x="1038" y="42" width="98" height="20" rx="10" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1"/>
    <text x="1087" y="56" text-anchor="middle" class="mono" font-size="9.5" fill="#1D4ED8" font-weight="700">RELEASE v4.2</text>

    <!-- Header Divider -->
    <line x1="490" y1="74" x2="1152" y2="74" stroke="#E2E8F0" stroke-width="1"/>

    <!-- 1. Identity & Animated Role Section -->
    <g transform="translate(510, 88)">
      <text x="0" y="14" class="mono" font-size="10.5" fill="#2563EB" font-weight="700">djabhi31@station:~$ whoami</text>
      
      <!-- Name -->
      <text x="0" y="44" class="sans" font-size="25" font-weight="800" fill="url(#textGradLight)" letter-spacing="0.5">ABHILASH GHOSH</text>
      <text x="250" y="42" class="mono" font-size="13" fill="#64748B">(@djabhi31)</text>

      <!-- Animated Rotating Role (4 states cycling smoothly every 16s) -->
      <g transform="translate(0, 68)">
        <text class="mono" font-size="13" font-weight="700" fill="#2563EB">
          <tspan>&gt; ROLE: </tspan>
        </text>

        <!-- Role 1: 0s-4s -->
        <text x="68" y="0" class="mono" font-size="13" font-weight="700" fill="#0F172A" opacity="0">
          Full-Stack &amp; 3D Web Engineer <tspan fill="#2563EB">▋</tspan>
          <animate attributeName="opacity" values="1;1;0;0;0;0;0;1" keyTimes="0;0.22;0.25;0.5;0.75;0.97;0.99;1" dur="16s" repeatCount="indefinite"/>
        </text>

        <!-- Role 2: 4s-8s -->
        <text x="68" y="0" class="mono" font-size="13" font-weight="700" fill="#7C3AED" opacity="0">
          Creative Technologist &amp; Music Producer <tspan fill="#7C3AED">▋</tspan>
          <animate attributeName="opacity" values="0;0;1;1;0;0;0;0" keyTimes="0;0.23;0.26;0.47;0.5;0.75;0.97;1" dur="16s" repeatCount="indefinite"/>
        </text>

        <!-- Role 3: 8s-12s -->
        <text x="68" y="0" class="mono" font-size="13" font-weight="700" fill="#059669" opacity="0">
          Founder of Mermaidz Records &amp; ExcuseVerse <tspan fill="#059669">▋</tspan>
          <animate attributeName="opacity" values="0;0;0;0;1;1;0;0" keyTimes="0;0.48;0.51;0.72;0.75;0.9;0.97;1" dur="16s" repeatCount="indefinite"/>
        </text>

        <!-- Role 4: 12s-16s -->
        <text x="68" y="0" class="mono" font-size="13" font-weight="700" fill="#0284C7" opacity="0">
          Geospatial &amp; Real-Time Systems Architect <tspan fill="#0284C7">▋</tspan>
          <animate attributeName="opacity" values="0;0;0;0;0;0;1;1" keyTimes="0;0.48;0.5;0.73;0.76;0.96;0.98;1" dur="16s" repeatCount="indefinite"/>
        </text>
      </g>

      <!-- Identity Pills -->
      <g transform="translate(0, 84)">
        <rect x="0" y="0" width="144" height="22" rx="11" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
        <text x="72" y="15" text-anchor="middle" class="mono" font-size="9.5" fill="#334155" font-weight="600">📍 Kolkata, India</text>

        <rect x="152" y="0" width="168" height="22" rx="11" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1"/>
        <text x="236" y="15" text-anchor="middle" class="mono" font-size="9.5" fill="#7C3AED" font-weight="600">🎧 DJ ABHI-Maheshtala</text>

        <rect x="328" y="0" width="154" height="22" rx="11" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
        <text x="405" y="15" text-anchor="middle" class="mono" font-size="9.5" fill="#1D4ED8" font-weight="600">🎓 M.Com (Calcutta Univ)</text>

        <rect x="490" y="0" width="132" height="22" rx="11" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>
        <text x="556" y="15" text-anchor="middle" class="mono" font-size="9.5" fill="#047857" font-weight="600">⚡ 38K+ YouTube</text>
      </g>
    </g>

    <!-- 2. Featured Projects Grid (2x2) -->
    <g transform="translate(510, 202)">
      <text x="0" y="0" class="mono" font-size="10" fill="#2563EB" font-weight="700" letter-spacing="1">// PRODUCTION BUILDS &amp; PLATFORMS</text>
      
      <!-- Project 1: EarthSphere -->
      <g transform="translate(0, 8)">
        <rect x="0" y="0" width="304" height="52" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="16" cy="17" r="4" fill="#0284C7">
          <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
        </circle>
        <text x="28" y="20" class="sans" font-size="11.5" font-weight="700" fill="#0F172A">EarthSphere</text>
        <rect x="110" y="9" width="58" height="14" rx="7" fill="#E0F2FE"/>
        <text x="139" y="19" text-anchor="middle" class="mono" font-size="7.5" fill="#0369A1" font-weight="700">LIVE PROD</text>
        <text x="14" y="34" class="sans" font-size="9" fill="#475569">Real-time planetary event intelligence via NASA EONET</text>
        <text x="14" y="45" class="mono" font-size="8" fill="#0284C7">Next.js 15 · Three.js · WebGL · MapLibre GL</text>
      </g>

      <!-- Project 2: God's Eye View -->
      <g transform="translate(318, 8)">
        <rect x="0" y="0" width="304" height="52" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="16" cy="17" r="4" fill="#7C3AED">
          <animate attributeName="opacity" values="1;0.4;1" dur="2.3s" repeatCount="indefinite"/>
        </circle>
        <text x="28" y="20" class="sans" font-size="11.5" font-weight="700" fill="#0F172A">God's Eye View</text>
        <rect x="130" y="9" width="62" height="14" rx="7" fill="#F3E8FF"/>
        <text x="161" y="19" text-anchor="middle" class="mono" font-size="7.5" fill="#7E22CE" font-weight="700">AZURE CLOUD</text>
        <text x="14" y="34" class="sans" font-size="9" fill="#475569">Real-time 3D planetary intelligence console</text>
        <text x="14" y="45" class="mono" font-size="8" fill="#7C3AED">Microsoft Azure · WebGL · 3D Engine · Cloud</text>
      </g>

      <!-- Project 3: ExcuseVerse -->
      <g transform="translate(0, 66)">
        <rect x="0" y="0" width="304" height="52" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="16" cy="17" r="4" fill="#D97706">
          <animate attributeName="opacity" values="1;0.4;1" dur="1.8s" repeatCount="indefinite"/>
        </circle>
        <text x="28" y="20" class="sans" font-size="11.5" font-weight="700" fill="#0F172A">ExcuseVerse</text>
        <rect x="110" y="9" width="54" height="14" rx="7" fill="#FEF3C7"/>
        <text x="137" y="19" text-anchor="middle" class="mono" font-size="7.5" fill="#B45309" font-weight="700">AI APP</text>
        <text x="14" y="34" class="sans" font-size="9" fill="#475569">AI situational generator with 2,500+ dynamic excuses</text>
        <text x="14" y="45" class="mono" font-size="8" fill="#D97706">AI Integration · Next.js · Multi-Lingual UX</text>
      </g>

      <!-- Project 4: Mermaidz Records -->
      <g transform="translate(318, 66)">
        <rect x="0" y="0" width="304" height="52" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="16" cy="17" r="4" fill="#059669">
          <animate attributeName="opacity" values="1;0.4;1" dur="2.1s" repeatCount="indefinite"/>
        </circle>
        <text x="28" y="20" class="sans" font-size="11.5" font-weight="700" fill="#0F172A">Mermaidz Records</text>
        <rect x="144" y="9" width="56" height="14" rx="7" fill="#D1FAE5"/>
        <text x="172" y="19" text-anchor="middle" class="mono" font-size="7.5" fill="#047857" font-weight="700">LABEL</text>
        <text x="14" y="34" class="sans" font-size="9" fill="#475569">Music publishing &amp; distribution brand for indie artists</text>
        <text x="14" y="45" class="mono" font-size="8" fill="#059669">150+ Global Stores · Royalties &amp; Rights</text>
      </g>
    </g>

    <!-- ==================== ANIMATION 5: SYSTEM TELEMETRY WORKLOAD METERS ==================== -->
    <g transform="translate(510, 332)">
      <text x="0" y="0" class="mono" font-size="10" fill="#2563EB" font-weight="700" letter-spacing="1">// SYSTEM TELEMETRY &amp; WORKLOADS</text>
      
      <!-- Meter 1: 3D WebGL Engine -->
      <g transform="translate(0, 10)">
        <text x="0" y="0" class="mono" font-size="8.5" fill="#475569" font-weight="600">3D WebGL Engine &amp; Shaders (Three.js)</text>
        <text x="622" y="0" text-anchor="end" class="mono" font-size="8.5" fill="#1D4ED8" font-weight="700">60 FPS // GPU 95%</text>
        <rect x="0" y="5" width="622" height="6" rx="3" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="0.75"/>
        <rect x="0" y="5" width="580" height="6" rx="3" fill="url(#blueMeterLight)">
          <animate attributeName="width" values="460;590;530;590" dur="3.5s" repeatCount="indefinite"/>
        </rect>
      </g>

      <!-- Meter 2: NASA EONET Radar -->
      <g transform="translate(0, 32)">
        <text x="0" y="0" class="mono" font-size="8.5" fill="#475569" font-weight="600">NASA EONET Real-Time Planetary Radar</text>
        <text x="622" y="0" text-anchor="end" class="mono" font-size="8.5" fill="#7C3AED" font-weight="700">SYNC: 100% // 24H STREAM</text>
        <rect x="0" y="5" width="622" height="6" rx="3" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="0.75"/>
        <rect x="0" y="5" width="520" height="6" rx="3" fill="url(#violetMeterLight)">
          <animate attributeName="width" values="360;530;440;530" dur="4.2s" repeatCount="indefinite"/>
        </rect>
      </g>

      <!-- Meter 3: Audio Workstation -->
      <g transform="translate(0, 54)">
        <text x="0" y="0" class="mono" font-size="8.5" fill="#475569" font-weight="600">Audio Workstation // Bass &amp; EDM Master (FL Studio)</text>
        <text x="622" y="0" text-anchor="end" class="mono" font-size="8.5" fill="#047857" font-weight="700">140 BPM // MASTERED</text>
        <rect x="0" y="5" width="622" height="6" rx="3" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="0.75"/>
        <rect x="0" y="5" width="560" height="6" rx="3" fill="url(#greenMeterLight)">
          <animate attributeName="width" values="410;575;490;575" dur="2.8s" repeatCount="indefinite"/>
        </rect>
      </g>
    </g>

    <!-- 4. Technical Stack Pills Grid -->
    <g transform="translate(510, 412)">
      <text x="0" y="0" class="mono" font-size="10" fill="#2563EB" font-weight="700" letter-spacing="1">// TECHNICAL ARSENAL &amp; CORE STACK</text>
      
      <!-- Row 1 -->
      <g transform="translate(0, 8)">
        <!-- Next.js 15 -->
        <rect x="0" y="0" width="98" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="10" cy="11" r="3" fill="#0284C7"/>
        <text x="20" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">Next.js 15</text>

        <!-- React 19 -->
        <rect x="105" y="0" width="96" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="115" cy="11" r="3" fill="#06B6D4"/>
        <text x="125" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">React 19</text>

        <!-- Three.js -->
        <rect x="208" y="0" width="94" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="218" cy="11" r="3" fill="#7C3AED"/>
        <text x="228" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">Three.js</text>

        <!-- WebGL -->
        <rect x="309" y="0" width="86" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="319" cy="11" r="3" fill="#DB2777"/>
        <text x="329" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">WebGL</text>

        <!-- TypeScript -->
        <rect x="402" y="0" width="104" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="412" cy="11" r="3" fill="#2563EB"/>
        <text x="422" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">TypeScript</text>

        <!-- Python -->
        <rect x="513" y="0" width="88" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="523" cy="11" r="3" fill="#CA8A04"/>
        <text x="533" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">Python</text>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 36)">
        <!-- TailwindCSS -->
        <rect x="0" y="0" width="112" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="10" cy="11" r="3" fill="#0891B2"/>
        <text x="20" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">TailwindCSS</text>

        <!-- Azure -->
        <rect x="119" y="0" width="118" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="129" cy="11" r="3" fill="#0284C7"/>
        <text x="139" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">Microsoft Azure</text>

        <!-- MapLibre GL -->
        <rect x="244" y="0" width="112" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="254" cy="11" r="3" fill="#059669"/>
        <text x="264" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">MapLibre GL</text>

        <!-- GitHub Actions -->
        <rect x="363" y="0" width="124" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="373" cy="11" r="3" fill="#4F46E5"/>
        <text x="383" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">GitHub Actions</text>

        <!-- FL Studio -->
        <rect x="494" y="0" width="106" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="504" cy="11" r="3" fill="#EA580C"/>
        <text x="514" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">FL Studio</text>
      </g>
    </g>

    <!-- 5. Terminal Connect & Footer Bar -->
    <g transform="translate(510, 482)">
      <rect x="0" y="0" width="622" height="62" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="18" cy="18" r="3" fill="#2563EB"/>
      <text x="28" y="21" class="mono" font-size="10" fill="#2563EB" font-weight="700">&gt; ECOSYSTEM &amp; CONNECT MATRIX</text>
      
      <text x="28" y="38" class="mono" font-size="9" fill="#0F172A">
        <tspan fill="#64748B">WEB:</tspan> abhilashghosh.pages.dev <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">YT:</tspan> @djabhimaheshtala (38K+) <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">SPOTIFY:</tspan> DJ ABHI
      </text>
      
      <text x="28" y="52" class="mono" font-size="9" fill="#0F172A">
        <tspan fill="#64748B">GH:</tspan> github.com/djabhi31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">X:</tspan> @DjAbhi31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">IG:</tspan> @djabhi.31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">MAIL:</tspan> abhilashghosh31@gmail.com
      </text>
    </g>

    <!-- Bottom Meta Tagline -->
    <text x="821" y="562" text-anchor="middle" class="mono" font-size="8.5" fill="#94A3B8" letter-spacing="1.2">SYSTEM STATUS: FULLY OPERATIONAL // KERNEL RUNNING</text>
  </g>
</svg>'''

    # Validate XML
    ET.fromstring(dark_svg)
    print("dark.svg is valid XML!")
    with open('dark.svg', 'w', encoding='utf-8') as f:
        f.write(dark_svg)

    ET.fromstring(light_svg)
    print("light.svg is valid XML!")
    with open('light.svg', 'w', encoding='utf-8') as f:
        f.write(light_svg)

if __name__ == '__main__':
    generate_svgs()
