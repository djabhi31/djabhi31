import os
from PIL import Image, ImageEnhance
import xml.etree.ElementTree as ET

def generate_svgs():
    # 1. Load avatar and extract ASCII characters
    avatar_path = 'avatar.png'
    if not os.path.exists(avatar_path):
        raise FileNotFoundError(f"Avatar file not found at {avatar_path}")
        
    img = Image.open(avatar_path).convert('L')
    tw, th = 50, 32
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
    dy = 8.8
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

    # 2. Build dark.svg
    dark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610" role="img" aria-label="Abhilash Ghosh (@djabhi31) - Full-Stack Engineer, 3D Web &amp; Creative Technologist">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="bgGlow1" cx="20%" cy="15%" r="65%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#030712" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlow2" cx="85%" cy="85%" r="60%">
      <stop offset="0%" stop-color="#7C3AED" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#030712" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlow3" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#059669" stop-opacity="0.12"/>
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
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#818CF8" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#C084FC" stop-opacity="0.4"/>
    </linearGradient>
    <linearGradient id="cardBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="scanlineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0"/>
      <stop offset="50%" stop-color="#22D3EE" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#818CF8"/>
      <stop offset="100%" stop-color="#C084FC"/>
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="gridPattern" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#334155" stroke-width="0.75" stroke-opacity="0.22"/>
    </pattern>

    <!-- Glow Filter -->
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    .mono {{ font-family: ui-monospace, SFMono-Regular, "Liberation Mono", Menlo, Consolas, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }}
    .ascii {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 7.4px; font-weight: 700; letter-spacing: 0.8px; fill: #38BDF8; }}
  </style>

  <!-- Root Canvas Background -->
  <rect width="1180" height="610" rx="22" fill="#030712"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlow1)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlow2)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlow3)"/>
  <rect width="1180" height="610" rx="22" fill="url(#gridPattern)"/>

  <!-- Outer Glass Frame Border -->
  <rect x="2" y="2" width="1176" height="606" rx="21" fill="none" stroke="url(#borderGrad)" stroke-width="1.5"/>

  <!-- ==================== LEFT COLUMN: VISUAL / IDENTITY ==================== -->
  <g id="left-column">
    <!-- Left Card Background -->
    <rect x="28" y="28" width="444" height="554" rx="16" fill="#0B1220" fill-opacity="0.82" stroke="url(#cardBorder)" stroke-width="1.2"/>

    <!-- Terminal Window Bar -->
    <circle cx="50" cy="52" r="5" fill="#EF4444"/>
    <circle cx="66" cy="52" r="5" fill="#F59E0B"/>
    <circle cx="82" cy="52" r="5" fill="#10B981"/>
    <text x="104" y="56" class="mono" font-size="11.5" fill="#94A3B8" font-weight="500">djabhi31@developer:~ (visual.id)</text>
    
    <!-- Status Pill -->
    <rect x="364" y="42" width="92" height="20" rx="10" fill="#10B981" fill-opacity="0.12" stroke="#10B981" stroke-width="1"/>
    <circle cx="376" cy="52" r="3.5" fill="#10B981">
      <animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="386" y="56" class="mono" font-size="10" fill="#34D399" font-weight="600">ONLINE</text>

    <!-- Header Divider -->
    <line x1="28" y1="74" x2="472" y2="74" stroke="#1E293B" stroke-width="1"/>

    <!-- Biometric ID Bar -->
    <text x="44" y="94" class="mono" font-size="10.5" fill="#38BDF8" font-weight="600" letter-spacing="1">VISUAL.MAP // BIO-TELEMETRY</text>
    <text x="456" y="94" text-anchor="end" class="mono" font-size="9" fill="#64748B">MATRIX: 50x32 CHR</text>

    <!-- ASCII Portrait Container Box -->
    <rect x="42" y="105" width="416" height="312" rx="10" fill="#040914" fill-opacity="0.92" stroke="#1E293B" stroke-width="1"/>

    <!-- ASCII Character Stream -->
    <text class="ascii" text-anchor="middle">
{tspans_dark_str}
    </text>

    <!-- Animated Scanline -->
    <line x1="43" y1="106" x2="457" y2="106" stroke="url(#scanlineGrad)" stroke-width="2.5" opacity="0.75">
      <animate attributeName="y1" values="108;412;108" dur="5.5s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="108;412;108" dur="5.5s" repeatCount="indefinite"/>
    </line>

    <!-- Telemetry Status Badges -->
    <g transform="translate(42, 428)">
      <rect x="0" y="0" width="132" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
      <text x="66" y="16" text-anchor="middle" class="mono" font-size="9" fill="#94A3B8">SYS: <tspan fill="#38BDF8" font-weight="600">NOMINAL</tspan></text>

      <rect x="142" y="0" width="132" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
      <text x="208" y="16" text-anchor="middle" class="mono" font-size="9" fill="#94A3B8">LOC: <tspan fill="#F8FAFC" font-weight="600">22.57°N, 88°E</tspan></text>

      <rect x="284" y="0" width="132" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
      <text x="350" y="16" text-anchor="middle" class="mono" font-size="9" fill="#94A3B8">FANS: <tspan fill="#A855F7" font-weight="600">38K+ YOUTUBE</tspan></text>
    </g>

    <!-- Terminal Command Line Prompt -->
    <rect x="42" y="462" width="416" height="54" rx="10" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
    <text x="56" y="484" class="mono" font-size="11" fill="#38BDF8" font-weight="600">~/profile $ <tspan fill="#F8FAFC">./ship --production</tspan></text>
    <text x="56" y="504" class="mono" font-size="10" fill="#94A3B8">&gt;&gt; REAL-TIME 3D SYSTEMS &amp; BEATS ARMED</text>
    <rect x="330" y="493" width="7" height="12" fill="#38BDF8">
      <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
    </rect>

    <!-- Quick Meta Pill -->
    <text x="250" y="555" text-anchor="middle" class="mono" font-size="9" fill="#475569" letter-spacing="1.2">ABHILASH GHOSH // DEV IDENTITY ENGINE</text>
  </g>

  <!-- ==================== RIGHT COLUMN: SYSTEM.INFO ==================== -->
  <g id="right-column">
    <!-- Right Card Background -->
    <rect x="490" y="28" width="662" height="554" rx="16" fill="#0B1220" fill-opacity="0.82" stroke="url(#cardBorder)" stroke-width="1.2"/>

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
      <text x="0" y="14" class="mono" font-size="11" fill="#38BDF8" font-weight="600">djabhi31@station:~$ whoami</text>
      
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
    <g transform="translate(510, 204)">
      <text x="0" y="0" class="mono" font-size="10.5" fill="#38BDF8" font-weight="600" letter-spacing="1">// PRODUCTION BUILDS &amp; PLATFORMS</text>
      
      <!-- Project 1: EarthSphere -->
      <g transform="translate(0, 10)">
        <rect x="0" y="0" width="304" height="58" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#38BDF8"/>
        <text x="28" y="21" class="sans" font-size="12" font-weight="700" fill="#F8FAFC">EarthSphere</text>
        <rect x="110" y="10" width="62" height="15" rx="7.5" fill="#0284C7" fill-opacity="0.25"/>
        <text x="141" y="21" text-anchor="middle" class="mono" font-size="8" fill="#38BDF8" font-weight="600">LIVE PROD</text>
        <text x="14" y="37" class="sans" font-size="9.5" fill="#94A3B8">Real-time planetary event intelligence via NASA EONET</text>
        <text x="14" y="50" class="mono" font-size="8.5" fill="#38BDF8">Next.js 15 · Three.js · WebGL · MapLibre GL</text>
      </g>

      <!-- Project 2: God's Eye View -->
      <g transform="translate(318, 10)">
        <rect x="0" y="0" width="304" height="58" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#A855F7"/>
        <text x="28" y="21" class="sans" font-size="12" font-weight="700" fill="#F8FAFC">God's Eye View</text>
        <rect x="134" y="10" width="64" height="15" rx="7.5" fill="#7C3AED" fill-opacity="0.25"/>
        <text x="166" y="21" text-anchor="middle" class="mono" font-size="8" fill="#C084FC" font-weight="600">AZURE CLOUD</text>
        <text x="14" y="37" class="sans" font-size="9.5" fill="#94A3B8">Real-time 3D planetary intelligence console</text>
        <text x="14" y="50" class="mono" font-size="8.5" fill="#A855F7">Microsoft Azure · WebGL · 3D Engine · Cloud</text>
      </g>

      <!-- Project 3: ExcuseVerse -->
      <g transform="translate(0, 76)">
        <rect x="0" y="0" width="304" height="58" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#F59E0B"/>
        <text x="28" y="21" class="sans" font-size="12" font-weight="700" fill="#F8FAFC">ExcuseVerse</text>
        <rect x="114" y="10" width="58" height="15" rx="7.5" fill="#D97706" fill-opacity="0.25"/>
        <text x="143" y="21" text-anchor="middle" class="mono" font-size="8" fill="#FBBF24" font-weight="600">AI APP</text>
        <text x="14" y="37" class="sans" font-size="9.5" fill="#94A3B8">AI situational generator with 2,500+ dynamic excuses</text>
        <text x="14" y="50" class="mono" font-size="8.5" fill="#FBBF24">AI Integration · Next.js · Multi-Lingual UX</text>
      </g>

      <!-- Project 4: Mermaidz Records -->
      <g transform="translate(318, 76)">
        <rect x="0" y="0" width="304" height="58" rx="8" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#10B981"/>
        <text x="28" y="21" class="sans" font-size="12" font-weight="700" fill="#F8FAFC">Mermaidz Records</text>
        <rect x="148" y="10" width="60" height="15" rx="7.5" fill="#059669" fill-opacity="0.25"/>
        <text x="178" y="21" text-anchor="middle" class="mono" font-size="8" fill="#34D399" font-weight="600">LABEL</text>
        <text x="14" y="37" class="sans" font-size="9.5" fill="#94A3B8">Music publishing &amp; distribution brand for indie artists</text>
        <text x="14" y="50" class="mono" font-size="8.5" fill="#34D399">150+ Global Stores · Royalties &amp; Rights</text>
      </g>
    </g>

    <!-- 3. Technical Stack Pills Grid -->
    <g transform="translate(510, 356)">
      <text x="0" y="0" class="mono" font-size="10.5" fill="#38BDF8" font-weight="600" letter-spacing="1">// TECHNICAL ARSENAL &amp; CORE STACK</text>
      
      <!-- Row 1 -->
      <g transform="translate(0, 10)">
        <!-- Next.js 15 -->
        <rect x="0" y="0" width="98" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="10" cy="12" r="3" fill="#38BDF8"/>
        <text x="20" y="16" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="500">Next.js 15</text>

        <!-- React 19 -->
        <rect x="105" y="0" width="96" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="115" cy="12" r="3" fill="#22D3EE"/>
        <text x="125" y="16" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="500">React 19</text>

        <!-- Three.js -->
        <rect x="208" y="0" width="94" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="218" cy="12" r="3" fill="#A855F7"/>
        <text x="228" y="16" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="500">Three.js</text>

        <!-- WebGL -->
        <rect x="309" y="0" width="86" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="319" cy="12" r="3" fill="#EC4899"/>
        <text x="329" y="16" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="500">WebGL</text>

        <!-- TypeScript -->
        <rect x="402" y="0" width="104" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="412" cy="12" r="3" fill="#3B82F6"/>
        <text x="422" y="16" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="500">TypeScript</text>

        <!-- Python -->
        <rect x="513" y="0" width="88" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="523" cy="12" r="3" fill="#EAB308"/>
        <text x="533" y="16" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="500">Python</text>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 40)">
        <!-- TailwindCSS -->
        <rect x="0" y="0" width="112" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="10" cy="12" r="3" fill="#06B6D4"/>
        <text x="20" y="16" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="500">TailwindCSS</text>

        <!-- Azure -->
        <rect x="119" y="0" width="118" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="129" cy="12" r="3" fill="#0284C7"/>
        <text x="139" y="16" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="500">Microsoft Azure</text>

        <!-- MapLibre GL -->
        <rect x="244" y="0" width="112" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="254" cy="12" r="3" fill="#10B981"/>
        <text x="264" y="16" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="500">MapLibre GL</text>

        <!-- GitHub Actions -->
        <rect x="363" y="0" width="124" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="373" cy="12" r="3" fill="#818CF8"/>
        <text x="383" y="16" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="500">GitHub Actions</text>

        <!-- FL Studio -->
        <rect x="494" y="0" width="106" height="24" rx="6" fill="#0F172A" stroke="#1E293B" stroke-width="1"/>
        <circle cx="504" cy="12" r="3" fill="#F97316"/>
        <text x="514" y="16" class="mono" font-size="9.5" fill="#F8FAFC" font-weight="500">FL Studio</text>
      </g>
    </g>

    <!-- 4. Terminal Connect & Footer Bar -->
    <g transform="translate(510, 442)">
      <rect x="0" y="0" width="622" height="88" rx="10" fill="#070D1A" stroke="#1E293B" stroke-width="1"/>
      <circle cx="18" cy="24" r="3" fill="#38BDF8"/>
      <text x="28" y="27" class="mono" font-size="11" fill="#38BDF8" font-weight="600">&gt; ECOSYSTEM &amp; CONNECT MATRIX</text>
      
      <text x="28" y="48" class="mono" font-size="9.5" fill="#F8FAFC">
        <tspan fill="#64748B">WEB:</tspan> abhilashghosh.pages.dev <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">YT:</tspan> @djabhimaheshtala (38K+) <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">SPOTIFY:</tspan> DJ ABHI
      </text>
      
      <text x="28" y="68" class="mono" font-size="9.5" fill="#F8FAFC">
        <tspan fill="#64748B">GH:</tspan> github.com/djabhi31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">X:</tspan> @DjAbhi31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">IG:</tspan> @djabhi.31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">MAIL:</tspan> abhilashghosh31@gmail.com
      </text>
    </g>

    <!-- Bottom Meta Tagline -->
    <text x="821" y="555" text-anchor="middle" class="mono" font-size="9" fill="#475569" letter-spacing="1.2">SYSTEM STATUS: FULLY OPERATIONAL // KERNEL RUNNING</text>
  </g>
</svg>'''

    # 3. Build light.svg (Truly designed light theme!)
    light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610" role="img" aria-label="Abhilash Ghosh (@djabhi31) - Full-Stack Engineer, 3D Web &amp; Creative Technologist">
  <defs>
    <!-- Background Gradients (Light) -->
    <radialGradient id="bgGlowLight1" cx="20%" cy="15%" r="65%">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="#F8FAFC" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlowLight2" cx="85%" cy="85%" r="60%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#F8FAFC" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="bgGlowLight3" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#F8FAFC" stop-opacity="0"/>
    </radialGradient>

    <!-- Accent Linear Gradients -->
    <linearGradient id="blueLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="100%" stop-color="#1D4ED8"/>
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
    <linearGradient id="scanlineGradLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563EB" stop-opacity="0"/>
      <stop offset="50%" stop-color="#2563EB" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#2563EB" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="textGradLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="50%" stop-color="#4338CA"/>
      <stop offset="100%" stop-color="#6B21A8"/>
    </linearGradient>

    <!-- Grid Pattern (Light) -->
    <pattern id="gridPatternLight" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#94A3B8" stroke-width="0.75" stroke-opacity="0.2"/>
    </pattern>

    <!-- Card Shadow -->
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <style>
    .mono {{ font-family: ui-monospace, SFMono-Regular, "Liberation Mono", Menlo, Consolas, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }}
    .ascii-light {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 7.4px; font-weight: 700; letter-spacing: 0.8px; fill: #1E293B; }}
  </style>

  <!-- Root Canvas Background -->
  <rect width="1180" height="610" rx="22" fill="#F8FAFC"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlowLight1)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlowLight2)"/>
  <rect width="1180" height="610" rx="22" fill="url(#bgGlowLight3)"/>
  <rect width="1180" height="610" rx="22" fill="url(#gridPatternLight)"/>

  <!-- Outer Glass Frame Border -->
  <rect x="2" y="2" width="1176" height="606" rx="21" fill="none" stroke="url(#borderGradLight)" stroke-width="1.5"/>

  <!-- ==================== LEFT COLUMN: VISUAL / IDENTITY ==================== -->
  <g id="left-column">
    <!-- Left Card Background -->
    <rect x="28" y="28" width="444" height="554" rx="16" fill="#FFFFFF" fill-opacity="0.94" stroke="url(#cardBorderLight)" stroke-width="1.2" filter="url(#cardShadow)"/>

    <!-- Terminal Window Bar -->
    <circle cx="50" cy="52" r="5" fill="#EF4444"/>
    <circle cx="66" cy="52" r="5" fill="#F59E0B"/>
    <circle cx="82" cy="52" r="5" fill="#10B981"/>
    <text x="104" y="56" class="mono" font-size="11.5" fill="#475569" font-weight="600">djabhi31@developer:~ (visual.id)</text>
    
    <!-- Status Pill -->
    <rect x="364" y="42" width="92" height="20" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="1"/>
    <circle cx="376" cy="52" r="3.5" fill="#10B981">
      <animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="386" y="56" class="mono" font-size="10" fill="#065F46" font-weight="700">ONLINE</text>

    <!-- Header Divider -->
    <line x1="28" y1="74" x2="472" y2="74" stroke="#E2E8F0" stroke-width="1"/>

    <!-- Biometric ID Bar -->
    <text x="44" y="94" class="mono" font-size="10.5" fill="#2563EB" font-weight="700" letter-spacing="1">VISUAL.MAP // BIO-TELEMETRY</text>
    <text x="456" y="94" text-anchor="end" class="mono" font-size="9" fill="#64748B">MATRIX: 50x32 CHR</text>

    <!-- ASCII Portrait Container Box -->
    <rect x="42" y="105" width="416" height="312" rx="10" fill="#F1F5F9" fill-opacity="0.95" stroke="#CBD5E1" stroke-width="1"/>

    <!-- ASCII Character Stream -->
    <text class="ascii-light" text-anchor="middle">
{tspans_light_str}
    </text>

    <!-- Animated Scanline -->
    <line x1="43" y1="106" x2="457" y2="106" stroke="url(#scanlineGradLight)" stroke-width="2.5" opacity="0.65">
      <animate attributeName="y1" values="108;412;108" dur="5.5s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="108;412;108" dur="5.5s" repeatCount="indefinite"/>
    </line>

    <!-- Telemetry Status Badges -->
    <g transform="translate(42, 428)">
      <rect x="0" y="0" width="132" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="66" y="16" text-anchor="middle" class="mono" font-size="9" fill="#475569">SYS: <tspan fill="#2563EB" font-weight="700">NOMINAL</tspan></text>

      <rect x="142" y="0" width="132" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="208" y="16" text-anchor="middle" class="mono" font-size="9" fill="#475569">LOC: <tspan fill="#0F172A" font-weight="700">22.57°N, 88°E</tspan></text>

      <rect x="284" y="0" width="132" height="24" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="350" y="16" text-anchor="middle" class="mono" font-size="9" fill="#475569">FANS: <tspan fill="#7C3AED" font-weight="700">38K+ YOUTUBE</tspan></text>
    </g>

    <!-- Terminal Command Line Prompt -->
    <rect x="42" y="462" width="416" height="54" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
    <text x="56" y="484" class="mono" font-size="11" fill="#2563EB" font-weight="700">~/profile $ <tspan fill="#0F172A">./ship --production</tspan></text>
    <text x="56" y="504" class="mono" font-size="10" fill="#475569">&gt;&gt; REAL-TIME 3D SYSTEMS &amp; BEATS ARMED</text>
    <rect x="330" y="493" width="7" height="12" fill="#2563EB">
      <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
    </rect>

    <!-- Quick Meta Pill -->
    <text x="250" y="555" text-anchor="middle" class="mono" font-size="9" fill="#94A3B8" letter-spacing="1.2">ABHILASH GHOSH // DEV IDENTITY ENGINE</text>
  </g>

  <!-- ==================== RIGHT COLUMN: SYSTEM.INFO ==================== -->
  <g id="right-column">
    <!-- Right Card Background -->
    <rect x="490" y="28" width="662" height="554" rx="16" fill="#FFFFFF" fill-opacity="0.94" stroke="url(#cardBorderLight)" stroke-width="1.2" filter="url(#cardShadow)"/>

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
      <text x="0" y="14" class="mono" font-size="11" fill="#2563EB" font-weight="700">djabhi31@station:~$ whoami</text>
      
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
    <g transform="translate(510, 204)">
      <text x="0" y="0" class="mono" font-size="10.5" fill="#2563EB" font-weight="700" letter-spacing="1">// PRODUCTION BUILDS &amp; PLATFORMS</text>
      
      <!-- Project 1: EarthSphere -->
      <g transform="translate(0, 10)">
        <rect x="0" y="0" width="304" height="58" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#0284C7"/>
        <text x="28" y="21" class="sans" font-size="12" font-weight="700" fill="#0F172A">EarthSphere</text>
        <rect x="110" y="10" width="62" height="15" rx="7.5" fill="#E0F2FE"/>
        <text x="141" y="21" text-anchor="middle" class="mono" font-size="8" fill="#0369A1" font-weight="700">LIVE PROD</text>
        <text x="14" y="37" class="sans" font-size="9.5" fill="#475569">Real-time planetary event intelligence via NASA EONET</text>
        <text x="14" y="50" class="mono" font-size="8.5" fill="#0284C7">Next.js 15 · Three.js · WebGL · MapLibre GL</text>
      </g>

      <!-- Project 2: God's Eye View -->
      <g transform="translate(318, 10)">
        <rect x="0" y="0" width="304" height="58" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#7C3AED"/>
        <text x="28" y="21" class="sans" font-size="12" font-weight="700" fill="#0F172A">God's Eye View</text>
        <rect x="134" y="10" width="64" height="15" rx="7.5" fill="#F3E8FF"/>
        <text x="166" y="21" text-anchor="middle" class="mono" font-size="8" fill="#7E22CE" font-weight="700">AZURE CLOUD</text>
        <text x="14" y="37" class="sans" font-size="9.5" fill="#475569">Real-time 3D planetary intelligence console</text>
        <text x="14" y="50" class="mono" font-size="8.5" fill="#7C3AED">Microsoft Azure · WebGL · 3D Engine · Cloud</text>
      </g>

      <!-- Project 3: ExcuseVerse -->
      <g transform="translate(0, 76)">
        <rect x="0" y="0" width="304" height="58" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#D97706"/>
        <text x="28" y="21" class="sans" font-size="12" font-weight="700" fill="#0F172A">ExcuseVerse</text>
        <rect x="114" y="10" width="58" height="15" rx="7.5" fill="#FEF3C7"/>
        <text x="143" y="21" text-anchor="middle" class="mono" font-size="8" fill="#B45309" font-weight="700">AI APP</text>
        <text x="14" y="37" class="sans" font-size="9.5" fill="#475569">AI situational generator with 2,500+ dynamic excuses</text>
        <text x="14" y="50" class="mono" font-size="8.5" fill="#D97706">AI Integration · Next.js · Multi-Lingual UX</text>
      </g>

      <!-- Project 4: Mermaidz Records -->
      <g transform="translate(318, 76)">
        <rect x="0" y="0" width="304" height="58" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="16" cy="18" r="4" fill="#059669"/>
        <text x="28" y="21" class="sans" font-size="12" font-weight="700" fill="#0F172A">Mermaidz Records</text>
        <rect x="148" y="10" width="60" height="15" rx="7.5" fill="#D1FAE5"/>
        <text x="178" y="21" text-anchor="middle" class="mono" font-size="8" fill="#047857" font-weight="700">LABEL</text>
        <text x="14" y="37" class="sans" font-size="9.5" fill="#475569">Music publishing &amp; distribution brand for indie artists</text>
        <text x="14" y="50" class="mono" font-size="8.5" fill="#059669">150+ Global Stores · Royalties &amp; Rights</text>
      </g>
    </g>

    <!-- 3. Technical Stack Pills Grid -->
    <g transform="translate(510, 356)">
      <text x="0" y="0" class="mono" font-size="10.5" fill="#2563EB" font-weight="700" letter-spacing="1">// TECHNICAL ARSENAL &amp; CORE STACK</text>
      
      <!-- Row 1 -->
      <g transform="translate(0, 10)">
        <!-- Next.js 15 -->
        <rect x="0" y="0" width="98" height="24" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="10" cy="12" r="3" fill="#0284C7"/>
        <text x="20" y="16" class="mono" font-size="9.5" fill="#0F172A" font-weight="600">Next.js 15</text>

        <!-- React 19 -->
        <rect x="105" y="0" width="96" height="24" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="115" cy="12" r="3" fill="#06B6D4"/>
        <text x="125" y="16" class="mono" font-size="9.5" fill="#0F172A" font-weight="600">React 19</text>

        <!-- Three.js -->
        <rect x="208" y="0" width="94" height="24" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="218" cy="12" r="3" fill="#7C3AED"/>
        <text x="228" y="16" class="mono" font-size="9.5" fill="#0F172A" font-weight="600">Three.js</text>

        <!-- WebGL -->
        <rect x="309" y="0" width="86" height="24" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="319" cy="12" r="3" fill="#DB2777"/>
        <text x="329" y="16" class="mono" font-size="9.5" fill="#0F172A" font-weight="600">WebGL</text>

        <!-- TypeScript -->
        <rect x="402" y="0" width="104" height="24" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="412" cy="12" r="3" fill="#2563EB"/>
        <text x="422" y="16" class="mono" font-size="9.5" fill="#0F172A" font-weight="600">TypeScript</text>

        <!-- Python -->
        <rect x="513" y="0" width="88" height="24" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="523" cy="12" r="3" fill="#CA8A04"/>
        <text x="533" y="16" class="mono" font-size="9.5" fill="#0F172A" font-weight="600">Python</text>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 40)">
        <!-- TailwindCSS -->
        <rect x="0" y="0" width="112" height="24" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="10" cy="12" r="3" fill="#0891B2"/>
        <text x="20" y="16" class="mono" font-size="9.5" fill="#0F172A" font-weight="600">TailwindCSS</text>

        <!-- Azure -->
        <rect x="119" y="0" width="118" height="24" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="129" cy="12" r="3" fill="#0284C7"/>
        <text x="139" y="16" class="mono" font-size="9.5" fill="#0F172A" font-weight="600">Microsoft Azure</text>

        <!-- MapLibre GL -->
        <rect x="244" y="0" width="112" height="24" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="254" cy="12" r="3" fill="#059669"/>
        <text x="264" y="16" class="mono" font-size="9.5" fill="#0F172A" font-weight="600">MapLibre GL</text>

        <!-- GitHub Actions -->
        <rect x="363" y="0" width="124" height="24" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="373" cy="12" r="3" fill="#4F46E5"/>
        <text x="383" y="16" class="mono" font-size="9.5" fill="#0F172A" font-weight="600">GitHub Actions</text>

        <!-- FL Studio -->
        <rect x="494" y="0" width="106" height="24" rx="6" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
        <circle cx="504" cy="12" r="3" fill="#EA580C"/>
        <text x="514" y="16" class="mono" font-size="9.5" fill="#0F172A" font-weight="600">FL Studio</text>
      </g>
    </g>

    <!-- 4. Terminal Connect & Footer Bar -->
    <g transform="translate(510, 442)">
      <rect x="0" y="0" width="622" height="88" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="18" cy="24" r="3" fill="#2563EB"/>
      <text x="28" y="27" class="mono" font-size="11" fill="#2563EB" font-weight="700">&gt; ECOSYSTEM &amp; CONNECT MATRIX</text>
      
      <text x="28" y="48" class="mono" font-size="9.5" fill="#0F172A">
        <tspan fill="#64748B">WEB:</tspan> abhilashghosh.pages.dev <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">YT:</tspan> @djabhimaheshtala (38K+) <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">SPOTIFY:</tspan> DJ ABHI
      </text>
      
      <text x="28" y="68" class="mono" font-size="9.5" fill="#0F172A">
        <tspan fill="#64748B">GH:</tspan> github.com/djabhi31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">X:</tspan> @DjAbhi31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">IG:</tspan> @djabhi.31 <tspan fill="#64748B">|</tspan> <tspan fill="#64748B">MAIL:</tspan> abhilashghosh31@gmail.com
      </text>
    </g>

    <!-- Bottom Meta Tagline -->
    <text x="821" y="555" text-anchor="middle" class="mono" font-size="9" fill="#94A3B8" letter-spacing="1.2">SYSTEM STATUS: FULLY OPERATIONAL // KERNEL RUNNING</text>
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
