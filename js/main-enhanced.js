// Enhanced main page JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const headerOffset = 80;
                    const elementPosition = target.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-visible');
            }
        });
    }, observerOptions);

    // Observe part cards
    const partCards = document.querySelectorAll('.part-card-enhanced');
    partCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `opacity 0.6s ${index * 0.1}s, transform 0.6s ${index * 0.1}s`;
        observer.observe(card);
    });

    // Add fade-in class when visible
    const style = document.createElement('style');
    style.textContent = `
        .fade-in-visible {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);

    // Form enhancement
    const consultationForm = document.getElementById('consultation-form');
    if (consultationForm) {
        consultationForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = {
                name: document.getElementById('name').value,
                phone: document.getElementById('phone').value,
                email: document.getElementById('email').value,
                businessType: document.getElementById('business-type').value,
                topic: document.getElementById('topic').value,
                message: document.getElementById('message').value
            };

            if (!formData.name || !formData.phone || !formData.topic) {
                alert('필수 항목을 모두 입력해주세요.');
                return;
            }

            // Show success message with style
            const successMessage = document.createElement('div');
            successMessage.style.cssText = `
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 2rem 3rem;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                z-index: 10000;
                text-align: center;
                animation: fadeInScale 0.3s ease-out;
            `;
            successMessage.innerHTML = `
                <h3 style="margin-bottom: 1rem; font-size: 1.5rem;">상담 신청이 완료되었습니다</h3>
                <p style="margin-bottom: 1.5rem;">곧 연락드리겠습니다.<br>감사합니다.</p>
                <button onclick="this.parentElement.remove()" style="
                    background: white;
                    color: #667eea;
                    border: none;
                    padding: 0.75rem 2rem;
                    border-radius: 50px;
                    font-weight: 600;
                    cursor: pointer;
                ">확인</button>
            `;
            document.body.appendChild(successMessage);
            
            consultationForm.reset();
        });
    }

    // Add fadeInScale animation
    const animationStyle = document.createElement('style');
    animationStyle.textContent = `
        @keyframes fadeInScale {
            from {
                opacity: 0;
                transform: translate(-50%, -50%) scale(0.9);
            }
            to {
                opacity: 1;
                transform: translate(-50%, -50%) scale(1);
            }
        }
    `;
    document.head.appendChild(animationStyle);
});


