document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('.menu li');
    
    menuItems.forEach(item => {
        const link = item.querySelector('a');
        const subMenu = item.querySelector('ul');
        
        if (subMenu) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                item.classList.toggle('expanded');
                item.classList.toggle('collapsed');
            });
        }
    });
});
