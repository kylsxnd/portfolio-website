from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# Route untuk serve static files (foto dan video)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/foto_cv/<path:filename>')
def serve_foto_cv(filename):
    return send_from_directory('foto cv', filename)

@app.route('/video/<path:filename>')
def serve_video(filename):
    return send_from_directory('video', filename)

# Template HTML untuk website portfolio
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ nama }} - Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header */
        header {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: white;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            transition: all 0.3s ease;
            padding: 0.5rem 1rem;
            border-radius: 20px;
        }

        .nav-links a:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-2px);
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            padding-top: 80px;
        }

        .hero-content {
            animation: fadeInUp 1s ease-out;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }

        .btn {
            display: inline-block;
            padding: 12px 30px;
            background: rgba(255, 255, 255, 0.2);
            color: white;
            text-decoration: none;
            border-radius: 50px;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        .btn:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }

        /* About Section */
        .about {
            background: white;
            padding: 80px 0;
        }

        .section-title {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: #333;
        }

        .about-content {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 3rem;
            align-items: center;
        }

        .about-text {
            font-size: 1.1rem;
            line-height: 1.8;
        }

        .profile-img {
            width: 250px;
            height: 250px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 4rem;
            margin: 0 auto;
        }

        /* Experience Section */
        .experience {
            background: #f8f9fa;
            padding: 80px 0;
        }

        .experience-timeline {
            position: relative;
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem 0;
        }

        .experience-timeline::after {
            content: '';
            position: absolute;
            width: 4px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -2px;
            border-radius: 2px;
        }

        .experience-item {
            padding: 10px 40px;
            position: relative;
            background-color: inherit;
            width: 50%;
            margin-bottom: 2rem;
        }

        .experience-item::after {
            content: '';
            position: absolute;
            width: 20px;
            height: 20px;
            right: -10px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border: 4px solid #f8f9fa;
            top: 25px;
            border-radius: 50%;
            z-index: 1;
        }

        .experience-item:nth-child(even) {
            left: 50%;
        }

        .experience-item:nth-child(even)::after {
            left: -10px;
        }

        .experience-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            position: relative;
        }

        .experience-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        }

        .experience-card::before {
            content: '';
            position: absolute;
            width: 0;
            height: 0;
            top: 25px;
            right: -15px;
            border: 15px solid transparent;
            border-left-color: white;
        }

        .experience-item:nth-child(even) .experience-card::before {
            left: -15px;
            border-left-color: transparent;
            border-right-color: white;
        }

        .experience-header {
            margin-bottom: 1rem;
        }

        .experience-title {
            color: #667eea;
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        .experience-company {
            color: #333;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .experience-period {
            color: #666;
            font-size: 0.9rem;
            font-style: italic;
            margin-bottom: 0.5rem;
        }

        .experience-location {
            color: #888;
            font-size: 0.9rem;
        }

        .experience-description {
            color: #555;
            line-height: 1.6;
            margin-top: 1rem;
        }

        .experience-achievements {
            margin-top: 1rem;
        }

        .experience-achievements ul {
            list-style: none;
            padding-left: 0;
        }

        .experience-achievements li {
            position: relative;
            padding-left: 1.5rem;
            margin-bottom: 0.5rem;
            color: #555;
        }

        .experience-achievements li::before {
            content: '✓';
            position: absolute;
            left: 0;
            color: #667eea;
            font-weight: bold;
        }

        /* Skills Section */
        .skills {
            background: white;
            padding: 80px 0;
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .skill-card {
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .skill-card:hover {
            transform: translateY(-5px);
        }

        /* Projects Section */
        .projects {
            background: #f8f9fa;
            padding: 80px 0;
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .project-card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            min-height: 400px;
        }

        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        }

        .project-media {
            width: 100%;
            height: 250px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2rem;
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }

        .project-media img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }

        .project-media img:hover {
            transform: scale(1.05);
        }

        .project-media video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            pointer-events: none;
        }

        .video-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 3rem;
            transition: all 0.3s ease;
        }

        .video-overlay:hover {
            background: rgba(0,0,0,0.5);
            transform: scale(1.02);
        }

        .project-content {
            padding: 2rem;
        }

        .project-card h3 {
            color: #667eea;
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }

        .project-card p {
            margin-bottom: 1rem;
            color: #666;
        }

        .media-placeholder {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            text-align: center;
        }

        /* Modal untuk fullscreen image/video */
        .modal {
            display: none;
            position: fixed;
            z-index: 2000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.9);
        }

        .modal-content {
            margin: auto;
            display: block;
            width: 90%;
            max-width: 900px;
            max-height: 90%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        .modal-content img {
            width: 100%;
            height: auto;
            max-height: 90vh;
            object-fit: contain;
        }

        .modal-content video {
            width: 100%;
            height: auto;
            max-height: 90vh;
        }

        .close {
            position: absolute;
            top: 15px;
            right: 35px;
            color: #f1f1f1;
            font-size: 40px;
            font-weight: bold;
            cursor: pointer;
            z-index: 2001;
        }

        .close:hover {
            color: #bbb;
        }

        /* Contact Section */
        .contact {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 80px 0;
            text-align: center;
        }

        .contact-info {
            margin-top: 2rem;
        }

        .contact-info p {
            margin: 1rem 0;
            font-size: 1.1rem;
        }

        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Project Categories */
        .project-categories {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        .category-btn {
            padding: 0.5rem 1.5rem;
            background: white;
            border: 2px solid #667eea;
            color: #667eea;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }

        .category-btn:hover,
        .category-btn.active {
            background: #667eea;
            color: white;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.5rem;
            }
            
            .about-content {
                grid-template-columns: 1fr;
                text-align: center;
            }
            
            .nav-links {
                display: none;
            }

            .projects-grid {
                grid-template-columns: 1fr;
            }

            .project-categories {
                flex-direction: column;
                align-items: center;
            }

            /* Mobile Timeline */
            .experience-timeline::after {
                left: 20px;
            }

            .experience-item {
                width: 100%;
                padding-left: 50px;
                padding-right: 20px;
            }

            .experience-item::after {
                left: 10px;
            }

            .experience-item:nth-child(even) {
                left: 0%;
            }

            .experience-item:nth-child(even)::after {
                left: 10px;
            }

            .experience-card::before {
                left: -15px;
                border-left-color: transparent;
                border-right-color: white;
            }

            .experience-item:nth-child(even) .experience-card::before {
                left: -15px;
                border-left-color: transparent;
                border-right-color: white;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <nav class="container">
            <div class="logo">{{ nama }}</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">Tentang</a></li>
                <li><a href="#experience">Pengalaman</a></li>
                <li><a href="#skills">Keahlian</a></li>
                <li><a href="#projects">Project</a></li>
                <li><a href="#contact">Kontak</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-content">
            <h1>Halo, Saya {{ nama }}</h1>
            <p>{{ profesi }} | {{ deskripsi_singkat }}</p>
            <a href="#about" class="btn">Kenali Saya Lebih Dekat</a>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2 class="section-title">Tentang Saya</h2>
            <div class="about-content">
                <div class="profile-img">
                    {{ nama[0] }}
                </div>
                <div class="about-text">
                    <p>{{ tentang_saya }}</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience Section -->
    <section id="experience" class="experience">
        <div class="container">
            <h2 class="section-title">Pengalaman Kerja</h2>
            <div class="experience-timeline">
                {% for exp in pengalaman %}
                <div class="experience-item">
                    <div class="experience-card">
                        <div class="experience-header">
                            <div class="experience-title">{{ exp.posisi }}</div>
                            <div class="experience-company">{{ exp.perusahaan }}</div>
                            <div class="experience-period">{{ exp.periode }}</div>
                            <div class="experience-location">{{ exp.lokasi }}</div>
                        </div>
                        <div class="experience-description">
                            {{ exp.deskripsi }}
                        </div>
                        {% if exp.pencapaian %}
                        <div class="experience-achievements">
                            <ul>
                                {% for pencapaian in exp.pencapaian %}
                                <li>{{ pencapaian }}</li>
                                {% endfor %}
                            </ul>
                        </div>
                        {% endif %}
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="skills">
        <div class="container">
            <h2 class="section-title">Keahlian Saya</h2>
            <div class="skills-grid">
                {% for skill in keahlian %}
                <div class="skill-card">
                    <h3>{{ skill.nama }}</h3>
                    <p>{{ skill.deskripsi }}</p>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects">
        <div class="container">
            <h2 class="section-title">Project Saya</h2>
            
            <!-- Project Categories Filter -->
            <div class="project-categories">
                <button class="category-btn active" onclick="filterProjects('all')">Semua</button>
                <button class="category-btn" onclick="filterProjects('design')">Design</button>
                <button class="category-btn" onclick="filterProjects('animation')">Animasi 3D</button>
            </div>

            <div class="projects-grid" id="projects-grid">
                {% for project in projects %}
                <div class="project-card" data-category="{{ project.kategori }}">
                    <div class="project-media" onclick="openModal('{{ project.media_url }}', '{{ project.media_type }}')">
                        {% if project.media_type == 'image' %}
                            <img src="{{ project.media_url }}" alt="{{ project.nama }}" loading="lazy">
                        {% elif project.media_type == 'video' %}
                            <video muted preload="metadata">
                                <source src="{{ project.media_url }}" type="video/mp4">
                                Browser Anda tidak mendukung video.
                            </video>
                            <div class="video-overlay">
                                ▶️
                            </div>
                        {% else %}
                            <div class="media-placeholder">
                                📁 {{ project.nama }}
                            </div>
                        {% endif %}
                    </div>
                    <div class="project-content">
                        <h3>{{ project.nama }}</h3>
                        <p>{{ project.deskripsi }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2 class="section-title">Hubungi Saya</h2>
            <div class="contact-info">
                <p><strong>Email:</strong> {{ email }}</p>
                <p><strong>Telepon:</strong> {{ telepon }}</p>
                <p><strong>Lokasi:</strong> {{ lokasi }}</p>
            </div>
        </div>
    </section>

    <!-- Modal untuk fullscreen view -->
    <div id="mediaModal" class="modal">
        <span class="close" onclick="closeModal()">&times;</span>
        <div id="modalContent" class="modal-content"></div>
    </div>

    <script>
        // Smooth scrolling untuk navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Filter projects by category
        function filterProjects(category) {
            const cards = document.querySelectorAll('.project-card');
            const buttons = document.querySelectorAll('.category-btn');
            
            // Update active button
            buttons.forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            // Filter cards
            cards.forEach(card => {
                if (category === 'all' || card.dataset.category === category) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        // Modal functions
        function openModal(src, type) {
            const modal = document.getElementById('mediaModal');
            const modalContent = document.getElementById('modalContent');
            
            if (type === 'image') {
                modalContent.innerHTML = `<img src="${src}" alt="Project Image">`;
            } else if (type === 'video') {
                modalContent.innerHTML = `
                    <video controls autoplay>
                        <source src="${src}" type="video/mp4">
                        Browser Anda tidak mendukung video.
                    </video>
                `;
            }
            
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';
        }

        function closeModal() {
            const modal = document.getElementById('mediaModal');
            const modalContent = document.getElementById('modalContent');
            
            // Stop video if playing
            const video = modalContent.querySelector('video');
            if (video) {
                video.pause();
                video.currentTime = 0;
            }
            
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
            modalContent.innerHTML = '';
        }

        // Close modal when clicking outside
        document.getElementById('mediaModal').addEventListener('click', function(e) {
            if (e.target === this) {
                closeModal();
            }
        });

        // Close modal with Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeModal();
            }
        });
    </script>
</body>
</html>
"""

# Data untuk portfolio - DENGAN PENGALAMAN KERJA
PORTFOLIO_DATA = {
    'nama': 'Muhammad Fauzan Hariyono',
    'profesi': 'Graphic Designer | 3D Animator Blender | Informatic Student',
    'deskripsi_singkat': 'Passionate Developer & Designer',
    'tentang_saya': 'Saya Muhammad Fauzan Hariyono sebagai mahasiswa informatika semester 4 di Universitas Gunadarma, telah mengembangkan keahlian teknis yang signifikan melalui partisipasi aktif dalam proyek-proyek seperti animator 3D. Keahlian bahasa saya terbukti dengan skor TOEIC yang impresif sebesar 726 yang saya peroleh melalui kompetisi yang diadakan oleh sekolah. Saya juga telah mendapatkan sertifikat BNSP sebagai pengakuan atas penyelesaian proyek perusahaan dengan standar yang tepat. Saya saat ini sedang memperdalam pengetahuan saya dalam pemrograman dan secara proaktif mencari kesempatan untuk memperluas pengalaman profesional saya di masa depan.',
    'pengalaman': [
        {
         'posisi': '3D Blender Animation',
            'perusahaan': 'Kulstori',
            'periode': 'May 2022 -  Jul 2022',
            'lokasi': 'Cinere, Jakarta Selatan',
            'deskripsi': 'membuat animasi belender yang seru dan menyenangkan untuk penonton , dan merigging karakter untuk di animasikan di dalam sebuah video nanti.',
            'pencapaian': [
                'berpengalaman sebagai animator 3D di kulstori dan membantu menganimasikan karakter RISKA DAN SI GEMBUL',
                'ahli dalam merigging dan menganimasikan karakter agar bergerak secara alami dan mulus',
                'kolaboratif dalam tim dan berfokus pada penciptaan animasi yang menarik dan disukai penonton',
            ]   
        },
        {
         'posisi': 'Social Media Designer',
            'perusahaan': 'Morephope',
            'periode': 'Juli 2022 - Okt 2022',
            'lokasi': 'Kalibata, Jakarta Timur',
            'deskripsi': 'Merancang kampanye edukasi tentang manfaat kopi melalui konten visual yang menarik dan informatif untuk meningkatkan awareness brand dan engagement audience.',
            'pencapaian': [
                'menciptakan desain poster yang menarik untuk instagram dan berbagai sosial media lainya',
                'berpatisipasi aktif dalam kerja tim untuk mengembangkan konsep-konsep kreatif yang inovatif',
                'bertanggung jawab atas perekaman dan penyuntingan video untuk konten instagram dan media sosial lainya',
            ]
        },
        {
            'posisi': 'Animator And Vector Illustration',
            'perusahaan': 'Tefa 2D',
            'periode': '2021 - 2023 ',
            'lokasi': 'Ciracas, Jakarta Timur',
            'deskripsi': 'saya membuat animasi vektor dalem bentuk 2D untuk iklan komersil sekolah dan untuk pendaftaran mahasiswa baru di smk itu.',
            'pencapaian': [
                'Membuat animasi 2d berbentuk video iklan komersil',
                'Membantu tim untuk membuat video sesuai kesepakatan yang akan menghasilkan hasil yang memukau',
                'Berkolaborasi dengan tim marketing untuk strategi konten yang efektif'
            ]
        },
    ],
    'keahlian': [
        {
            'nama': 'Graphic Design',
            'deskripsi': 'Saya membuat graphic design seperti poster dan juga mockup baju dengan menggunakan Adobe Photoshop dan Illustrator.'
        },
        {
            'nama': '3D Blender Animation',
            'deskripsi': 'Saya membuat sebuah video untuk animasi 3D seperti karakter animasi, serta melakukan rigging karakter dengan detail yang baik.'
        },
        {
            'nama': 'Microsoft Office',
            'deskripsi': 'Saya mempunyai skill menengah untuk Microsoft Office dan sedang belajar untuk memahaminya lebih dalam.'
        },
        {
            'nama': 'Programming',
            'deskripsi': 'Saya sedang memperdalam keahlian programming dan belajar data science untuk masa depan.'
        }
    ],
    'projects': [
        # === DESIGN PROJECTS ===
        {
            'nama': 'Poster 5 Manfaat Kopi By Morephope',
            'deskripsi': 'Desain poster informatif tentang manfaat kopi dengan gaya visual yang menarik dan mudah dipahami.',
            'media_type': 'image',
            'media_url': '/foto_cv/1333%20(1).jpg',
            'kategori': 'design'
        },
        {
            'nama': 'Cyber Bullying Awareness Campaign',
            'deskripsi': 'Kampanye kesadaran tentang cyber bullying dengan desain yang friendly dan mudah dipahami anak-anak.',
            'media_type': 'image',
            'media_url': '/foto_cv/portofolio%20pujha%20cyber%20bullying%20(1).jpg',
            'kategori': 'design'
        },
        {
            'nama': 'Pujha Collection Fashion Design',
            'deskripsi': 'Desain fashion untuk koleksi Pujha dengan sentuhan modern dan elegan | ini poster untuk penjualan aksesoris yang bisa dilihat di IG:pujha.accesories.',
            'media_type': 'image',
            'media_url': '/foto_cv/Pujha%20Collection%20(1).jpg',
            'kategori': 'design'
        },
        {
            'nama': '5 Kopi Arabik Poster',
            'deskripsi': 'Infografis tentang berbagai manfaat kopi dengan layout yang clean dan informatif.',
            'media_type': 'image',
            'media_url': '/foto_cv/tanggal-14%20(1).jpg',
            'kategori': 'design'
        },
        {
            'nama': 'Manfaat Kopi Untuk Kesehatan',
            'deskripsi': 'Poster tentang jenis-jenis kopi arabica terbaik dengan desain yang menarik.',
            'media_type': 'image',
            'media_url': '/foto_cv/tanggal-22(2)%20(1).jpg',
            'kategori': 'design'
        },
        
        # === ANIMATION PROJECTS ===
        {
            'nama': 'Animasi Melompat 3D Blender',
            'deskripsi': 'Animasi karakter 3D yang menampilkan gerakan melompat dengan teknik rigging yang baik.',
            'media_type': 'video',
            'media_url': '/video/1.Loncat%20Ojan0001-0045.mp4',
            'kategori': 'animation'
        },
        {
            'nama': 'Bola Ada Donat - Object Animation',
            'deskripsi': 'Animasi objek 3D yang kreatif dengan interaksi antara bola dan donat.',
            'media_type': 'video',
            'media_url': '/video/bola%20ada%20donat%201.mp4',
            'kategori': 'animation'
        },
        {
            'nama': 'Animasi Gembul Yang Sedang Berbicara',
            'deskripsi': 'Animasi karakter 3D dengan rigging advanced dan gerakan yang natural.',
            'media_type': 'video',
            'media_url': '/video/gembuludah10386-0857_2.mp4',
            'kategori': 'animation'
        },
        {
            'nama': 'Walk & Sit Cycle Animation',
            'deskripsi': 'Animasi cycle berjalan dan duduk yang menampilkan kemampuan animasi dasar yang solid.',
            'media_type': 'video',
            'media_url': '/video/jalan%20dan%20duduk0001-0028.mp4',
            'kategori': 'animation'
        },
        {
            'nama': 'Animasi Riska Yang Sedang Berjoget',
            'deskripsi': 'Animasi pendek yang ekspresif dan fun dengan karakter yang menarik.',
            'media_type': 'video',
            'media_url': '/video/yihhaa....%20%23shorts.mp4',
            'kategori': 'animation'
        }
    ],
    'email': 'fauzanhariyono280705@gmail.com',
    'telepon': '+62 856 9565 1087',
    'lokasi': 'Depok, Cimanggis Jawa Barat, Indonesia'
}

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, **PORTFOLIO_DATA)

@app.route('/api/profile')
def api_profile():
    """API endpoint untuk mendapatkan data profile"""
    return PORTFOLIO_DATA

if __name__ == '__main__':
    print("🚀 Starting Portfolio Website...")
    print("📱 Buka browser dan akses: http://localhost:5000")
    print("💡 Tekan Ctrl+C untuk menghentikan server")
    print("📂 Struktur folder yang diperlukan:")
    print("   📁 foto cv/")
    print("   📁 video/")
    print("   📄 portfolio.py")
    print("\n✅ FITUR BARU YANG DITAMBAHKAN:")
    print("   👨‍💼 Section Pengalaman Kerja dengan timeline design")
    print("   🎯 4 pengalaman kerja profesional termasuk freelance")
    print("   📊 Pencapaian spesifik untuk setiap pengalaman")
    print("   🎨 Design timeline yang modern dan responsive")
    print("   📱 Mobile-friendly experience section")
    print("   🔗 Navigasi header yang sudah diupdate")
    
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=False)
