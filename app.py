from flask import Flask, Response, request, redirect, url_for, render_template_string
from DAL import dal

app = Flask(__name__)


def with_base_head(html: str) -> str:
    # Convert stylesheet link
    html = html.replace('href="styles.css"', f'href="{url_for("serve_styles")}"')

    # Map both relative and absolute .html links to Flask routes (preserve href)
    replacements = [
        ('href="index.html"', f'href="{url_for("home")}"'),
        ('href="/index.html"', f'href="{url_for("home")}"'),
        ('href="about.html"', f'href="{url_for("about")}"'),
        ('href="/about.html"', f'href="{url_for("about")}"'),
        ('href="resume.html"', f'href="{url_for("resume")}"'),
        ('href="/resume.html"', f'href="{url_for("resume")}"'),
        ('href="projects.html"', f'href="{url_for("projects")}"'),
        ('href="/projects.html"', f'href="{url_for("projects")}"'),
        ('href="contact.html"', f'href="{url_for("contact")}"'),
        ('href="/contact.html"', f'href="{url_for("contact")}"'),
        ('href="thankyou.html"', f'href="{url_for("thankyou")}"'),
        ('href="/thankyou.html"', f'href="{url_for("thankyou")}"'),
    ]
    for needle, repl in replacements:
        html = html.replace(needle, repl)

    # Convert contact form action if present
    html = html.replace('action="thankyou.html"', f'action="{url_for("thankyou")}"')
    html = html.replace('action="/thankyou.html"', f'action="{url_for("thankyou")}"')

    return html


@app.get('/')
def home() -> Response:
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Personal portfolio website showcasing skills, experience, and projects">
    <title>Pranav's Portfolio - Home</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">

</head>
<body>
    <header>
        <nav class="container">
            <div class="logo">Pranav's Portfolio</div>
            <ul class="nav-links">
                <li><a href="index.html" aria-current="page">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="resume.html">Resume</a></li>
                <li><a href="projects.html">Projects</a></li>
                <li><a href="contact.html">Add Project</a></li>
            </ul>
            <button class="mobile-menu-toggle" aria-label="Toggle navigation menu">☰</button>
        </nav>
    </header>

    <main>
        <!-- Hero Section -->
        <section class="hero">
            <div class="container">
                <h1>Pranav Dandagi</h1>
                <p>MSIS student at Indiana University. Former Technical Solutions Engineer at Comviva. I work on reliable data pipelines, scalable systems, and analytics-driven solutions.</p>
                <a href="resume.html" class="btn">View My Resume</a>
            </div>
        </section>

        <!-- Introduction Section -->
        <section class="section">
            <div class="container">
                <h2>Highlights</h2>
                <div class="grid grid-2">
                    <div class="card">
                        <h3>Education</h3>
                        <p><strong>MS in Information Systems</strong>, Kelley School of Business, Indiana University (Dec 2026), GPA 3.7/4.0</p>
                        <ul>
                            <li>IS Foundations: databases, project management, technology infrastructure</li>
                            <li>Business Foundations: strategy, finance, operations, marketing</li>
                        </ul>
                    </div>
                    <div class="card">
                        <h3>Experience</h3>
                        <p><strong>Technical Solutions Engineer</strong> at Comviva (Dec 2023 – May 2025)</p>
                        <ul>
                            <li>Maintained €500K+/day data pipelines for Airtel; improved reliability and performance</li>
                            <li>Delivered scalable SMS gateway solutions; resolved bottlenecks across onboarding, reporting, billing</li>
                            <li>Diagnostics with SQL/Linux; reporting automation with Excel</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Quick Navigation -->
        <section class="section">
            <div class="container">
                <h2>Explore My Work</h2>
                <div class="grid grid-3">
                    <div class="card">
                        <h3>About Me</h3>
                        <p>Learn about my background, career goals, and what drives my passion for technology and development.</p>
                        <a href="about.html" class="btn">Read More</a>
                    </div>
                    <div class="card">
                        <h3>My Resume</h3>
                        <p>View my educational background, professional experience, and technical skills in detail.</p>
                        <a href="resume.html" class="btn">View Resume</a>
                    </div>
                    <div class="card">
                        <h3>Projects</h3>
                        <p>Explore my portfolio of projects, including detailed descriptions, technologies used, and live demos.</p>
                        <a href="projects.html" class="btn">View Projects</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Call to Action -->
        <section class="section">
            <div class="container">
                <h2>Let's Connect</h2>
                <p>Ready to discuss opportunities or collaborate on exciting projects? I'd love to hear from you.</p>
                <a href="contact.html" class="btn">Get In Touch</a>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <div class="social-links">
                <a href="https://github.com/Pranav-44/aidd" target="_blank" rel="noopener noreferrer" aria-label="GitHub Profile">GitHub</a>
                <a href="https://www.linkedin.com/in/pranavdandagi/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn Profile">LinkedIn</a>
                <a href="mailto:pdandagi@iu.edu" aria-label="Email Contact">Email</a>
            </div>
            <p>&copy; 2024 Pranav's Portfolio. All rights reserved.</p>
            <p><a href="https://github.com/Pranav-44/aidd" target="_blank" rel="noopener noreferrer">View Source Code on GitHub</a></p>
        </div>
    </footer>

    <script>
        // Enhanced JavaScript functionality
        document.addEventListener('DOMContentLoaded', function() {
            // Mobile menu toggle functionality
            const mobileToggle = document.querySelector('.mobile-menu-toggle');
            const navLinks = document.querySelector('.nav-links');
            
            if (mobileToggle && navLinks) {
                mobileToggle.addEventListener('click', function() {
                    navLinks.classList.toggle('active');
                    this.setAttribute('aria-expanded', navLinks.classList.contains('active'));
                });
            }

            // Header scroll effect
            const header = document.querySelector('header');
            let lastScrollY = window.scrollY;
            
            window.addEventListener('scroll', function() {
                const currentScrollY = window.scrollY;
                
                if (currentScrollY > 100) {
                    header.classList.add('scrolled');
                } else {
                    header.classList.remove('scrolled');
                }
                
                lastScrollY = currentScrollY;
            });

            // Smooth scrolling for anchor links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });

            // Add loading animation to buttons
            document.querySelectorAll('.btn').forEach(button => {
                button.addEventListener('click', function(e) {
                    if (this.type === 'submit') {
                        this.style.opacity = '0.7';
                        this.style.transform = 'scale(0.98)';
                    }
                });
            });

            // Intersection Observer for animations
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };

            const observer = new IntersectionObserver(function(entries) {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            }, observerOptions);

            // Observe cards for animation
            document.querySelectorAll('.card').forEach(card => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                observer.observe(card);
            });
        });
    </script>
</body>
</html>
"""
    return with_base_head(html)


@app.get('/about')
def about() -> Response:
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Learn about Pranav's background, career goals, and passion for technology">
    <title>About Pranav - Personal Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="container">
            <div class="logo">Pranav's Portfolio</div>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html" aria-current="page">About</a></li>
                <li><a href="resume.html">Resume</a></li>
                <li><a href="projects.html">Projects</a></li>
                <li><a href="contact.html">Add Project</a></li>
            </ul>
            <button class="mobile-menu-toggle" aria-label="Toggle navigation menu">☰</button>
        </nav>
    </header>
    <main>
        <!-- Hero Section -->
        <section class="hero">
            <div class="container">
                <h1>About Me</h1>
                <p>Discover my journey, passions, and aspirations in the world of technology</p>
            </div>
        </section>
        <!-- About Content -->
        <section class="section">
            <div class="container">
                <div class="grid grid-2">
                    <div>
                        <img src="images/WhatsApp Image 2025-10-04 at 10.21.11 PM.jpeg" alt="Pranav's professional headshot" class="profile-image">
                    </div>
                    <div>
                        <h2>Hello, I'm Pranav</h2>
                        <p>MS in Information Systems candidate at Indiana University’s Kelley School of Business (Dec 2026, GPA 3.7/4.0). Former Technical Solutions Engineer at Comviva, where I supported high‑throughput telecom platforms and analytics-driven operations.</p>
                        <p>I care about building reliable systems, clear data flows, and pragmatic tooling that improve performance and decisions. I enjoy working across data, infrastructure, and product to deliver measurable outcomes.</p>
                    </div>
                </div>
            </div>
        </section>
        <!-- Background Section -->
        <section class="section">
            <div class="container">
                <h2>My Background</h2>
                <div class="grid grid-2">
                    <div class="card">
                        <h3>Education</h3>
                        <p><strong>Kelley School of Business, Indiana University</strong> — MSIS (Dec 2026). Certificates in IS Foundations (databases, project management, infrastructure) and Business Foundations (strategy, finance, operations, marketing).</p>
                    </div>
                    <div class="card">
                        <h3>Experience</h3>
                        <p><strong>Comviva (Technical Solutions Engineer):</strong> safeguarded €500K+/day data pipelines for Airtel, delivered scalable SMS gateway solutions, and improved platform reliability using SQL, Linux tooling, and reporting automation.</p>
                    </div>
                </div>
            </div>
        </section>
        <!-- Goals Section -->
        <section class="section">
            <div class="container">
                <h2>Focus Areas</h2>
                <div class="grid grid-3">
                    <div class="card">
                        <h3>Reliable Data Systems</h3>
                        <p>Designing and operating pipelines with strong observability, graceful failure handling, and clear SLIs/SLOs.</p>
                    </div>
                    <div class="card">
                        <h3>Analytics for Decisions</h3>
                        <p>Turning operational data into actionable insights through validation, modeling, and lean reporting.</p>
                    </div>
                    <div class="card">
                        <h3>Pragmatic Engineering</h3>
                        <p>Prioritizing maintainability, measurable impact, and clear communication across stakeholders.</p>
                    </div>
                </div>
            </div>
        </section>
        <!-- Interests Section -->
        <section class="section">
            <div class="container">
                <h2>Beyond Coding</h2>
                <p>When I'm not coding, you'll find me exploring new technologies, contributing to open-source projects, or enjoying outdoor activities. I believe in maintaining a healthy work-life balance and finding inspiration in diverse experiences.</p>
                
                <div class="grid grid-2">
                    <div class="card">
                        <h3>Continuous Learning</h3>
                        <p>I'm always exploring new programming languages, frameworks, and tools. Currently, I'm particularly interested in AI/ML integration, cloud architecture, and mobile development.</p>
                    </div>
                    <div class="card">
                        <h3>Community Involvement</h3>
                        <p>I enjoy participating in tech meetups, contributing to open-source projects, and sharing knowledge with the developer community through blogging and mentoring.</p>
                    </div>
                </div>
            </div>
        </section>
        <!-- Call to Action -->
        <section class="section">
            <div class="container">
                <h2>Let's Connect</h2>
                <p>I'm always excited to discuss new opportunities, collaborate on interesting projects, or simply connect with fellow developers and technology enthusiasts.</p>
                <a href="contact.html" class="btn">Get In Touch</a>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <div class="social-links">
                <a href="https://github.com/Pranav-44/aidd" target="_blank" rel="noopener noreferrer" aria-label="GitHub Profile">GitHub</a>
                <a href="https://www.linkedin.com/in/pranavdandagi/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn Profile">LinkedIn</a>
                <a href="mailto:pdandagi@iu.edu" aria-label="Email Contact">Email</a>
            </div>
            <p>&copy; 2024 Pranav's Portfolio. All rights reserved.</p>
            <p><a href="https://github.com/Pranav-44/aidd" target="_blank" rel="noopener noreferrer">View Source Code on GitHub</a></p>
        </div>
    </footer>
    <script>
        // Enhanced JavaScript functionality
        document.addEventListener('DOMContentLoaded', function() {
            // Mobile menu toggle functionality
            const mobileToggle = document.querySelector('.mobile-menu-toggle');
            const navLinks = document.querySelector('.nav-links');
            
            if (mobileToggle && navLinks) {
                mobileToggle.addEventListener('click', function() {
                    navLinks.classList.toggle('active');
                    this.setAttribute('aria-expanded', navLinks.classList.contains('active'));
                });
            }

            // Header scroll effect
            const header = document.querySelector('header');
            let lastScrollY = window.scrollY;
            
            window.addEventListener('scroll', function() {
                const currentScrollY = window.scrollY;
                
                if (currentScrollY > 100) {
                    header.classList.add('scrolled');
                } else {
                    header.classList.remove('scrolled');
                }
                
                lastScrollY = currentScrollY;
            });

            // Smooth scrolling for anchor links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });

            // Add loading animation to buttons
            document.querySelectorAll('.btn').forEach(button => {
                button.addEventListener('click', function(e) {
                    if (this.type === 'submit') {
                        this.style.opacity = '0.7';
                        this.style.transform = 'scale(0.98)';
                    }
                });
            });

            // Intersection Observer for animations
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };

            const observer = new IntersectionObserver(function(entries) {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            }, observerOptions);

            // Observe cards for animation
            document.querySelectorAll('.card').forEach(card => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                observer.observe(card);
            });
        });
    </script>
</body>
</html>
"""
    return with_base_head(html)


@app.get('/resume')
def resume() -> Response:
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Pranav's professional resume including education, experience, skills, and achievements">
    <title>Resume - Pranav's Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="container">
            <div class="logo">Pranav's Portfolio</div>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="resume.html" aria-current="page">Resume</a></li>
                <li><a href="projects.html">Projects</a></li>
                <li><a href="contact.html">Add Project</a></li>
            </ul>
            <button class="mobile-menu-toggle" aria-label="Toggle navigation menu">☰</button>
        </nav>
    </header>
    <main>
        <!-- Hero Section -->
        <section class="hero">
            <div class="container">
                <h1>My Resume</h1>
                <p>Education, experience, skills, and achievements</p>
            </div>
        </section>
        <!-- Resume Content -->
        <section class="section">
            <div class="container">
                <!-- Contact Information -->
                <div class="card">
                    <h2>Contact Information</h2>
                    <div class="grid grid-2">
                        <div>
                            <p><strong>Name:</strong> PRANAV DANDAGI</p>
                            <p><strong>Email:</strong> <a href="mailto:pdandagi@iu.edu">pdandagi@iu.edu</a></p>
                            <p><strong>Phone:</strong> (+1) 930 333-7201</p>
                            <p><strong>Location:</strong> Bloomington, IN</p>
                        </div>
                        <div>
                            <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/pranavdandagi" target="_blank" rel="noopener noreferrer">linkedin.com/in/pranavdandagi</a></p>
                            <p><strong>GitHub:</strong> <a href="https://github.com/Pranav-44/aidd" target="_blank" rel="noopener noreferrer">github.com/Pranav-44</a></p>
                        </div>
                    </div>
                </div>
                <!-- Education -->
                <div class="card">
                    <h2>Education</h2>
                    <div class="grid grid-2">
                        <div>
                            <h3>Master of Science in Information Systems</h3>
                            <p><strong>Kelley School of Business, Indiana University – Bloomington, IN</strong> | December 2026</p>
                            <p>GPA: 3.7/4.00</p>
                            <ul>
                                <li>Certificate in IS Foundations (Summer 2025): Database systems, project management, technology infrastructure</li>
                                <li>Certificate in Business Foundations (Summer 2025): Strategy, finance, operations, marketing</li>
                            </ul>
                        </div>
                        <div>
                            <h3>Bachelor of Engineering in Computer Science and Engineering</h3>
                            <p><strong>KLS Gogte Institute of Technology – Belagavi, India</strong> | August 2023</p>
                            <p>GPA: 3.8/4.00</p>
                            <ul>
                                <li>Co-Captain, college swim team; led training/strategy for 10+ teammates; contributed to 6+ individual medals at Inter-College Championship</li>
                                <li>Built Python and SQL projects applying core CSE concepts; active in tech clubs and outreach</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <!-- Professional Experience -->
                <div class="card">
                    <h2>Experience</h2>
                    <div class="grid grid-1">
                        <div>
                            <h3>Technical Solutions Engineer</h3>
                            <p><strong>Comviva Technologies – Gurgaon, India</strong> | December 2023 – May 2025</p>
                            <ul>
                                <li>Ensured €500K+/day data pipeline integrity for Airtel by managing incidents, analyzing system failures, and collaborating with stakeholders to maintain service continuity</li>
                                <li>Partnered with product and support teams to deliver scalable SMS gateway solutions for B2B clients, resolving system bottlenecks and improving onboarding, reporting, and billing efficiency</li>
                                <li>Diagnosed platform issues using SQL and Linux tools, reducing downtime and increasing system performance</li>
                                <li>Created and maintained Excel-based reporting tools to streamline client support operations and enable faster decision-making</li>
                            </ul>
                        </div>
                    </div>
                    <div class="grid grid-1">
                        <div>
                            <h3>Data Science Intern</h3>
                            <p><strong>Data for Decisions – Bangalore, India</strong> | March 2023 – June 2023</p>
                            <ul>
                                <li>Built an in-house Legacy Migration system using Python OCR libraries to extract and digitize data from unstructured legacy formats</li>
                                <li>Improved data accuracy and integration by building validation scripts, enabling smoother migration into modern systems and enhancing accessibility</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <!-- Technical Skills -->
                <div class="card">
                    <h2>Technical</h2>
                    <div class="grid grid-3">
                        <div>
                            <h3>Languages & Tools</h3>
                            <ul>
                                <li>Python, R, SQL, Java, C</li>
                                <li>Jira, Excel</li>
                            </ul>
                        </div>
                        <div>
                            <h3>Methodologies</h3>
                            <ul>
                                <li>Agile: Scrum, SAFe, Kanban</li>
                                <li>Project management</li>
                            </ul>
                        </div>
                        <div>
                            <h3>Certifications</h3>
                            <ul>
                                <li>Data Science for Engineers using R (NPTEL)</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <!-- Academic Projects -->
                <div class="card">
                    <h2>Academic Projects</h2>
                    <ul>
                        <li><strong>Customer Spending Forecasting:</strong> Built a predictive model using customer behavior data to forecast e-commerce spending patterns and inform targeted marketing strategies.</li>
                        <li><strong>Hospital Operations Optimization:</strong> Developed a data-driven resource planning model in R to predict patient satisfaction, estimate length of stay, and optimize treatment allocation across 20+ conditions.</li>
                    </ul>
                </div>
                <!-- Leadership -->
                <div class="card">
                    <h2>Leadership</h2>
                    <h3>Rotaract Club of GIT – India</h3>
                    <p><strong>Youth Service and Sports Director</strong> | January 2020 – January 2022</p>
                    <ul>
                        <li>Led blood drives, clean-up initiatives, and tree plantations, engaging 300+ students and boosting volunteer turnout by 40%</li>
                        <li>Initiated regular sports activities for peers to foster teamwork and wellness</li>
                    </ul>
                </div>
                <!-- Download Resume -->
                <div class="card" style="text-align: center;">
                    <h2>Download Resume</h2>
                    <p>Get a PDF version of my resume for your records</p>
                    <a href="Dandagi, Pranav.pdf" class="btn" id="downloadResumeBtn" download>Download PDF Resume</a>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <div class="social-links">
                <a href="https://github.com/Pranav-44/aidd" target="_blank" rel="noopener noreferrer" aria-label="GitHub Profile">GitHub</a>
                <a href="https://www.linkedin.com/in/pranavdandagi/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn Profile">LinkedIn</a>
                <a href="mailto:pdandagi@iu.edu" aria-label="Email Contact">Email</a>
            </div>
            <p>&copy; 2024 Pranav's Portfolio. All rights reserved.</p>
            <p><a href="https://github.com/Pranav-44/aidd" target="_blank" rel="noopener noreferrer">View Source Code on GitHub</a></p>
        </div>
    </footer>
    <script>
        // Mobile menu toggle functionality
        document.addEventListener('DOMContentLoaded', function() {
            const mobileToggle = document.querySelector('.mobile-menu-toggle');
            const navLinks = document.querySelector('.nav-links');
            
            if (mobileToggle && navLinks) {
                mobileToggle.addEventListener('click', function() {
                    navLinks.classList.toggle('active');
                });
            }
            
            // Resume download with fallback to Print to PDF
            const downloadBtn = document.getElementById('downloadResumeBtn');
            if (downloadBtn) {
                downloadBtn.addEventListener('click', function(event) {
                    // Try to detect if resume.pdf exists
                    fetch('Dandagi, Pranav.pdf', { method: 'HEAD' }).then(function(response) {
                        if (response.ok) {
                            // Let the browser download the file
                            window.location.href = 'Dandagi, Pranav.pdf';
                        } else {
                            // Fallback to print dialog to save as PDF
                            event.preventDefault();
                            window.print();
                        }
                    }).catch(function() {
                        // Network or missing file: fallback to print
                        event.preventDefault();
                        window.print();
                    });
                    // Prevent default while we check
                    event.preventDefault();
                });
            }
        });
    </script>
</body>
</html>
"""
    return with_base_head(html)


@app.get('/projects')
def projects() -> Response:
    # Get projects from database
    projects_data = dal.get_all_projects()
    
    # Check for success/error messages
    added = request.args.get('added')
    deleted = request.args.get('deleted')
    error = request.args.get('error')
    
    # Generate success/error message
    message_html = ""
    if added == '1':
        message_html = '<div class="alert alert-success">Project added successfully!</div>'
    elif deleted == '1':
        message_html = '<div class="alert alert-success">Project deleted successfully!</div>'
    elif error == '1':
        message_html = '<div class="alert alert-error">Error adding project to database. Please try again.</div>'
    elif error == '2':
        message_html = '<div class="alert alert-error">Please fill in all required fields.</div>'
    elif error == '3':
        message_html = '<div class="alert alert-error">Could not delete the project. It may not exist.</div>'
    elif error == '4':
        message_html = '<div class="alert alert-error">Project title is required.</div>'
    elif error == '5':
        message_html = '<div class="alert alert-error">Project description is required.</div>'
    elif error == '6':
        message_html = '<div class="alert alert-error">Image filename is required.</div>'
    elif error == '7':
        message_html = '<div class="alert alert-error">Invalid image filename format. Use format like "example.png" or "example.jpg".</div>'
    elif error == '8':
        message_html = '<div class="alert alert-error">Image file not found. Make sure the image exists in the static/images folder.</div>'
    
    # Generate projects HTML table
    projects_html = ""
    if projects_data:
        projects_html = """
        <div class="card">
            <h2>My Projects</h2>
            <p>Here are my latest projects stored in the database:</p>
            <table class="projects-table">
                <thead>
                    <tr>
                        <th>Image</th>
                        <th>Title</th>
                        <th>Description</th>
                        <th style=\"width:140px;\">Actions</th>
                    </tr>
                </thead>
                <tbody>"""
        
        for project in projects_data:
            projects_html += f"""
                    <tr>
                        <td>
                            <img src="/images/{project['image_filename']}" 
                                 alt="{project['title']}" 
                                 class="project-thumbnail"
                                 style="width: 150px; height: 100px; object-fit: cover; border-radius: 8px;">
                        </td>
                        <td><strong>{project['title']}</strong></td>
                        <td>{project['description']}</td>
                        <td>
                            <form action="/projects/delete" method="POST" onsubmit="return confirm('Delete this project?');">
                                <input type="hidden" name="project_id" value="{project['id']}">
                                <button type="submit" class="btn btn-danger" aria-label="Delete {project['title']}">Delete</button>
                            </form>
                        </td>
                    </tr>"""
        
        projects_html += """
                </tbody>
            </table>
        </div>"""
    else:
        projects_html = """
        <div class="card">
            <h2>My Projects</h2>
            <p>No projects found in the database. <a href="/contact">Add a new project</a> to get started!</p>
        </div>"""
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Explore Pranav's portfolio of web development projects with detailed descriptions and live demos">
    <title>Projects - Pranav's Portfolio</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        .projects-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
            background: var(--bg-primary);
            border-radius: var(--radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-md);
        }}
        .projects-table th,
        .projects-table td {{
            padding: 1.5rem;
            text-align: left;
            border-bottom: 1px solid var(--border-light);
            vertical-align: top;
        }}
        .projects-table th {{
            background: linear-gradient(135deg, var(--bg-secondary), var(--bg-tertiary));
            font-weight: 700;
            color: var(--text-primary);
            text-transform: uppercase;
            font-size: 0.875rem;
            letter-spacing: 0.05em;
        }}
        .projects-table tr:hover {{
            background-color: var(--bg-secondary);
        }}
        .project-thumbnail {{
            border: 3px solid var(--border-color);
            border-radius: var(--radius-md);
            transition: var(--transition-normal);
            box-shadow: var(--shadow-sm);
        }}
        .project-thumbnail:hover {{
            transform: scale(1.1);
            border-color: var(--primary-color);
            box-shadow: var(--shadow-lg);
        }}
        .alert {{
            padding: 1rem 1.5rem;
            margin: 1.5rem 0;
            border-radius: var(--radius-lg);
            font-weight: 500;
            border: 1px solid;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        .alert-success {{
            background-color: rgba(16, 185, 129, 0.1);
            color: var(--success-color);
            border-color: rgba(16, 185, 129, 0.2);
        }}
        .alert-error {{
            background-color: rgba(239, 68, 68, 0.1);
            color: var(--error-color);
            border-color: rgba(239, 68, 68, 0.2);
        }}
        @media (max-width: 768px) {{
            .projects-table {{
                font-size: 0.9rem;
            }}
            .projects-table th,
            .projects-table td {{
                padding: 0.5rem;
            }}
            .project-thumbnail {{
                width: 100px !important;
                height: 70px !important;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <nav class="container">
            <div class="logo">Pranav's Portfolio</div>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="resume.html">Resume</a></li>
                <li><a href="projects.html" aria-current="page">Projects</a></li>
                <li><a href="contact.html">Add Project</a></li>
            </ul>
            <button class="mobile-menu-toggle" aria-label="Toggle navigation menu">☰</button>
        </nav>
    </header>
    <main>
        <!-- Hero Section -->
        <section class="hero">
            <div class="container">
                <h1>My Projects</h1>
                <p>Explore my portfolio of web development projects and technical solutions</p>
            </div>
        </section>
        
        <!-- Quick Add Project -->
        <section class="section">
            <div class="container">
                <div class="card" style="margin-bottom: 2rem;">
                    <h2>Quick Add Project</h2>
                    <p>Add a new project to your portfolio. Choose from available images below:</p>
                    
                    <!-- Available Images List -->
                    <div style="margin-bottom: 1.5rem; padding: 1rem; background: var(--bg-secondary); border-radius: var(--radius-md);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                            <h4 style="margin-bottom: 0; color: var(--text-primary);">Available Images:</h4>
                            <button type="button" id="refreshImagesBtn" style="background: var(--primary-color); color: white; border: none; padding: 0.5rem 1rem; border-radius: var(--radius-sm); cursor: pointer; font-size: 0.875rem;">Refresh</button>
                        </div>
                        <div id="availableImagesList" style="min-height: 2rem;">
                            <div style="color: var(--text-light); font-style: italic;">Loading available images...</div>
                        </div>
                    </div>
                    
                    <form action="/projects/add" method="POST" class="grid grid-3" style="gap: 1rem;">
                        <div class="form-group">
                            <label for="qa_title">Title *</label>
                            <input type="text" id="qa_title" name="project_title" required minlength="3" placeholder="e.g., My Awesome Project">
                        </div>
                        <div class="form-group">
                            <label for="qa_image">Image filename *</label>
                            <input type="text" id="qa_image" name="image_filename" required placeholder="Ecommerce-KPI-dashboard.png">
                            <div class="help-text">Copy exactly from the list above</div>
                        </div>
                        <div class="form-group" style="grid-column: 1 / -1;">
                            <label for="qa_desc">Description *</label>
                            <textarea id="qa_desc" name="project_description" rows="3" required minlength="10" placeholder="Describe your project, technologies used, and key features..."></textarea>
                        </div>
                        <div style="grid-column: 1 / -1;">
                            <button type="submit" class="btn">Add Project</button>
                        </div>
                    </form>
                </div>
                
                <!-- Projects from Database -->
                {message_html}
                {projects_html}
                
                <!-- Development Process -->
                <div class="card">
                    <h2>Development Process</h2>
                    <div class="grid grid-2">
                        <div>
                            <h3>My Approach</h3>
                            <p>I follow a systematic approach to project development that emphasizes planning, user experience, and code quality:</p>
                            <ul>
                                <li><strong>Planning:</strong> Requirements analysis and technical architecture design</li>
                                <li><strong>Design:</strong> User interface mockups and user experience planning</li>
                                <li><strong>Development:</strong> Agile development with regular testing and iteration</li>
                                <li><strong>Testing:</strong> Comprehensive testing including unit, integration, and user testing</li>
                                <li><strong>Deployment:</strong> CI/CD pipeline setup and production deployment</li>
                                <li><strong>Maintenance:</strong> Ongoing support and feature updates</li>
                            </ul>
                        </div>
                        <div>
                            <h3>Best Practices</h3>
                            <ul>
                                <li>Clean, maintainable code with proper documentation</li>
                                <li>Responsive design for all screen sizes</li>
                                <li>Accessibility compliance (WCAG 2.1)</li>
                                <li>Performance optimization and SEO best practices</li>
                                <li>Security best practices and data protection</li>
                                <li>Version control with Git and collaborative workflows</li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <!-- Contact for Projects -->
                <div class="card" style="text-align: center;">
                    <h2>Interested in Working Together?</h2>
                    <p>I'm always excited to take on new challenges and collaborate on interesting projects. Whether you need a custom web application, want to discuss a potential collaboration, or have questions about any of my projects, I'd love to hear from you.</p>
                    <a href="contact.html" class="btn">Get In Touch</a>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <div class="social-links">
                <a href="https://github.com/Pranav-44" target="_blank" rel="noopener noreferrer" aria-label="GitHub Profile">GitHub</a>
                <a href="https://www.linkedin.com/in/pranavdandagi/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn Profile">LinkedIn</a>
                <a href="mailto:pdandagi@iu.edu" aria-label="Email Contact">Email</a>
            </div>
            <p>&copy; 2024 Pranav's Portfolio. All rights reserved.</p>
            <p><a href="https://github.com/Pranav-44/aidd" target="_blank" rel="noopener noreferrer">View Source Code on GitHub</a></p>
        </div>
    </footer>
    <script>
        // Mobile menu toggle functionality
        document.addEventListener('DOMContentLoaded', function() {{
            const mobileToggle = document.querySelector('.mobile-menu-toggle');
            const navLinks = document.querySelector('.nav-links');
            
            if (mobileToggle && navLinks) {{
                mobileToggle.addEventListener('click', function() {{
                    navLinks.classList.toggle('active');
                }});
            }}

            // Load available images
            function loadAvailableImages() {{
                const imagesList = document.getElementById('availableImagesList');
                if (!imagesList) return;

                imagesList.innerHTML = '<div style="color: var(--text-light); font-style: italic;">Loading available images...</div>';

                fetch('/api/available-images')
                    .then(response => response.json())
                    .then(images => {{
                        if (images.length === 0) {{
                            imagesList.innerHTML = '<div style="color: var(--text-light); font-style: italic;">No images found in static/images folder</div>';
                            return;
                        }}

                        const imagesHtml = images.map(image => 
                            `<div style="margin-bottom: 0.25rem;">
                                <code style="background: var(--bg-tertiary); padding: 0.25rem 0.5rem; border-radius: var(--radius-sm); cursor: pointer;" onclick="selectImage('${{image}}')">${{image}}</code>
                            </div>`
                        ).join('');

                        imagesList.innerHTML = imagesHtml;
                    }})
                    .catch(error => {{
                        console.error('Error loading images:', error);
                        imagesList.innerHTML = '<div style="color: var(--error-color);">Error loading images</div>';
                    }});
            }}

            // Function to select an image when clicked
            function selectImage(filename) {{
                const imageInput = document.getElementById('qa_image');
                if (imageInput) {{
                    imageInput.value = filename;
                    imageInput.focus();
                }}
            }}

            // Make selectImage globally available
            window.selectImage = selectImage;

            // Load images on page load
            loadAvailableImages();

            // Add refresh button functionality
            const refreshBtn = document.getElementById('refreshImagesBtn');
            if (refreshBtn) {{
                refreshBtn.addEventListener('click', function() {{
                    loadAvailableImages();
                }});
            }}
        }});
    </script>
</body>
</html>"""
    return with_base_head(html)


@app.post('/contact')
def contact_post() -> Response:
    """Handle project submission form."""
    title = request.form.get('project_title', '').strip()
    description = request.form.get('project_description', '').strip()
    image_filename = request.form.get('image_filename', '').strip()
    
    if title and description and image_filename:
        success = dal.add_project(title, description, image_filename)
        if success:
            return redirect(url_for('projects') + '?added=1')
        else:
            return redirect(url_for('contact') + '?error=1')
    else:
        return redirect(url_for('contact') + '?error=2')


@app.post('/projects/add')
def projects_add() -> Response:
    """Add a project from the quick add form on Projects page."""
    title = request.form.get('project_title', '').strip()
    description = request.form.get('project_description', '').strip()
    image_filename = request.form.get('image_filename', '').strip()

    # Validate required fields
    if not title:
        return redirect(url_for('projects') + '?error=4')
    if not description:
        return redirect(url_for('projects') + '?error=5')
    if not image_filename:
        return redirect(url_for('projects') + '?error=6')

    # Validate image filename format
    import os
    import re
    if not re.match(r'^[a-zA-Z0-9._\s-]+\.(png|jpg|jpeg)$', image_filename, re.IGNORECASE):
        return redirect(url_for('projects') + '?error=7')

    # Check if image file exists
    image_path = os.path.join('images', image_filename)
    if not os.path.exists(image_path):
        return redirect(url_for('projects') + '?error=8')

    if dal.add_project(title, description, image_filename):
        return redirect(url_for('projects') + '?added=1')
    return redirect(url_for('projects') + '?error=1')


@app.post('/projects/delete')
def projects_delete() -> Response:
    """Delete a project by ID from the Projects page."""
    project_id_raw = request.form.get('project_id')
    try:
        project_id = int(project_id_raw) if project_id_raw is not None else -1
    except ValueError:
        project_id = -1

    if project_id < 0:
        return redirect(url_for('projects') + '?error=3')

    if dal.delete_project(project_id):
        return redirect(url_for('projects') + '?deleted=1')
    return redirect(url_for('projects') + '?error=3')

@app.get('/contact')
def contact() -> Response:
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Contact Pranav - Get in touch for opportunities, collaborations, or questions about projects">
    <title>Add Project - Pranav's Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="container">
            <div class="logo">Pranav's Portfolio</div>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="resume.html">Resume</a></li>
                <li><a href="projects.html">Projects</a></li>
                <li><a href="contact.html" aria-current="page">Contact</a></li>
            </ul>
            <button class="mobile-menu-toggle" aria-label="Toggle navigation menu">☰</button>
        </nav>
    </header>
    <main>
        <!-- Hero Section -->
        <section class="hero">
            <div class="container">
                <h1>Add Projects</h1>
                <p>Add new projects to my portfolio database. Make sure to upload your project images to the images folder first.</p>
            </div>
        </section>
        <!-- Contact Content -->
        <section class="section">
            <div class="container">
                <div class="grid grid-2">
                    <!-- Project Guidelines -->
                    <div class="card">
                        <h2>Project Guidelines</h2>
                        <p>Before adding a project, please ensure you follow these guidelines:</p>
                        
                        <h3>Image Requirements</h3>
                        <div>
                            <ul>
                                <li>Upload your project image to the <code>images/</code> folder</li>
                                <li>Use descriptive filenames (e.g., <code>ecommerce-dashboard.png</code>)</li>
                                <li>Supported formats: PNG, JPG, JPEG</li>
                                <li>Recommended size: 800x600 pixels or similar aspect ratio</li>
                            </ul>
                        </div>

                        <h3>Available Images</h3>
                        <div style="margin-bottom: 1rem; padding: 1rem; background: var(--bg-secondary); border-radius: var(--radius-md);">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                                <h4 style="margin-bottom: 0; color: var(--text-primary); font-size: 0.875rem;">Current Images:</h4>
                                <button type="button" id="refreshImagesBtnContact" style="background: var(--primary-color); color: white; border: none; padding: 0.25rem 0.75rem; border-radius: var(--radius-sm); cursor: pointer; font-size: 0.75rem;">Refresh</button>
                            </div>
                            <div id="availableImagesListContact" style="min-height: 1.5rem;">
                                <div style="color: var(--text-light); font-style: italic; font-size: 0.875rem;">Loading available images...</div>
                            </div>
                        </div>

                        <h3>Project Information</h3>
                        <div>
                            <ul>
                                <li><strong>Title:</strong> Clear, descriptive project name</li>
                                <li><strong>Description:</strong> Include technologies used, key features, and project goals</li>
                                <li><strong>Image:</strong> Screenshot or demo of the project</li>
                            </ul>
                        </div>

                        <h3>Example Projects</h3>
                        <div>
                            <p>Check out existing projects in my portfolio:</p>
                            <a href="projects.html" class="btn btn-secondary">View Current Projects</a>
                        </div>

                        <h3>Need Help?</h3>
                        <p>If you have questions about adding projects, feel free to reach out:</p>
                        <div class="social-links">
                            <a href="mailto:pdandagi@iu.edu" aria-label="Email Contact">
                                Email Me
                            </a>
                            <a href="https://github.com/Pranav-44" target="_blank" rel="noopener noreferrer" aria-label="GitHub Profile">
                                GitHub
                            </a>
                        </div>
                    </div>

                    <!-- Project Submission Form -->
                    <div class="card">
                        <h2>Add New Project</h2>
                        <p>Use this form to add a new project to my portfolio. Make sure you've already uploaded the project image to the images folder.</p>
                        <form id="projectForm" action="/contact" method="POST" novalidate>
                            <div class="form-group">
                                <label for="project_title">Project Title *</label>
                                <input 
                                    type="text" 
                                    id="project_title" 
                                    name="project_title" 
                                    required 
                                    minlength="3"
                                    placeholder="Enter project title"
                                    aria-describedby="project_title-error"
                                >
                                <div id="project_title-error" class="error" role="alert"></div>
                            </div>

                            <div class="form-group">
                                <label for="project_description">Project Description *</label>
                                <textarea 
                                    id="project_description" 
                                    name="project_description" 
                                    rows="5"
                                    required
                                    minlength="10"
                                    placeholder="Describe your project, technologies used, and key features"
                                    aria-describedby="project_description-error"
                                ></textarea>
                                <div id="project_description-error" class="error" role="alert"></div>
                            </div>

                            <div class="form-group">
                                <label for="image_filename">Image Filename *</label>
                                <input 
                                    type="text" 
                                    id="image_filename" 
                                    name="image_filename" 
                                    required
                                    placeholder="e.g., my-project-screenshot.png"
                                    aria-describedby="image_filename-error"
                                >
                                <div id="image_filename-help" class="help-text">
                                    Enter the exact filename of your project image (must be in images folder)
                                </div>
                                <div id="image_filename-error" class="error" role="alert"></div>
                            </div>

                            <button type="submit" class="btn">Add Project</button>
                        </form>
                    </div>
                </div>

                <!-- Additional Information -->
                <div class="card">
                    <h2>What I'm Looking For</h2>
                    <div class="grid grid-3">
                        <div>
                            <h3>Career Opportunities</h3>
                            <p>Full-time software development positions, internships, or graduate program opportunities in web development, software engineering, or related fields.</p>
                        </div>
                        <div>
                            <h3>Freelance Projects</h3>
                            <p>Custom web applications, website development, consulting projects, or technical problem-solving challenges.</p>
                        </div>
                        <div>
                            <h3>Collaboration</h3>
                            <p>Open source contributions, hackathon partnerships, mentorship opportunities, or knowledge sharing initiatives.</p>
                        </div>
                    </div>
                </div>

                <!-- FAQ Section -->
                <div class="card">
                    <h2>Frequently Asked Questions</h2>
                    <div class="grid grid-2">
                        <div>
                            <h3>What's the best way to reach you?</h3>
                            <p>Email is the most reliable method. I check my inbox regularly and respond to all professional inquiries within 24 hours.</p>
                            
                            <h3>Do you work remotely?</h3>
                            <p>Yes, I'm comfortable with remote work and have experience collaborating with distributed teams using modern communication tools.</p>
                        </div>
                        <div>
                            <h3>What types of projects interest you most?</h3>
                            <p>I'm particularly interested in full-stack web applications, user experience optimization, and projects that solve real-world problems.</p>
                            
                            <h3>Are you available for consulting?</h3>
                            <p>Yes, I offer consulting services for web development projects, code reviews, and technical architecture guidance.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <div class="social-links">
                <a href="https://github.com/Pranav-44/aidd" target="_blank" rel="noopener noreferrer" aria-label="GitHub Profile">GitHub</a>
                <a href="https://www.linkedin.com/in/pranavdandagi/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn Profile">LinkedIn</a>
                <a href="mailto:pdandagi@iu.edu" aria-label="Email Contact">Email</a>
            </div>
            <p>&copy; 2024 Pranav's Portfolio. All rights reserved.</p>
            <p><a href="https://github.com/Pranav-44/aidd" target="_blank" rel="noopener noreferrer">View Source Code on GitHub</a></p>
        </div>
    </footer>
    <script>
        // Mobile menu toggle functionality
        document.addEventListener('DOMContentLoaded', function() {
            const mobileToggle = document.querySelector('.mobile-menu-toggle');
            const navLinks = document.querySelector('.nav-links');
            
            if (mobileToggle && navLinks) {
                mobileToggle.addEventListener('click', function() {
                    navLinks.classList.toggle('active');
                });
            }

            // Load available images for contact page
            function loadAvailableImagesContact() {{
                const imagesList = document.getElementById('availableImagesListContact');
                if (!imagesList) return;

                imagesList.innerHTML = '<div style="color: var(--text-light); font-style: italic; font-size: 0.875rem;">Loading available images...</div>';

                fetch('/api/available-images')
                    .then(response => response.json())
                    .then(images => {{
                        if (images.length === 0) {{
                            imagesList.innerHTML = '<div style="color: var(--text-light); font-style: italic; font-size: 0.875rem;">No images found in static/images folder</div>';
                            return;
                        }}

                        const imagesHtml = images.map(image => 
                            `<div style="margin-bottom: 0.25rem;">
                                <code style="background: var(--bg-tertiary); padding: 0.25rem 0.5rem; border-radius: var(--radius-sm); cursor: pointer; font-size: 0.75rem;" onclick="selectImageContact('${{image}}')">${{image}}</code>
                            </div>`
                        ).join('');

                        imagesList.innerHTML = imagesHtml;
                    }})
                    .catch(error => {{
                        console.error('Error loading images:', error);
                        imagesList.innerHTML = '<div style="color: var(--error-color); font-size: 0.875rem;">Error loading images</div>';
                    }});
            }}

            // Function to select an image when clicked on contact page
            function selectImageContact(filename) {{
                const imageInput = document.getElementById('image_filename');
                if (imageInput) {{
                    imageInput.value = filename;
                    imageInput.focus();
                }}
            }}

            // Make selectImageContact globally available
            window.selectImageContact = selectImageContact;

            // Load images on page load
            loadAvailableImagesContact();

            // Add refresh button functionality for contact page
            const refreshBtnContact = document.getElementById('refreshImagesBtnContact');
            if (refreshBtnContact) {{
                refreshBtnContact.addEventListener('click', function() {{
                    loadAvailableImagesContact();
                }});
            }}

            // Form validation functionality
            const form = document.getElementById('projectForm');

            // Form submission validation
            form.addEventListener('submit', function(event) {
                let isValid = true;

                // Clear previous errors
                const errorElements = document.querySelectorAll('.error');
                errorElements.forEach(element => {
                    element.textContent = '';
                    element.classList.remove('show');
                });

                // Validate all required fields
                const requiredFields = form.querySelectorAll('[required]');
                requiredFields.forEach(field => {
                    const errorElement = document.getElementById(field.id + '-error');
                    
                    if (!field.value.trim()) {
                        errorElement.textContent = 'This field is required';
                        errorElement.classList.add('show');
                        field.setCustomValidity('This field is required');
                        isValid = false;
                    } else {
                        field.setCustomValidity('');
                    }
                });

                // Additional validation for specific fields
                const title = document.getElementById('project_title');
                const description = document.getElementById('project_description');
                const imageFilename = document.getElementById('image_filename');

                // Title validation
                if (title.value && title.value.length < 3) {
                    document.getElementById('project_title-error').textContent = 'Title must be at least 3 characters long';
                    document.getElementById('project_title-error').classList.add('show');
                    title.setCustomValidity('Title too short');
                    isValid = false;
                }

                // Description validation
                if (description.value && description.value.length < 10) {
                    document.getElementById('project_description-error').textContent = 'Description must be at least 10 characters long';
                    document.getElementById('project_description-error').classList.add('show');
                    description.setCustomValidity('Description too short');
                    isValid = false;
                }

                // Image filename validation
                if (imageFilename.value && !/^[a-zA-Z0-9._\s-]+\\.(png|jpg|jpeg)$/i.test(imageFilename.value)) {
                    document.getElementById('image_filename-error').textContent = 'Please enter a valid image filename (e.g., project.png, project.jpg, project.jpeg)';
                    document.getElementById('image_filename-error').classList.add('show');
                    imageFilename.setCustomValidity('Invalid image filename');
                    isValid = false;
                }

                if (!isValid) {
                    event.preventDefault();
                    // Focus on first invalid field
                    const firstInvalidField = form.querySelector(':invalid');
                    if (firstInvalidField) {
                        firstInvalidField.focus();
                    }
                }
                // If valid, let the form submit naturally to the POST route
            });
        });
    </script>
</body>
</html>
"""
    # Ensure form action points to flask thankyou route
    html = html.replace('action="thankyou.html"', f'action="{url_for("thankyou")}"')
    return with_base_head(html)


@app.get('/thankyou')
def thankyou() -> Response:
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Thank you for contacting Pranav - Your message has been received">
    <title>Thank You - Pranav's Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="container">
            <div class="logo">Pranav's Portfolio</div>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="resume.html">Resume</a></li>
                <li><a href="projects.html">Projects</a></li>
                <li><a href="contact.html">Add Project</a></li>
            </ul>
            <button class="mobile-menu-toggle" aria-label="Toggle navigation menu">☰</button>
        </nav>
    </header>
    <main>
        <!-- Hero Section -->
        <section class="hero">
            <div class="container">
                <h1>Thank You!</h1>
                <p>Your message has been successfully sent</p>
            </div>
        </section>
        <!-- Thank You Content -->
        <section class="section">
            <div class="container">
                <div class="card" style="text-align: center; max-width: 600px; margin: 0 auto;">
                    <h2>Message Received</h2>
                    <p>Thank you for reaching out! I've received your message and will get back to you as soon as possible.</p>
                    
                    <div style="margin: 2rem 0;">
                        <h3>What happens next?</h3>
                        <ul style="text-align: left; display: inline-block;">
                            <li>I'll review your message within 24 hours</li>
                            <li>You'll receive a response via email</li>
                            <li>For urgent matters, I may reach out by phone</li>
                            <li>I'll follow up on any project discussions or opportunities</li>
                        </ul>
                    </div>

                    <div style="margin: 2rem 0;">
                        <h3>In the meantime...</h3>
                        <p>Feel free to explore more of my work or connect with me on social media:</p>
                        
                        <div class="social-links" style="margin: 1rem 0;">
                            <a href="https://linkedin.com/in/pranav" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn Profile">
                                LinkedIn
                            </a>
                            <a href="https://github.com/Pranav-44" target="_blank" rel="noopener noreferrer" aria-label="GitHub Profile">
                                GitHub
                            </a>
                            <a href="https://twitter.com/pranav" target="_blank" rel="noopener noreferrer" aria-label="Twitter Profile">
                                Twitter
                            </a>
                        </div>
                    </div>

                    <div style="margin: 2rem 0;">
                        <a href="index.html" class="btn">Back to Home</a>
                        <a href="projects.html" class="btn btn-secondary">View My Projects</a>
                    </div>

                    <div style="background-color: #F8F9FA; padding: 1.5rem; border-radius: 8px; margin-top: 2rem;">
                        <h4>Quick Response Times</h4>
                        <p><strong>General Inquiries:</strong> Within 24 hours</p>
                        <p><strong>Project Discussions:</strong> Within 12 hours</p>
                        <p><strong>Urgent Matters:</strong> Same day when possible</p>
                    </div>
                </div>

                <!-- Additional Resources -->
                <div class="grid grid-2" style="margin-top: 3rem;">
                    <div class="card">
                        <h3>Explore My Work</h3>
                        <p>Take a look at my latest projects and see examples of my development skills in action.</p>
                        <a href="projects.html" class="btn">View Projects</a>
                    </div>
                    
                    <div class="card">
                        <h3>Download Resume</h3>
                        <p>Get a PDF copy of my resume for your records or to share with your team.</p>
                        <a href="resume.pdf" class="btn" id="downloadResumeBtn" download>Download Resume</a>
                    </div>
                </div>

                <!-- Contact Information -->
                <div class="card" style="margin-top: 2rem;">
                    <h2>Alternative Contact Methods</h2>
                    <div class="grid grid-3">
                        <div>
                            <h4>Email</h4>
                            <p><a href="mailto:pranav@example.com">pranav@example.com</a></p>
                            <p>Best for detailed discussions</p>
                        </div>
                        <div>
                            <h4>LinkedIn</h4>
                            <p><a href="https://linkedin.com/in/pranav" target="_blank" rel="noopener noreferrer">linkedin.com/in/pranav</a></p>
                            <p>Great for professional networking</p>
                        </div>
                        <div>
                            <h4>GitHub</h4>
                            <p><a href="https://github.com/Pranav-44" target="_blank" rel="noopener noreferrer">github.com/Pranav-44</a></p>
                            <p>View my code and contributions</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <div class="social-links">
                <a href="https://github.com/Pranav-44" target="_blank" rel="noopener noreferrer" aria-label="GitHub Profile">GitHub</a>
                <a href="https://www.linkedin.com/in/pranavdandagi/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn Profile">LinkedIn</a>
                <a href="mailto:pdandagi@iu.edu" aria-label="Email Contact">Email</a>
            </div>
            <p>&copy; 2024 Pranav's Portfolio. All rights reserved.</p>
            <p><a href="https://github.com/Pranav-44/aidd" target="_blank" rel="noopener noreferrer">View Source Code on GitHub</a></p>
        </div>
    </footer>
    <script>
        // Mobile menu toggle functionality
        document.addEventListener('DOMContentLoaded', function() {
            const mobileToggle = document.querySelector('.mobile-menu-toggle');
            const navLinks = document.querySelector('.nav-links');
            
            if (mobileToggle && navLinks) {
                mobileToggle.addEventListener('click', function() {
                    navLinks.classList.toggle('active');
                });
            }

            // Display form data if available (for demonstration)
            const urlParams = new URLSearchParams(window.location.search);
            const firstName = urlParams.get('firstName');
            
            if (firstName) {
                const messageElement = document.querySelector('.card p');
                if (messageElement) {
                    messageElement.innerHTML = `Thank you for reaching out, ${firstName}! I've received your message and will get back to you as soon as possible.`;
                }
            }

            // Resume download with fallback to Print to PDF
            const downloadBtn = document.getElementById('downloadResumeBtn');
            if (downloadBtn) {
                downloadBtn.addEventListener('click', function(event) {
                    fetch('resume.pdf', { method: 'HEAD' }).then(function(response) {
                        if (response.ok) {
                            window.location.href = 'resume.pdf';
                        } else {
                            event.preventDefault();
                            window.print();
                        }
                    }).catch(function() {
                        event.preventDefault();
                        window.print();
                    });
                    event.preventDefault();
                });
            }
        });
    </script>
</body>
</html>
"""
    return with_base_head(html)


@app.get('/test')
def test_page() -> Response:
    # Developer test page for navigation; optional in Flask version
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website Test - All Pages</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .test-section { margin: 20px 0; padding: 20px; border: 1px solid #ccc; border-radius: 5px; }
        .test-link { display: inline-block; margin: 10px; padding: 10px 20px; background: #3498DB; color: white; text-decoration: none; border-radius: 5px; }
        .test-link:hover { background: #2980B9; }
        .status { padding: 5px 10px; border-radius: 3px; color: white; }
        .status.pass { background: #27AE60; }
        .status.fail { background: #E74C3C; }
        .status.warning { background: #F39C12; }
    </style>
</head>
<body>
    <h1>Personal Portfolio Website Test</h1>
    
    <div class="test-section">
        <h2>Page Navigation Test</h2>
        <p>Click each link to test page loading and navigation:</p>
        <a href="index.html" class="test-link" target="_blank">Home Page</a>
        <a href="about.html" class="test-link" target="_blank">About Page</a>
        <a href="resume.html" class="test-link" target="_blank">Resume Page</a>
        <a href="projects.html" class="test-link" target="_blank">Projects Page</a>
        <a href="contact.html" class="test-link" target="_blank">Contact Page</a>
        <a href="thankyou.html" class="test-link" target="_blank">Thank You Page</a>
    </div>

    <div class="test-section">
        <h2>Requirements Checklist</h2>
        <ul>
            <li><span class="status pass">✓</span> 6 HTML pages created (index, about, resume, projects, contact, thankyou)</li>
            <li><span class="status pass">✓</span> Consistent navigation bar on all pages</li>
            <li><span class="status pass">✓</span> External CSS stylesheet (styles.css) linked to all pages</li>
            <li><span class="status pass">✓</span> Responsive design with CSS Flexbox/Grid and media queries</li>
            <li><span class="status pass">✓</span> Semantic HTML tags (header, nav, main, footer)</li>
            <li><span class="status pass">✓</span> Contact form with required fields (First Name, Last Name, Email, Password, Confirm Password)</li>
            <li><span class="status pass">✓</span> HTML validation attributes (required, type, pattern, minlength)</li>
            <li><span class="status pass">✓</span> Password matching validation with JavaScript</li>
            <li><span class="status pass">✓</span> Labels linked with for and id attributes</li>
            <li><span class="status pass">✓</span> Alt text for all images (placeholders included)</li>
            <li><span class="status pass">✓</span> Form redirects to thankyou.html after submission</li>
            <li><span class="status pass">✓</span> AI documentation file (.prompt/dev_notes.md) created</li>
        </ul>
    </div>

    <div class="test-section">
        <h2>Browser Testing Instructions</h2>
        <ol>
            <li><strong>Chrome:</strong> Open each page and test navigation, form validation, and responsive design</li>
            <li><strong>Edge/Firefox:</strong> Repeat the same tests to ensure cross-browser compatibility</li>
            <li><strong>Mobile Testing:</strong> Use browser dev tools to test mobile responsiveness</li>
            <li><strong>Accessibility:</strong> Test keyboard navigation and screen reader compatibility</li>
        </ol>
    </div>

    <div class="test-section">
        <h2>Form Testing</h2>
        <p>Test the contact form with these scenarios:</p>
        <ul>
            <li>Submit with empty fields (should show validation errors)</li>
            <li>Submit with invalid email format</li>
            <li>Submit with mismatched passwords</li>
            <li>Submit with weak password (should fail validation)</li>
            <li>Submit with all valid data (should redirect to thankyou.html)</li>
        </ul>
    </div>

    <div class="test-section">
        <h2>Notes</h2>
        <p><span class="status warning">⚠</span> <strong>Images:</strong> Placeholder image paths are included. Add actual images to the /images directory for production.</p>
        <p><span class="status warning">⚠</span> <strong>Contact Info:</strong> Update email addresses, phone numbers, and social media links with actual information.</p>
        <p><span class="status warning">⚠</span> <strong>Resume PDF:</strong> Add an actual resume.pdf file for the download link.</p>
    </div>
</body>
</html>
"""
    # Convert links to Flask routes
    html = html.replace('href="index.html"', url_for('home')) \
               .replace('href="about.html"', url_for('about')) \
               .replace('href="resume.html"', url_for('resume')) \
               .replace('href="projects.html"', url_for('projects')) \
               .replace('href="contact.html"', url_for('contact')) \
               .replace('href="thankyou.html"', url_for('thankyou'))
    return html


@app.get('/styles.css')
def serve_styles():
    # Let Flask serve styles.css directly from the same directory
    with open('styles.css', 'rb') as f:
        content = f.read()
    return Response(content, mimetype='text/css')


@app.get('/images/<path:filename>')
def serve_image(filename: str):
    # Serve images from images folder
    from flask import send_from_directory
    return send_from_directory('images', filename)

@app.get('/static/<path:filename>')
def serve_static(filename: str):
    # Serve static files from static folder
    from flask import send_from_directory
    return send_from_directory('static', filename)


@app.get('/<path:filename>')
def serve_pdf_or_static(filename: str):
    # Serve any pdfs or other direct files in root (like resume.pdf)
    from flask import send_from_directory, abort
    if filename.lower().endswith('.pdf'):
        return send_from_directory('.', filename)
    # For old .html links, redirect to new routes
    mapping = {
        'index.html': url_for('home'),
        'about.html': url_for('about'),
        'resume.html': url_for('resume'),
        'projects.html': url_for('projects'),
        'contact.html': url_for('contact'),
        'thankyou.html': url_for('thankyou'),
    }
    if filename in mapping:
        return redirect(mapping[filename])
    abort(404)


@app.get('/api/available-images')
def get_available_images():
    """API endpoint to get list of available images in images folder."""
    import os
    import json
    
    try:
        images_dir = 'images'
        if not os.path.exists(images_dir):
            return json.dumps([])
        
        # Get all image files
        image_files = []
        for filename in os.listdir(images_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_files.append(filename)
        
        # Sort alphabetically
        image_files.sort()
        
        return json.dumps(image_files)
    except Exception as e:
        print(f"Error getting available images: {e}")
        return json.dumps([])

@app.get('/favicon.ico')
def favicon():
    # Avoid noisy 404s in logs
    return ('', 204)


if __name__ == '__main__':
    app.run(debug=True)


