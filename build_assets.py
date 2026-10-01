import os
import base64
import io
from PIL import Image, ImageEnhance
import xml.etree.ElementTree as ET

def generate_svgs():
    avatar_path = 'avatar.png'
    if not os.path.exists(avatar_path):
        raise FileNotFoundError(f"Avatar file not found at {avatar_path}")
        
    # 1. Studio-grade image enhancement for crystal-clear avatar
    img = Image.open(avatar_path).convert('RGB')
    # Subtle studio enhancement: crisp sharpness, vibrant color pop, balanced contrast
    img_sharp = ImageEnhance.Sharpness(img).enhance(1.22)
    img_color = ImageEnhance.Color(img_sharp).enhance(1.08)
    img_contrast = ImageEnhance.Contrast(img_color).enhance(1.05)
    
    # Save optimized JPEG to base64
    buf = io.BytesIO()
    img_contrast.save(buf, format='JPEG', quality=92)
    b64_avatar = base64.b64encode(buf.getvalue()).decode('ascii')

    # 2. Generate 24 animated Equalizer bars
    eq_dark_bars = []
    eq_light_bars = []
    base_x = 61
    base_y = 438

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
        
        bar_d = f'''        <rect x="{bx}" y="{base_y - p[0]}" width="10" height="{p[0]}" rx="3" fill="url(#eqGradDark)">
          <animate attributeName="height" values="{h_vals}" dur="{dur}" repeatCount="indefinite"/>
          <animate attributeName="y" values="{y_vals}" dur="{dur}" repeatCount="indefinite"/>
        </rect>'''
        eq_dark_bars.append(bar_d)

        bar_l = f'''        <rect x="{bx}" y="{base_y - p[0]}" width="10" height="{p[0]}" rx="3" fill="url(#eqGradLight)">
          <animate attributeName="height" values="{h_vals}" dur="{dur}" repeatCount="indefinite"/>
          <animate attributeName="y" values="{y_vals}" dur="{dur}" repeatCount="indefinite"/>
        </rect>'''
        eq_light_bars.append(bar_l)

    eq_dark_str = '\n'.join(eq_dark_bars)
    eq_light_str = '\n'.join(eq_light_bars)

    # 3. Build hyper-animated dark.svg
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

    <!-- Holographic Avatar Clip Path -->
    <clipPath id="avatarClip">
      <circle cx="250" cy="233" r="72"/>
    </clipPath>

    <!-- Hologram Core Breathing Glow -->
    <radialGradient id="holoCoreGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.75"/>
      <stop offset="45%" stop-color="#8B5CF6" stop-opacity="0.40"/>
      <stop offset="85%" stop-color="#EC4899" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#030712" stop-opacity="0"/>
    </radialGradient>

    <!-- Animated Hologram Frame Border Gradient -->
    <linearGradient id="avatarBorderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22D3EE">
        <animate attributeName="stop-color" values="#22D3EE;#A855F7;#38BDF8;#34D399;#22D3EE" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#818CF8">
        <animate attributeName="stop-color" values="#818CF8;#EC4899;#22D3EE;#818CF8;#818CF8" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#C084FC">
        <animate attributeName="stop-color" values="#C084FC;#22D3EE;#A855F7;#818CF8;#C084FC" dur="5s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <!-- Hologram Laser Scan Beam Ribbon -->
    <linearGradient id="hologramSweepGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0"/>
      <stop offset="50%" stop-color="#38BDF8" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#C084FC" stop-opacity="0"/>
    </linearGradient>

    <!-- Laser Border Beam Gradient -->
    <linearGradient id="laserBeam" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22D3EE"/>
      <stop offset="35%" stop-color="#818CF8"/>
      <stop offset="70%" stop-color="#C084FC"/>
      <stop offset="100%" stop-color="#34D399"/>
    </linearGradient>

    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#818CF8" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#C084FC" stop-opacity="0.40"/>
    </linearGradient>
    <linearGradient id="cardBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.65"/>
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
  </style>

  <!-- Root Canvas Background -->
  <rect width="1180" height="610" rx="22" fill="#030712"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlow1)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlow2)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlow3)"/>
  <rect width="1180" height="610" rx="22" fill="url(#gridPattern)"/>

  <!-- Outer Glass Frame Base Border -->
  <rect x="2" y="2" width="1176" height="606" rx="21" fill="none" stroke="url(#borderGrad)" stroke-width="1.5"/>

  <!-- ANIMATION 1: LASER BORDER SHIMMER -->
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
    <text x="456" y="93" text-anchor="end" class="mono" font-size="9" fill="#10B981" font-weight="600">● TARGET LOCK: 99.8%</text>

    <!-- ========================================================================= -->
    <!--          ULTRA-PREMIUM HOLOGRAPHIC QUANTUM AVATAR REACTOR CHAMBER         -->
    <!-- ========================================================================= -->
    <g id="holographic-avatar-reactor">
      <!-- Container Box -->
      <rect x="42" y="104" width="416" height="258" rx="10" fill="#040914" fill-opacity="0.94" stroke="#1E293B" stroke-width="1"/>

      <!-- Ambient Chamber Grid Accent -->
      <line x1="42" y1="170" x2="458" y2="170" stroke="#1E293B" stroke-width="0.5" stroke-dasharray="4 6"/>
      <line x1="42" y1="296" x2="458" y2="296" stroke="#1E293B" stroke-width="0.5" stroke-dasharray="4 6"/>

      <!-- TOP IDENTIFICATION BADGE -->
      <g transform="translate(160, 112)">
        <rect x="0" y="0" width="180" height="20" rx="10" fill="#070D1A" stroke="#22D3EE" stroke-width="0.8"/>
        <circle cx="12" cy="10" r="3" fill="#22D3EE">
          <animate attributeName="opacity" values="1;0.4;1" dur="1.8s" repeatCount="indefinite"/>
        </circle>
        <text x="22" y="14" class="mono" font-size="8.5" fill="#38BDF8" font-weight="700" letter-spacing="0.5">● HOLOGRAPHIC // DJ ABHI</text>
      </g>

      <!-- ==================== LEFT TELEMETRY SIDECAR ==================== -->
      <g transform="translate(50, 142)">
        <rect x="0" y="0" width="76" height="182" rx="6" fill="#070D1A" fill-opacity="0.9" stroke="#1E293B" stroke-width="0.8"/>
        <text x="38" y="16" text-anchor="middle" class="mono" font-size="7.5" fill="#38BDF8" font-weight="700">BIO.SENSORS</text>
        <line x1="6" y1="22" x2="70" y2="22" stroke="#1E293B" stroke-width="0.8"/>

        <circle cx="12" cy="34" r="2.5" fill="#10B981">
          <animate attributeName="opacity" values="1;0.3;1" dur="1.4s" repeatCount="indefinite"/>
        </circle>
        <text x="20" y="37" class="mono" font-size="7" fill="#34D399" font-weight="600">AUTH: 100%</text>

        <text x="8" y="56" class="mono" font-size="6.8" fill="#94A3B8">ID: AG-31</text>
        <text x="8" y="70" class="mono" font-size="6.8" fill="#94A3B8">22.57° N</text>
        <text x="8" y="84" class="mono" font-size="6.8" fill="#94A3B8">88.36° E</text>
        <text x="8" y="98" class="mono" font-size="6.8" fill="#94A3B8">CALCUTTA</text>
        <text x="8" y="112" class="mono" font-size="6.8" fill="#38BDF8">LOCK: 99.8%</text>

        <!-- Mini 4-Bar Biometric Pulse Signal -->
        <g transform="translate(10, 128)">
          <text x="0" y="-4" class="mono" font-size="6" fill="#64748B">PULSE:</text>
          <rect x="0" y="0" width="10" height="28" rx="2" fill="#1E293B"/>
          <rect x="0" y="12" width="10" height="16" rx="2" fill="#22D3EE">
            <animate attributeName="height" values="16;26;8;22;16" dur="1.8s" repeatCount="indefinite"/>
            <animate attributeName="y" values="12;2;20;6;12" dur="1.8s" repeatCount="indefinite"/>
          </rect>

          <rect x="14" y="0" width="10" height="28" rx="2" fill="#1E293B"/>
          <rect x="14" y="6" width="10" height="22" rx="2" fill="#38BDF8">
            <animate attributeName="height" values="22;10;28;14;22" dur="1.5s" repeatCount="indefinite"/>
            <animate attributeName="y" values="6;18;0;14;6" dur="1.5s" repeatCount="indefinite"/>
          </rect>

          <rect x="28" y="0" width="10" height="28" rx="2" fill="#1E293B"/>
          <rect x="28" y="16" width="10" height="12" rx="2" fill="#818CF8">
            <animate attributeName="height" values="12;24;6;20;12" dur="2.1s" repeatCount="indefinite"/>
            <animate attributeName="y" values="16;4;22;8;16" dur="2.1s" repeatCount="indefinite"/>
          </rect>

          <rect x="42" y="0" width="10" height="28" rx="2" fill="#1E293B"/>
          <rect x="42" y="8" width="10" height="20" rx="2" fill="#C084FC">
            <animate attributeName="height" values="20;14;26;10;20" dur="1.7s" repeatCount="indefinite"/>
            <animate attributeName="y" values="8;14;2;18;8" dur="1.7s" repeatCount="indefinite"/>
          </rect>
        </g>
      </g>

      <!-- ==================== RIGHT TELEMETRY SIDECAR ==================== -->
      <g transform="translate(374, 142)">
        <rect x="0" y="0" width="76" height="182" rx="6" fill="#070D1A" fill-opacity="0.9" stroke="#1E293B" stroke-width="0.8"/>
        <text x="38" y="16" text-anchor="middle" class="mono" font-size="7.5" fill="#C084FC" font-weight="700">NEURAL.LINK</text>
        <line x1="6" y1="22" x2="70" y2="22" stroke="#1E293B" stroke-width="0.8"/>

        <circle cx="12" cy="34" r="2.5" fill="#A855F7">
          <animate attributeName="opacity" values="1;0.3;1" dur="1.8s" repeatCount="indefinite"/>
        </circle>
        <text x="20" y="37" class="mono" font-size="7" fill="#C084FC" font-weight="600">SYNC: READY</text>

        <text x="8" y="56" class="mono" font-size="6.8" fill="#94A3B8">140 BPM</text>
        <text x="8" y="70" class="mono" font-size="6.8" fill="#94A3B8">38K+ AUD</text>
        <text x="8" y="84" class="mono" font-size="6.8" fill="#94A3B8">GL: 60 FPS</text>
        <text x="8" y="98" class="mono" font-size="6.8" fill="#94A3B8">WEBGL 2.0</text>
        <text x="8" y="112" class="mono" font-size="6.8" fill="#34D399">ACTIVE CORE</text>

        <!-- Mini 4-Bar Neural Throughput Signal -->
        <g transform="translate(10, 128)">
          <text x="0" y="-4" class="mono" font-size="6" fill="#64748B">THROUGHPUT:</text>
          <rect x="0" y="0" width="10" height="28" rx="2" fill="#1E293B"/>
          <rect x="0" y="8" width="10" height="20" rx="2" fill="#A855F7">
            <animate attributeName="height" values="20;12;26;14;20" dur="1.6s" repeatCount="indefinite"/>
            <animate attributeName="y" values="8;16;2;14;8" dur="1.6s" repeatCount="indefinite"/>
          </rect>

          <rect x="14" y="0" width="10" height="28" rx="2" fill="#1E293B"/>
          <rect x="14" y="14" width="10" height="14" rx="2" fill="#EC4899">
            <animate attributeName="height" values="14;26;8;22;14" dur="1.9s" repeatCount="indefinite"/>
            <animate attributeName="y" values="14;2;20;6;14" dur="1.9s" repeatCount="indefinite"/>
          </rect>

          <rect x="28" y="0" width="10" height="28" rx="2" fill="#1E293B"/>
          <rect x="28" y="6" width="10" height="22" rx="2" fill="#38BDF8">
            <animate attributeName="height" values="22;14;28;10;22" dur="1.4s" repeatCount="indefinite"/>
            <animate attributeName="y" values="6;14;0;18;6" dur="1.4s" repeatCount="indefinite"/>
          </rect>

          <rect x="42" y="0" width="10" height="28" rx="2" fill="#1E293B"/>
          <rect x="42" y="12" width="10" height="16" rx="2" fill="#10B981">
            <animate attributeName="height" values="16;26;10;24;16" dur="2.0s" repeatCount="indefinite"/>
            <animate attributeName="y" values="12;2;18;4;12" dur="2.0s" repeatCount="indefinite"/>
          </rect>
        </g>
      </g>

      <!-- ==================== CENTER: HOLOGRAPHIC QUANTUM AVATAR ==================== -->
      <!-- 1. Holographic Breathing Reactor Core Glow -->
      <circle cx="250" cy="233" r="92" fill="url(#holoCoreGlow)">
        <animate attributeName="r" values="84;106;84" dur="4s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.55;0.95;0.55" dur="4s" repeatCount="indefinite"/>
      </circle>

      <!-- 2. Dual-Frequency Expanding Quantum Radar/Sonar Waves -->
      <circle cx="250" cy="233" r="74" fill="none" stroke="#22D3EE" stroke-width="1.6" opacity="0.8">
        <animate attributeName="r" values="74;128" dur="3.2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.85;0" dur="3.2s" repeatCount="indefinite"/>
      </circle>
      <circle cx="250" cy="233" r="74" fill="none" stroke="#C084FC" stroke-width="1.6" opacity="0.8">
        <animate attributeName="r" values="74;128" begin="1.6s" dur="3.2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.85;0" begin="1.6s" dur="3.2s" repeatCount="indefinite"/>
      </circle>

      <!-- 3. Gyroscopic HUD Rings -->
      <!-- Ring A: Outer Compass Ring with Cardinal Ticks (Clockwise, 24s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0 250 233" to="360 250 233" dur="24s" repeatCount="indefinite"/>
        <circle cx="250" cy="233" r="114" fill="none" stroke="#38BDF8" stroke-width="1.4" stroke-dasharray="24 12 6 12 36 12" opacity="0.75"/>
        <!-- Cardinal Marks -->
        <polygon points="250,116 247,122 253,122" fill="#22D3EE"/>
        <polygon points="250,350 247,344 253,344" fill="#22D3EE"/>
        <polygon points="133,233 139,230 139,236" fill="#22D3EE"/>
        <polygon points="367,233 361,230 361,236" fill="#22D3EE"/>
      </g>

      <!-- Ring B: Segmented Target Arcs (Counter-Clockwise, 14s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="360 250 233" to="0 250 233" dur="14s" repeatCount="indefinite"/>
        <circle cx="250" cy="233" r="100" fill="none" stroke="#A855F7" stroke-width="2.2" stroke-dasharray="64 92 64 92" stroke-linecap="round" opacity="0.85"/>
      </g>

      <!-- Ring C: Precision Dotted Calibration Track (Clockwise, 36s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0 250 233" to="360 250 233" dur="36s" repeatCount="indefinite"/>
        <circle cx="250" cy="233" r="88" fill="none" stroke="#818CF8" stroke-width="1.2" stroke-dasharray="3 6" opacity="0.75"/>
      </g>

      <!-- 4. Orbital Satellites (3 Orbiting Quantum Nodes) -->
      <!-- Satellite 1: Neon Cyan (R=114, 7s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0 250 233" to="360 250 233" dur="7s" repeatCount="indefinite"/>
        <circle cx="250" cy="119" r="3.5" fill="#22D3EE"/>
        <circle cx="250" cy="119" r="6" fill="#22D3EE" opacity="0.4"/>
      </g>
      <!-- Satellite 2: Neon Violet (R=100, Counter-clockwise, 10s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="360 250 233" to="0 250 233" dur="10s" repeatCount="indefinite"/>
        <circle cx="250" cy="133" r="3" fill="#C084FC"/>
        <circle cx="250" cy="133" r="5.5" fill="#C084FC" opacity="0.4"/>
      </g>
      <!-- Satellite 3: Emerald (R=88, 5s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0 250 233" to="360 250 233" dur="5s" repeatCount="indefinite"/>
        <circle cx="250" cy="145" r="2.5" fill="#34D399"/>
      </g>

      <!-- 5. REAL STUDIO PORTRAIT (Masked to circle with 3D breathing float) -->
      <g id="avatar-core-group">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -2.5; 0 0; 0 2.5; 0 0" dur="4.5s" repeatCount="indefinite"/>
        
        <!-- High-Definition Masked Image -->
        <image href="data:image/jpeg;base64,{b64_avatar}" x="178" y="161" width="144" height="144" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarClip)"/>

        <!-- Glowing Neon Reactor Rim -->
        <circle cx="250" cy="233" r="73" fill="none" stroke="url(#avatarBorderGrad)" stroke-width="2.5"/>

        <!-- Holographic Laser Scanner Sweep (Clipped to Avatar) -->
        <rect x="176" y="159" width="148" height="14" fill="url(#hologramSweepGrad)" clip-path="url(#avatarClip)">
          <animate attributeName="y" values="155;302;155" dur="3.2s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="0.4;0.9;0.4" dur="3.2s" repeatCount="indefinite"/>
        </rect>
        <line x1="176" y1="166" x2="324" y2="166" stroke="#22D3EE" stroke-width="1.6" clip-path="url(#avatarClip)">
          <animate attributeName="y1" values="162;309;162" dur="3.2s" repeatCount="indefinite"/>
          <animate attributeName="y2" values="162;309;162" dur="3.2s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="0.4;1;0.4" dur="3.2s" repeatCount="indefinite"/>
        </line>
      </g>

      <!-- 6. Cybernetic Corner Tracking Brackets -->
      <g id="tracking-corners" stroke="#22D3EE" stroke-width="1.8" fill="none">
        <animate attributeName="stroke" values="#22D3EE;#A855F7;#38BDF8;#22D3EE" dur="4.5s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.6;1;0.6" dur="2.5s" repeatCount="indefinite"/>
        <!-- Top-Left -->
        <path d="M 188 185 L 188 171 L 202 171"/>
        <!-- Top-Right -->
        <path d="M 312 185 L 312 171 L 298 171"/>
        <!-- Bottom-Left -->
        <path d="M 188 281 L 188 295 L 202 295"/>
        <!-- Bottom-Right -->
        <path d="M 312 281 L 312 295 L 298 295"/>
      </g>

      <!-- Precision Micro-Crosshair Center Ticks -->
      <g stroke="#22D3EE" stroke-width="1.2" opacity="0.8">
        <line x1="243" y1="233" x2="247" y2="233"/>
        <line x1="253" y1="233" x2="257" y2="233"/>
        <line x1="250" y1="226" x2="250" y2="230"/>
        <line x1="250" y1="236" x2="250" y2="240"/>
      </g>

      <!-- BOTTOM BIOMETRIC CORE STATUS -->
      <g transform="translate(160, 334)">
        <rect x="0" y="0" width="180" height="20" rx="10" fill="#070D1A" stroke="#A855F7" stroke-width="0.8"/>
        <circle cx="12" cy="10" r="3" fill="#A855F7">
          <animate attributeName="opacity" values="1;0.4;1" dur="1.8s" repeatCount="indefinite"/>
        </circle>
        <text x="22" y="14" class="mono" font-size="8" fill="#C084FC" font-weight="700" letter-spacing="0.5">BIOMETRIC CORE // SECURED</text>
      </g>
    </g>

    <!-- ANIMATION 6: BOUNCING AUDIO EQUALIZER (DJ ABHI) -->
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
    <text x="1087" y="56" text-anchor="middle" class="mono" font-size="9.5" fill="#38BDF8" font-weight="600">RELEASE v4.5</text>

    <!-- Header Divider -->
    <line x1="490" y1="74" x2="1152" y2="74" stroke="#1E293B" stroke-width="1"/>

    <!-- 1. Identity & Animated Role Section -->
    <g transform="translate(510, 88)">
      <text x="0" y="14" class="mono" font-size="10.5" fill="#38BDF8" font-weight="600">djabhi31@station:~$ whoami</text>
      
      <!-- Name -->
      <text x="0" y="44" class="sans" font-size="25" font-weight="800" fill="url(#textGrad)" letter-spacing="0.5">ABHILASH GHOSH</text>
      <text x="250" y="42" class="mono" font-size="13" fill="#64748B">(@djabhi31)</text>

      <!-- Roles & Badges Row -->
      <g transform="translate(0, 56)">
        <!-- Badge 1: 3D Systems -->
        <rect x="0" y="0" width="170" height="22" rx="11" fill="#0284C7" fill-opacity="0.16" stroke="#0284C7" stroke-width="1"/>
        <circle cx="11" cy="11" r="3.5" fill="#38BDF8"/>
        <text x="22" y="15" class="mono" font-size="9.5" fill="#38BDF8" font-weight="600">3D Systems Engineer</text>

        <!-- Badge 2: Producer / DJ -->
        <rect x="178" y="0" width="168" height="22" rx="11" fill="#F43F5E" fill-opacity="0.15" stroke="#F43F5E" stroke-width="1"/>
        <circle cx="189" cy="11" r="3.5" fill="#FB7185"/>
        <text x="200" y="15" class="mono" font-size="9.5" fill="#FDA4AF" font-weight="600">DJ ABHI-Maheshtala</text>

        <!-- Badge 3: Cloud / NASA -->
        <rect x="354" y="0" width="138" height="22" rx="11" fill="#10B981" fill-opacity="0.15" stroke="#10B981" stroke-width="1"/>
        <circle cx="365" cy="11" r="3.5" fill="#34D399"/>
        <text x="376" y="15" class="mono" font-size="9.5" fill="#6EE7B7" font-weight="600">Cloud Telemetry</text>

        <!-- Badge 4: Location -->
        <rect x="500" y="0" width="122" height="22" rx="11" fill="#8B5CF6" fill-opacity="0.15" stroke="#8B5CF6" stroke-width="1"/>
        <circle cx="511" cy="11" r="3.5" fill="#C084FC"/>
        <text x="522" y="15" class="mono" font-size="9.5" fill="#DDD6FE" font-weight="600">Kolkata, IN</text>
      </g>
    </g>

    <!-- 2. System Architecture / Hardware Gauges (Telemetry Meters) -->
    <g transform="translate(510, 178)">
      <text x="0" y="10" class="mono" font-size="10" fill="#64748B" font-weight="600">SYSTEM ARCHITECTURE TELEMETRY</text>
      
      <!-- Meter 1: WebGL GPU Compute -->
      <g transform="translate(0, 20)">
        <text x="0" y="12" class="mono" font-size="9.5" fill="#94A3B8">WEBGL 3D COMPUTE (THREE.JS)</text>
        <text x="622" y="12" text-anchor="end" class="mono" font-size="9.5" fill="#38BDF8" font-weight="600">60 FPS // ULTRA</text>
        <rect x="0" y="18" width="622" height="6" rx="3" fill="#1E293B"/>
        <rect x="0" y="18" width="580" height="6" rx="3" fill="url(#cyanMeter)">
          <animate attributeName="width" values="540;590;560;610;580" dur="4s" repeatCount="indefinite"/>
        </rect>
      </g>

      <!-- Meter 2: Cloud Telemetry Link -->
      <g transform="translate(0, 50)">
        <text x="0" y="12" class="mono" font-size="9.5" fill="#94A3B8">AZURE / NASA EONET DATASTREAM</text>
        <text x="622" y="12" text-anchor="end" class="mono" font-size="9.5" fill="#C084FC" font-weight="600">42ms // REAL-TIME</text>
        <rect x="0" y="18" width="622" height="6" rx="3" fill="#1E293B"/>
        <rect x="0" y="18" width="550" height="6" rx="3" fill="url(#violetMeter)">
          <animate attributeName="width" values="520;565;535;580;550" dur="3.5s" repeatCount="indefinite"/>
        </rect>
      </g>

      <!-- Meter 3: Sound Engine & Studio Throughput -->
      <g transform="translate(0, 80)">
        <text x="0" y="12" class="mono" font-size="9.5" fill="#94A3B8">SOUND MASTERING / DSP ENGINE</text>
        <text x="622" y="12" text-anchor="end" class="mono" font-size="9.5" fill="#34D399" font-weight="600">32-BIT FLOAT // 140BPM</text>
        <rect x="0" y="18" width="622" height="6" rx="3" fill="#1E293B"/>
        <rect x="0" y="18" width="595" height="6" rx="3" fill="url(#greenMeter)">
          <animate attributeName="width" values="580;615;590;620;595" dur="3s" repeatCount="indefinite"/>
        </rect>
      </g>
    </g>

    <!-- 3. Production Deployments Table Grid -->
    <g transform="translate(510, 290)">
      <text x="0" y="10" class="mono" font-size="10" fill="#64748B" font-weight="600">PRODUCTION DEPLOYMENTS &amp; LIVE PLATFORMS</text>
      
      <!-- Row 1: EarthSphere + God's Eye View -->
      <g transform="translate(0, 20)">
        <!-- Project 1: EarthSphere -->
        <rect x="0" y="0" width="304" height="48" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#38BDF8"/>
        <text x="28" y="21" class="sans" font-size="11.5" fill="#F8FAFC" font-weight="700">EarthSphere</text>
        <rect x="110" y="10" width="56" height="15" rx="7.5" fill="#22C55E" fill-opacity="0.15"/>
        <text x="138" y="21" text-anchor="middle" class="mono" font-size="7.5" fill="#4ADE80" font-weight="700">LIVE PROD</text>
        <text x="16" y="38" class="mono" font-size="8.5" fill="#94A3B8">NASA EONET · Next.js 15 · Three.js 3D</text>

        <!-- Project 2: God's Eye View -->
        <rect x="318" y="0" width="304" height="48" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="334" cy="18" r="4" fill="#818CF8"/>
        <text x="346" y="21" class="sans" font-size="11.5" fill="#F8FAFC" font-weight="700">God's Eye View</text>
        <rect x="444" y="10" width="66" height="15" rx="7.5" fill="#0284C7" fill-opacity="0.2"/>
        <text x="477" y="21" text-anchor="middle" class="mono" font-size="7.5" fill="#38BDF8" font-weight="700">AZURE CLOUD</text>
        <text x="334" y="38" class="mono" font-size="8.5" fill="#94A3B8">Planetary WebGL Console on Azure</text>
      </g>

      <!-- Row 2: ExcuseVerse + Mermaidz Records -->
      <g transform="translate(0, 76)">
        <!-- Project 3: ExcuseVerse -->
        <rect x="0" y="0" width="304" height="48" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#C084FC"/>
        <text x="28" y="21" class="sans" font-size="11.5" fill="#F8FAFC" font-weight="700">ExcuseVerse</text>
        <rect x="114" y="10" width="46" height="15" rx="7.5" fill="#8B5CF6" fill-opacity="0.2"/>
        <text x="137" y="21" text-anchor="middle" class="mono" font-size="7.5" fill="#C084FC" font-weight="700">AI GEN</text>
        <text x="16" y="38" class="mono" font-size="8.5" fill="#94A3B8">Context AI Generator · Multi-Lingual</text>

        <!-- Project 4: Mermaidz Records -->
        <rect x="318" y="0" width="304" height="48" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="334" cy="18" r="4" fill="#34D399"/>
        <text x="346" y="21" class="sans" font-size="11.5" fill="#F8FAFC" font-weight="700">Mermaidz Records</text>
        <rect x="466" y="10" width="58" height="15" rx="7.5" fill="#10B981" fill-opacity="0.2"/>
        <text x="495" y="21" text-anchor="middle" class="mono" font-size="7.5" fill="#34D399" font-weight="700">150+ DSPS</text>
        <text x="334" y="38" class="mono" font-size="8.5" fill="#94A3B8">Global Music Distribution &amp; Label</text>
      </g>
    </g>

    <!-- 4. Core Tech Stack Tags Row -->
    <g transform="translate(510, 432)">
      <text x="0" y="10" class="mono" font-size="10" fill="#64748B" font-weight="600">CORE ARSENAL PILLARS</text>
      
      <g transform="translate(0, 18)">
        <!-- Next.js 15 -->
        <rect x="0" y="0" width="112" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="10" cy="11" r="3" fill="#38BDF8"/>
        <text x="20" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">Next.js 15</text>

        <!-- Three.js -->
        <rect x="122" y="0" width="112" height="22" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="132" cy="11" r="3" fill="#C084FC"/>
        <text x="142" y="15" class="mono" font-size="9" fill="#F8FAFC" font-weight="500">Three.js / WebGL</text>

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

    # 4. Build hyper-animated light.svg
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

    <!-- Holographic Avatar Clip Path -->
    <clipPath id="avatarClipLight">
      <circle cx="250" cy="233" r="72"/>
    </clipPath>

    <!-- Hologram Core Breathing Glow (Light) -->
    <radialGradient id="holoCoreGlowLight" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#7C3AED" stop-opacity="0.25"/>
      <stop offset="85%" stop-color="#DB2777" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="#F8FAFC" stop-opacity="0"/>
    </radialGradient>

    <!-- Animated Hologram Frame Border Gradient (Light) -->
    <linearGradient id="avatarBorderGradLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284C7">
        <animate attributeName="stop-color" values="#0284C7;#7C3AED;#2563EB;#059669;#0284C7" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#4F46E5">
        <animate attributeName="stop-color" values="#4F46E5;#DB2777;#0284C7;#4F46E5;#4F46E5" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#9333EA">
        <animate attributeName="stop-color" values="#9333EA;#0284C7;#7C3AED;#4F46E5;#9333EA" dur="5s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <!-- Hologram Laser Scan Beam Ribbon (Light) -->
    <linearGradient id="hologramSweepGradLight" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0"/>
      <stop offset="50%" stop-color="#2563EB" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#7C3AED" stop-opacity="0"/>
    </linearGradient>

    <!-- Laser Border Beam Gradient (Light) -->
    <linearGradient id="laserBeamLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="35%" stop-color="#7C3AED"/>
      <stop offset="70%" stop-color="#DB2777"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>

    <linearGradient id="borderGradLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB" stop-opacity="0.30"/>
      <stop offset="50%" stop-color="#7C3AED" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#0284C7" stop-opacity="0.25"/>
    </linearGradient>
    <linearGradient id="cardBorderLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB" stop-opacity="0.30"/>
      <stop offset="100%" stop-color="#E2E8F0" stop-opacity="0.80"/>
    </linearGradient>

    <!-- Audio Equalizer Gradient (Light) -->
    <linearGradient id="eqGradLight" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="45%" stop-color="#2563EB"/>
      <stop offset="75%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#E11D48"/>
    </linearGradient>

    <!-- Telemetry Meter Gradients (Light) -->
    <linearGradient id="cyanMeterLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#38BDF8"/>
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
      <stop offset="50%" stop-color="#4F46E5"/>
      <stop offset="100%" stop-color="#7C3AED"/>
    </linearGradient>

    <!-- Grid Pattern (Light) -->
    <pattern id="gridPatternLight" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#CBD5E1" stroke-width="0.75" stroke-opacity="0.38"/>
    </pattern>
  </defs>

  <style>
    .mono {{ font-family: ui-monospace, SFMono-Regular, "Liberation Mono", Menlo, Consolas, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }}
  </style>

  <!-- Root Canvas Background -->
  <rect width="1180" height="610" rx="22" fill="#F8FAFC"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlowLight1)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlowLight2)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlowLight3)"/>
  <rect width="1180" height="610" rx="22" fill="url(#gridPatternLight)"/>

  <!-- Outer Glass Frame Base Border -->
  <rect x="2" y="2" width="1176" height="606" rx="21" fill="none" stroke="url(#borderGradLight)" stroke-width="1.5"/>

  <!-- ANIMATION 1: LASER BORDER SHIMMER (Light) -->
  <rect x="2" y="2" width="1176" height="606" rx="21" fill="none" stroke="url(#laserBeamLight)" stroke-width="2.5" stroke-dasharray="160 580">
    <animate attributeName="stroke-dashoffset" values="0;-740" dur="4.5s" repeatCount="indefinite"/>
  </rect>

  <!-- ==================== LEFT COLUMN: VISUAL / IDENTITY ==================== -->
  <g id="left-column">
    <!-- Left Card Background -->
    <rect x="28" y="28" width="444" height="554" rx="16" fill="#FFFFFF" fill-opacity="0.94" stroke="url(#cardBorderLight)" stroke-width="1.2"/>

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
    <text x="456" y="93" text-anchor="end" class="mono" font-size="9" fill="#059669" font-weight="700">● TARGET LOCK: 99.8%</text>

    <!-- ========================================================================= -->
    <!--     ULTRA-PREMIUM HOLOGRAPHIC QUANTUM AVATAR REACTOR CHAMBER (LIGHT)      -->
    <!-- ========================================================================= -->
    <g id="holographic-avatar-reactor-light">
      <!-- Container Box -->
      <rect x="42" y="104" width="416" height="258" rx="10" fill="#F8FAFC" fill-opacity="0.95" stroke="#CBD5E1" stroke-width="1"/>

      <!-- Ambient Chamber Grid Accent -->
      <line x1="42" y1="170" x2="458" y2="170" stroke="#E2E8F0" stroke-width="0.6" stroke-dasharray="4 6"/>
      <line x1="42" y1="296" x2="458" y2="296" stroke="#E2E8F0" stroke-width="0.6" stroke-dasharray="4 6"/>

      <!-- TOP IDENTIFICATION BADGE -->
      <g transform="translate(160, 112)">
        <rect x="0" y="0" width="180" height="20" rx="10" fill="#EFF6FF" stroke="#2563EB" stroke-width="0.8"/>
        <circle cx="12" cy="10" r="3" fill="#2563EB">
          <animate attributeName="opacity" values="1;0.4;1" dur="1.8s" repeatCount="indefinite"/>
        </circle>
        <text x="22" y="14" class="mono" font-size="8.5" fill="#1E40AF" font-weight="700" letter-spacing="0.5">● HOLOGRAPHIC // DJ ABHI</text>
      </g>

      <!-- ==================== LEFT TELEMETRY SIDECAR (LIGHT) ==================== -->
      <g transform="translate(50, 142)">
        <rect x="0" y="0" width="76" height="182" rx="6" fill="#FFFFFF" fill-opacity="0.95" stroke="#CBD5E1" stroke-width="0.8"/>
        <text x="38" y="16" text-anchor="middle" class="mono" font-size="7.5" fill="#2563EB" font-weight="700">BIO.SENSORS</text>
        <line x1="6" y1="22" x2="70" y2="22" stroke="#E2E8F0" stroke-width="0.8"/>

        <circle cx="12" cy="34" r="2.5" fill="#059669">
          <animate attributeName="opacity" values="1;0.3;1" dur="1.4s" repeatCount="indefinite"/>
        </circle>
        <text x="20" y="37" class="mono" font-size="7" fill="#047857" font-weight="700">AUTH: 100%</text>

        <text x="8" y="56" class="mono" font-size="6.8" fill="#475569" font-weight="600">ID: AG-31</text>
        <text x="8" y="70" class="mono" font-size="6.8" fill="#475569" font-weight="600">22.57° N</text>
        <text x="8" y="84" class="mono" font-size="6.8" fill="#475569" font-weight="600">88.36° E</text>
        <text x="8" y="98" class="mono" font-size="6.8" fill="#475569" font-weight="600">CALCUTTA</text>
        <text x="8" y="112" class="mono" font-size="6.8" fill="#2563EB" font-weight="700">LOCK: 99.8%</text>

        <!-- Mini 4-Bar Biometric Pulse Signal -->
        <g transform="translate(10, 128)">
          <text x="0" y="-4" class="mono" font-size="6" fill="#64748B">PULSE:</text>
          <rect x="0" y="0" width="10" height="28" rx="2" fill="#E2E8F0"/>
          <rect x="0" y="12" width="10" height="16" rx="2" fill="#0284C7">
            <animate attributeName="height" values="16;26;8;22;16" dur="1.8s" repeatCount="indefinite"/>
            <animate attributeName="y" values="12;2;20;6;12" dur="1.8s" repeatCount="indefinite"/>
          </rect>

          <rect x="14" y="0" width="10" height="28" rx="2" fill="#E2E8F0"/>
          <rect x="14" y="6" width="10" height="22" rx="2" fill="#2563EB">
            <animate attributeName="height" values="22;10;28;14;22" dur="1.5s" repeatCount="indefinite"/>
            <animate attributeName="y" values="6;18;0;14;6" dur="1.5s" repeatCount="indefinite"/>
          </rect>

          <rect x="28" y="0" width="10" height="28" rx="2" fill="#E2E8F0"/>
          <rect x="28" y="16" width="10" height="12" rx="2" fill="#7C3AED">
            <animate attributeName="height" values="12;24;6;20;12" dur="2.1s" repeatCount="indefinite"/>
            <animate attributeName="y" values="16;4;22;8;16" dur="2.1s" repeatCount="indefinite"/>
          </rect>

          <rect x="42" y="0" width="10" height="28" rx="2" fill="#E2E8F0"/>
          <rect x="42" y="8" width="10" height="20" rx="2" fill="#9333EA">
            <animate attributeName="height" values="20;14;26;10;20" dur="1.7s" repeatCount="indefinite"/>
            <animate attributeName="y" values="8;14;2;18;8" dur="1.7s" repeatCount="indefinite"/>
          </rect>
        </g>
      </g>

      <!-- ==================== RIGHT TELEMETRY SIDECAR (LIGHT) ==================== -->
      <g transform="translate(374, 142)">
        <rect x="0" y="0" width="76" height="182" rx="6" fill="#FFFFFF" fill-opacity="0.95" stroke="#CBD5E1" stroke-width="0.8"/>
        <text x="38" y="16" text-anchor="middle" class="mono" font-size="7.5" fill="#7C3AED" font-weight="700">NEURAL.LINK</text>
        <line x1="6" y1="22" x2="70" y2="22" stroke="#E2E8F0" stroke-width="0.8"/>

        <circle cx="12" cy="34" r="2.5" fill="#7C3AED">
          <animate attributeName="opacity" values="1;0.3;1" dur="1.8s" repeatCount="indefinite"/>
        </circle>
        <text x="20" y="37" class="mono" font-size="7" fill="#6D28D9" font-weight="700">SYNC: READY</text>

        <text x="8" y="56" class="mono" font-size="6.8" fill="#475569" font-weight="600">140 BPM</text>
        <text x="8" y="70" class="mono" font-size="6.8" fill="#475569" font-weight="600">38K+ AUD</text>
        <text x="8" y="84" class="mono" font-size="6.8" fill="#475569" font-weight="600">GL: 60 FPS</text>
        <text x="8" y="98" class="mono" font-size="6.8" fill="#475569" font-weight="600">WEBGL 2.0</text>
        <text x="8" y="112" class="mono" font-size="6.8" fill="#047857" font-weight="700">ACTIVE CORE</text>

        <!-- Mini 4-Bar Neural Throughput Signal -->
        <g transform="translate(10, 128)">
          <text x="0" y="-4" class="mono" font-size="6" fill="#64748B">THROUGHPUT:</text>
          <rect x="0" y="0" width="10" height="28" rx="2" fill="#E2E8F0"/>
          <rect x="0" y="8" width="10" height="20" rx="2" fill="#7C3AED">
            <animate attributeName="height" values="20;12;26;14;20" dur="1.6s" repeatCount="indefinite"/>
            <animate attributeName="y" values="8;16;2;14;8" dur="1.6s" repeatCount="indefinite"/>
          </rect>

          <rect x="14" y="0" width="10" height="28" rx="2" fill="#E2E8F0"/>
          <rect x="14" y="14" width="10" height="14" rx="2" fill="#DB2777">
            <animate attributeName="height" values="14;26;8;22;14" dur="1.9s" repeatCount="indefinite"/>
            <animate attributeName="y" values="14;2;20;6;14" dur="1.9s" repeatCount="indefinite"/>
          </rect>

          <rect x="28" y="0" width="10" height="28" rx="2" fill="#E2E8F0"/>
          <rect x="28" y="6" width="10" height="22" rx="2" fill="#2563EB">
            <animate attributeName="height" values="22;14;28;10;22" dur="1.4s" repeatCount="indefinite"/>
            <animate attributeName="y" values="6;14;0;18;6" dur="1.4s" repeatCount="indefinite"/>
          </rect>

          <rect x="42" y="0" width="10" height="28" rx="2" fill="#E2E8F0"/>
          <rect x="42" y="12" width="10" height="16" rx="2" fill="#059669">
            <animate attributeName="height" values="16;26;10;24;16" dur="2.0s" repeatCount="indefinite"/>
            <animate attributeName="y" values="12;2;18;4;12" dur="2.0s" repeatCount="indefinite"/>
          </rect>
        </g>
      </g>

      <!-- ==================== CENTER: HOLOGRAPHIC QUANTUM AVATAR (LIGHT) ==================== -->
      <!-- 1. Holographic Breathing Reactor Core Glow -->
      <circle cx="250" cy="233" r="92" fill="url(#holoCoreGlowLight)">
        <animate attributeName="r" values="84;106;84" dur="4s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.45;0.85;0.45" dur="4s" repeatCount="indefinite"/>
      </circle>

      <!-- 2. Dual-Frequency Expanding Quantum Radar/Sonar Waves -->
      <circle cx="250" cy="233" r="74" fill="none" stroke="#2563EB" stroke-width="1.6" opacity="0.8">
        <animate attributeName="r" values="74;128" dur="3.2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.80;0" dur="3.2s" repeatCount="indefinite"/>
      </circle>
      <circle cx="250" cy="233" r="74" fill="none" stroke="#7C3AED" stroke-width="1.6" opacity="0.8">
        <animate attributeName="r" values="74;128" begin="1.6s" dur="3.2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.80;0" begin="1.6s" dur="3.2s" repeatCount="indefinite"/>
      </circle>

      <!-- 3. Gyroscopic HUD Rings (Light) -->
      <!-- Ring A: Outer Compass Ring with Cardinal Ticks (Clockwise, 24s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0 250 233" to="360 250 233" dur="24s" repeatCount="indefinite"/>
        <circle cx="250" cy="233" r="114" fill="none" stroke="#2563EB" stroke-width="1.4" stroke-dasharray="24 12 6 12 36 12" opacity="0.75"/>
        <!-- Cardinal Marks -->
        <polygon points="250,116 247,122 253,122" fill="#2563EB"/>
        <polygon points="250,350 247,344 253,344" fill="#2563EB"/>
        <polygon points="133,233 139,230 139,236" fill="#2563EB"/>
        <polygon points="367,233 361,230 361,236" fill="#2563EB"/>
      </g>

      <!-- Ring B: Segmented Target Arcs (Counter-Clockwise, 14s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="360 250 233" to="0 250 233" dur="14s" repeatCount="indefinite"/>
        <circle cx="250" cy="233" r="100" fill="none" stroke="#7C3AED" stroke-width="2.2" stroke-dasharray="64 92 64 92" stroke-linecap="round" opacity="0.85"/>
      </g>

      <!-- Ring C: Precision Dotted Calibration Track (Clockwise, 36s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0 250 233" to="360 250 233" dur="36s" repeatCount="indefinite"/>
        <circle cx="250" cy="233" r="88" fill="none" stroke="#4F46E5" stroke-width="1.2" stroke-dasharray="3 6" opacity="0.75"/>
      </g>

      <!-- 4. Orbital Satellites (3 Orbiting Quantum Nodes) -->
      <!-- Satellite 1: Sapphire Blue (R=114, 7s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0 250 233" to="360 250 233" dur="7s" repeatCount="indefinite"/>
        <circle cx="250" cy="119" r="3.5" fill="#2563EB"/>
        <circle cx="250" cy="119" r="6" fill="#2563EB" opacity="0.35"/>
      </g>
      <!-- Satellite 2: Royal Purple (R=100, Counter-clockwise, 10s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="360 250 233" to="0 250 233" dur="10s" repeatCount="indefinite"/>
        <circle cx="250" cy="133" r="3" fill="#7C3AED"/>
        <circle cx="250" cy="133" r="5.5" fill="#7C3AED" opacity="0.35"/>
      </g>
      <!-- Satellite 3: Emerald (R=88, 5s) -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0 250 233" to="360 250 233" dur="5s" repeatCount="indefinite"/>
        <circle cx="250" cy="145" r="2.5" fill="#059669"/>
      </g>

      <!-- 5. REAL STUDIO PORTRAIT (Light) -->
      <g id="avatar-core-group-light">
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -2.5; 0 0; 0 2.5; 0 0" dur="4.5s" repeatCount="indefinite"/>
        
        <!-- High-Definition Masked Image -->
        <image href="data:image/jpeg;base64,{b64_avatar}" x="178" y="161" width="144" height="144" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarClipLight)"/>

        <!-- Glowing Neon Reactor Rim -->
        <circle cx="250" cy="233" r="73" fill="none" stroke="url(#avatarBorderGradLight)" stroke-width="2.5"/>

        <!-- Holographic Laser Scanner Sweep (Clipped to Avatar) -->
        <rect x="176" y="159" width="148" height="14" fill="url(#hologramSweepGradLight)" clip-path="url(#avatarClipLight)">
          <animate attributeName="y" values="155;302;155" dur="3.2s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="0.35;0.8;0.35" dur="3.2s" repeatCount="indefinite"/>
        </rect>
        <line x1="176" y1="166" x2="324" y2="166" stroke="#2563EB" stroke-width="1.6" clip-path="url(#avatarClipLight)">
          <animate attributeName="y1" values="162;309;162" dur="3.2s" repeatCount="indefinite"/>
          <animate attributeName="y2" values="162;309;162" dur="3.2s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="0.4;1;0.4" dur="3.2s" repeatCount="indefinite"/>
        </line>
      </g>

      <!-- 6. Cybernetic Corner Tracking Brackets (Light) -->
      <g id="tracking-corners-light" stroke="#2563EB" stroke-width="1.8" fill="none">
        <animate attributeName="stroke" values="#2563EB;#7C3AED;#0284C7;#2563EB" dur="4.5s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.6;1;0.6" dur="2.5s" repeatCount="indefinite"/>
        <!-- Top-Left -->
        <path d="M 188 185 L 188 171 L 202 171"/>
        <!-- Top-Right -->
        <path d="M 312 185 L 312 171 L 298 171"/>
        <!-- Bottom-Left -->
        <path d="M 188 281 L 188 295 L 202 295"/>
        <!-- Bottom-Right -->
        <path d="M 312 281 L 312 295 L 298 295"/>
      </g>

      <!-- Precision Micro-Crosshair Center Ticks -->
      <g stroke="#2563EB" stroke-width="1.2" opacity="0.8">
        <line x1="243" y1="233" x2="247" y2="233"/>
        <line x1="253" y1="233" x2="257" y2="233"/>
        <line x1="250" y1="226" x2="250" y2="230"/>
        <line x1="250" y1="236" x2="250" y2="240"/>
      </g>

      <!-- BOTTOM BIOMETRIC CORE STATUS (Light) -->
      <g transform="translate(160, 334)">
        <rect x="0" y="0" width="180" height="20" rx="10" fill="#F3E8FF" stroke="#7C3AED" stroke-width="0.8"/>
        <circle cx="12" cy="10" r="3" fill="#7C3AED">
          <animate attributeName="opacity" values="1;0.4;1" dur="1.8s" repeatCount="indefinite"/>
        </circle>
        <text x="22" y="14" class="mono" font-size="8" fill="#6D28D9" font-weight="700" letter-spacing="0.5">BIOMETRIC CORE // SECURED</text>
      </g>
    </g>

    <!-- ANIMATION 6: BOUNCING AUDIO EQUALIZER (DJ ABHI - LIGHT) -->
    <g id="audio-equalizer-light">
      <rect x="42" y="372" width="416" height="74" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
      <circle cx="56" cy="386" r="3.5" fill="#E11D48">
        <animate attributeName="opacity" values="1;0.4;1" dur="1s" repeatCount="indefinite"/>
      </circle>
      <text x="66" y="390" class="mono" font-size="9.5" fill="#0F172A" font-weight="700">AUDIO.ENGINE // DJ ABHI SPECTRUM</text>
      <text x="444" y="390" text-anchor="end" class="mono" font-size="8.5" fill="#2563EB" font-weight="700">140 BPM [STEREO]</text>

      <!-- 24 Bouncing Equalizer Bars -->
{eq_light_str}
    </g>

    <!-- Terminal Command Line Prompt (Light) -->
    <rect x="42" y="456" width="416" height="74" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
    <text x="56" y="475" class="mono" font-size="10.5" fill="#2563EB" font-weight="700">~/profile $ <tspan fill="#0F172A">./launch --sound --systems</tspan></text>
    <text x="56" y="494" class="mono" font-size="9.5" fill="#64748B">[OK] 3D_WEBGL: 60FPS · TELEMETRY: REAL-TIME</text>
    <text x="56" y="512" class="mono" font-size="9.5" fill="#64748B">[OK] AUDIO_BASS: ONLINE · COMMUNITY: 38K+</text>
    <rect x="345" y="501" width="7" height="13" fill="#2563EB">
      <animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite"/>
    </rect>

    <!-- Quick Meta Pill -->
    <text x="250" y="555" text-anchor="middle" class="mono" font-size="9" fill="#94A3B8" letter-spacing="1.2">ABHILASH GHOSH // SYSTEM BIO-IDENTITY CORE</text>
  </g>

  <!-- ==================== RIGHT COLUMN: SYSTEM.INFO (LIGHT) ==================== -->
  <g id="right-column-light">
    <!-- Right Card Background -->
    <rect x="490" y="28" width="662" height="554" rx="16" fill="#FFFFFF" fill-opacity="0.94" stroke="url(#cardBorderLight)" stroke-width="1.2"/>

    <!-- Terminal Bar -->
    <circle cx="512" cy="52" r="5" fill="#EF4444"/>
    <circle cx="528" cy="52" r="5" fill="#F59E0B"/>
    <circle cx="544" cy="52" r="5" fill="#10B981"/>
    <text x="564" y="56" class="mono" font-size="11.5" fill="#475569" font-weight="600">SYSTEM.INFO // EXECUTIVE_CORE</text>
    <rect x="1038" y="42" width="98" height="20" rx="10" fill="#EFF6FF" stroke="#2563EB" stroke-width="1"/>
    <text x="1087" y="56" text-anchor="middle" class="mono" font-size="9.5" fill="#1D4ED8" font-weight="700">RELEASE v4.5</text>

    <!-- Header Divider -->
    <line x1="490" y1="74" x2="1152" y2="74" stroke="#E2E8F0" stroke-width="1"/>

    <!-- 1. Identity & Animated Role Section -->
    <g transform="translate(510, 88)">
      <text x="0" y="14" class="mono" font-size="10.5" fill="#2563EB" font-weight="700">djabhi31@station:~$ whoami</text>
      
      <!-- Name -->
      <text x="0" y="44" class="sans" font-size="25" font-weight="800" fill="url(#textGradLight)" letter-spacing="0.5">ABHILASH GHOSH</text>
      <text x="250" y="42" class="mono" font-size="13" fill="#64748B">(@djabhi31)</text>

      <!-- Roles & Badges Row -->
      <g transform="translate(0, 56)">
        <!-- Badge 1: 3D Systems -->
        <rect x="0" y="0" width="170" height="22" rx="11" fill="#EFF6FF" stroke="#2563EB" stroke-width="1"/>
        <circle cx="11" cy="11" r="3.5" fill="#2563EB"/>
        <text x="22" y="15" class="mono" font-size="9.5" fill="#1D4ED8" font-weight="700">3D Systems Engineer</text>

        <!-- Badge 2: Producer / DJ -->
        <rect x="178" y="0" width="168" height="22" rx="11" fill="#FFF1F2" stroke="#E11D48" stroke-width="1"/>
        <circle cx="189" cy="11" r="3.5" fill="#E11D48"/>
        <text x="200" y="15" class="mono" font-size="9.5" fill="#BE123C" font-weight="700">DJ ABHI-Maheshtala</text>

        <!-- Badge 3: Cloud / NASA -->
        <rect x="354" y="0" width="138" height="22" rx="11" fill="#ECFDF5" stroke="#059669" stroke-width="1"/>
        <circle cx="365" cy="11" r="3.5" fill="#059669"/>
        <text x="376" y="15" class="mono" font-size="9.5" fill="#047857" font-weight="700">Cloud Telemetry</text>

        <!-- Badge 4: Location -->
        <rect x="500" y="0" width="122" height="22" rx="11" fill="#F3E8FF" stroke="#7C3AED" stroke-width="1"/>
        <circle cx="511" cy="11" r="3.5" fill="#7C3AED"/>
        <text x="522" y="15" class="mono" font-size="9.5" fill="#6D28D9" font-weight="700">Kolkata, IN</text>
      </g>
    </g>

    <!-- 2. System Architecture / Hardware Gauges (Telemetry Meters - Light) -->
    <g transform="translate(510, 178)">
      <text x="0" y="10" class="mono" font-size="10" fill="#64748B" font-weight="700">SYSTEM ARCHITECTURE TELEMETRY</text>
      
      <!-- Meter 1: WebGL GPU Compute -->
      <g transform="translate(0, 20)">
        <text x="0" y="12" class="mono" font-size="9.5" fill="#475569" font-weight="600">WEBGL 3D COMPUTE (THREE.JS)</text>
        <text x="622" y="12" text-anchor="end" class="mono" font-size="9.5" fill="#0284C7" font-weight="700">60 FPS // ULTRA</text>
        <rect x="0" y="18" width="622" height="6" rx="3" fill="#E2E8F0"/>
        <rect x="0" y="18" width="580" height="6" rx="3" fill="url(#cyanMeterLight)">
          <animate attributeName="width" values="540;590;560;610;580" dur="4s" repeatCount="indefinite"/>
        </rect>
      </g>

      <!-- Meter 2: Cloud Telemetry Link -->
      <g transform="translate(0, 50)">
        <text x="0" y="12" class="mono" font-size="9.5" fill="#475569" font-weight="600">AZURE / NASA EONET DATASTREAM</text>
        <text x="622" y="12" text-anchor="end" class="mono" font-size="9.5" fill="#6D28D9" font-weight="700">42ms // REAL-TIME</text>
        <rect x="0" y="18" width="622" height="6" rx="3" fill="#E2E8F0"/>
        <rect x="0" y="18" width="550" height="6" rx="3" fill="url(#violetMeterLight)">
          <animate attributeName="width" values="520;565;535;580;550" dur="3.5s" repeatCount="indefinite"/>
        </rect>
      </g>

      <!-- Meter 3: Sound Engine & Studio Throughput -->
      <g transform="translate(0, 80)">
        <text x="0" y="12" class="mono" font-size="9.5" fill="#475569" font-weight="600">SOUND MASTERING / DSP ENGINE</text>
        <text x="622" y="12" text-anchor="end" class="mono" font-size="9.5" fill="#047857" font-weight="700">32-BIT FLOAT // 140BPM</text>
        <rect x="0" y="18" width="622" height="6" rx="3" fill="#E2E8F0"/>
        <rect x="0" y="18" width="595" height="6" rx="3" fill="url(#greenMeterLight)">
          <animate attributeName="width" values="580;615;590;620;595" dur="3s" repeatCount="indefinite"/>
        </rect>
      </g>
    </g>

    <!-- 3. Production Deployments Table Grid (Light) -->
    <g transform="translate(510, 290)">
      <text x="0" y="10" class="mono" font-size="10" fill="#64748B" font-weight="700">PRODUCTION DEPLOYMENTS &amp; LIVE PLATFORMS</text>
      
      <!-- Row 1: EarthSphere + God's Eye View -->
      <g transform="translate(0, 20)">
        <!-- Project 1: EarthSphere -->
        <rect x="0" y="0" width="304" height="48" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#0284C7"/>
        <text x="28" y="21" class="sans" font-size="11.5" fill="#0F172A" font-weight="700">EarthSphere</text>
        <rect x="110" y="10" width="56" height="15" rx="7.5" fill="#DCFCE7"/>
        <text x="138" y="21" text-anchor="middle" class="mono" font-size="7.5" fill="#15803D" font-weight="700">LIVE PROD</text>
        <text x="16" y="38" class="mono" font-size="8.5" fill="#64748B">NASA EONET · Next.js 15 · Three.js 3D</text>

        <!-- Project 2: God's Eye View -->
        <rect x="318" y="0" width="304" height="48" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="334" cy="18" r="4" fill="#4F46E5"/>
        <text x="346" y="21" class="sans" font-size="11.5" fill="#0F172A" font-weight="700">God's Eye View</text>
        <rect x="444" y="10" width="66" height="15" rx="7.5" fill="#EFF6FF"/>
        <text x="477" y="21" text-anchor="middle" class="mono" font-size="7.5" fill="#1D4ED8" font-weight="700">AZURE CLOUD</text>
        <text x="334" y="38" class="mono" font-size="8.5" fill="#64748B">Planetary WebGL Console on Azure</text>
      </g>

      <!-- Row 2: ExcuseVerse + Mermaidz Records -->
      <g transform="translate(0, 76)">
        <!-- Project 3: ExcuseVerse -->
        <rect x="0" y="0" width="304" height="48" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#7C3AED"/>
        <text x="28" y="21" class="sans" font-size="11.5" fill="#0F172A" font-weight="700">ExcuseVerse</text>
        <rect x="114" y="10" width="46" height="15" rx="7.5" fill="#F3E8FF"/>
        <text x="137" y="21" text-anchor="middle" class="mono" font-size="7.5" fill="#6D28D9" font-weight="700">AI GEN</text>
        <text x="16" y="38" class="mono" font-size="8.5" fill="#64748B">Context AI Generator · Multi-Lingual</text>

        <!-- Project 4: Mermaidz Records -->
        <rect x="318" y="0" width="304" height="48" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="334" cy="18" r="4" fill="#059669"/>
        <text x="346" y="21" class="sans" font-size="11.5" fill="#0F172A" font-weight="700">Mermaidz Records</text>
        <rect x="466" y="10" width="58" height="15" rx="7.5" fill="#ECFDF5"/>
        <text x="495" y="21" text-anchor="middle" class="mono" font-size="7.5" fill="#047857" font-weight="700">150+ DSPS</text>
        <text x="334" y="38" class="mono" font-size="8.5" fill="#64748B">Global Music Distribution &amp; Label</text>
      </g>
    </g>

    <!-- 4. Core Tech Stack Tags Row (Light) -->
    <g transform="translate(510, 432)">
      <text x="0" y="10" class="mono" font-size="10" fill="#64748B" font-weight="700">CORE ARSENAL PILLARS</text>
      
      <g transform="translate(0, 18)">
        <!-- Next.js 15 -->
        <rect x="0" y="0" width="112" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="10" cy="11" r="3" fill="#0284C7"/>
        <text x="20" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">Next.js 15</text>

        <!-- Three.js -->
        <rect x="122" y="0" width="112" height="22" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="132" cy="11" r="3" fill="#7C3AED"/>
        <text x="142" y="15" class="mono" font-size="9" fill="#0F172A" font-weight="600">Three.js / WebGL</text>

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

    <!-- 5. Terminal Connect & Footer Bar (Light) -->
    <g transform="translate(510, 482)">
      <rect x="0" y="0" width="622" height="62" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
      <circle cx="18" cy="18" r="3" fill="#0284C7"/>
      <text x="28" y="21" class="mono" font-size="10" fill="#0284C7" font-weight="700">&gt; ECOSYSTEM &amp; CONNECT MATRIX</text>
      
      <text x="28" y="38" class="mono" font-size="9" fill="#0F172A">
        <tspan fill="#64748B">WEB:</tspan> abhilashghosh.pages.dev <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">YT:</tspan> @djabhimaheshtala (38K+) <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">SPOTIFY:</tspan> DJ ABHI
      </text>
      
      <text x="28" y="52" class="mono" font-size="9" fill="#0F172A">
        <tspan fill="#64748B">GH:</tspan> github.com/djabhi31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">X:</tspan> @DjAbhi31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">IG:</tspan> @djabhi.31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">MAIL:</tspan> abhilashghosh31@gmail.com
      </text>
    </g>

    <!-- Bottom Meta Tagline -->
    <text x="821" y="562" text-anchor="middle" class="mono" font-size="8.5" fill="#64748B" letter-spacing="1.2">SYSTEM STATUS: FULLY OPERATIONAL // KERNEL RUNNING</text>
  </g>
</svg>'''

    # Validate XML Syntax
    try:
        ET.fromstring(dark_svg)
        print("dark_svg is VALID XML")
    except Exception as e:
        print(f"Error parsing dark_svg: {e}")
        raise

    try:
        ET.fromstring(light_svg)
        print("light_svg is VALID XML")
    except Exception as e:
        print(f"Error parsing light_svg: {e}")
        raise

    with open('dark.svg', 'w', encoding='utf-8') as f:
        f.write(dark_svg)
    print(f"dark.svg generated successfully ({os.path.getsize('dark.svg')} bytes)")

    with open('light.svg', 'w', encoding='utf-8') as f:
        f.write(light_svg)
    print(f"light.svg generated successfully ({os.path.getsize('light.svg')} bytes)")

if __name__ == '__main__':
    generate_svgs()
