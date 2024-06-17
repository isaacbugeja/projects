//nav icon code

document.getElementById('nav-toggle').addEventListener('click', function() {
    const navList = document.getElementById('nav-bar-list');
    navList.classList.toggle('show');
    this.textContent = navList.classList.contains('show') ? '✖' : '☰';
});

document.addEventListener('click', function(event) {
    const navList = document.getElementById('nav-bar-list');
    const navToggle = document.getElementById('nav-toggle');
    if (!navList.contains(event.target) && !navToggle.contains(event.target)) {
        navList.classList.remove('show');
        navToggle.textContent = '☰';
    }
});

//Back to Top button code
document.addEventListener('DOMContentLoaded', () => {
    const backToTopButton = document.querySelector('.top');
    const showButtonAt = 0.05 * document.documentElement.scrollHeight;

    window.addEventListener('scroll', () => {
        if (window.scrollY > showButtonAt) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });
});
