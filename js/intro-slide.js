// Intro Slide JavaScript - Full Screen Presentation

let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    // Show first slide
    if (slides.length > 0) {
        slides[0].classList.add('active');
    }

    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
            e.preventDefault();
            nextSlide();
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
            e.preventDefault();
            prevSlide();
        } else if (e.key === 'Home') {
            e.preventDefault();
            goToSlide(0);
        } else if (e.key === 'End') {
            e.preventDefault();
            goToSlide(totalSlides - 1);
        }
    });

    // Touch/swipe support
    let touchStartX = 0;
    let touchEndX = 0;

    document.addEventListener('touchstart', function(e) {
        touchStartX = e.changedTouches[0].screenX;
    });

    document.addEventListener('touchend', function(e) {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });

    function handleSwipe() {
        const swipeThreshold = 50;
        const diff = touchStartX - touchEndX;

        if (Math.abs(diff) > swipeThreshold) {
            if (diff > 0) {
                // Swipe left - next slide
                nextSlide();
            } else {
                // Swipe right - previous slide
                prevSlide();
            }
        }
    }

    // Navigation button handlers
    const prevButtons = document.querySelectorAll('.btn-prev');
    const nextButtons = document.querySelectorAll('.btn-next');

    prevButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            prevSlide();
        });
    });

    nextButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            const href = btn.getAttribute('href');
            if (href && href.startsWith('#')) {
                e.preventDefault();
                nextSlide();
            }
        });
    });

    // Update slide indicator
    updateSlideIndicator();
});

function nextSlide() {
    if (currentSlide < totalSlides - 1) {
        goToSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 0) {
        goToSlide(currentSlide - 1);
    }
}

function goToSlide(index) {
    if (index < 0 || index >= totalSlides) return;

    // Remove active class from current slide
    slides[currentSlide].classList.remove('active');
    slides[currentSlide].classList.add('prev');

    // Update current slide
    currentSlide = index;

    // Add active class to new slide
    slides[currentSlide].classList.remove('prev');
    slides[currentSlide].classList.add('active');

    // Update URL hash
    window.location.hash = `slide${currentSlide + 1}`;

    // Update slide indicator
    updateSlideIndicator();
}

function updateSlideIndicator() {
    const indicators = document.querySelectorAll('.slide-indicator');
    indicators.forEach(indicator => {
        indicator.textContent = `${currentSlide + 1} / ${totalSlides}`;
    });
}

// Handle hash navigation
window.addEventListener('hashchange', function() {
    const hash = window.location.hash;
    if (hash) {
        const match = hash.match(/slide(\d+)/);
        if (match) {
            const slideIndex = parseInt(match[1]) - 1;
            if (slideIndex >= 0 && slideIndex < totalSlides) {
                goToSlide(slideIndex);
            }
        }
    }
});

// Initialize from hash if present
if (window.location.hash) {
    const hash = window.location.hash;
    const match = hash.match(/slide(\d+)/);
    if (match) {
        const slideIndex = parseInt(match[1]) - 1;
        if (slideIndex >= 0 && slideIndex < totalSlides) {
            goToSlide(slideIndex);
        }
    }
}

// Prevent default scroll behavior
document.addEventListener('wheel', function(e) {
    if (e.deltaY > 0) {
        e.preventDefault();
        nextSlide();
    } else {
        e.preventDefault();
        prevSlide();
    }
}, { passive: false });


