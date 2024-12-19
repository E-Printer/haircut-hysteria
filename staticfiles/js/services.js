document.addEventListener("DOMContentLoaded", () => {
    const tabs = document.querySelectorAll(".tab-item a");
    const panels = document.querySelectorAll(".wpb_tab");

    tabs.forEach(tab => {
        tab.addEventListener("click", e => {
            e.preventDefault();

            // Remove active class from all tabs and hide all panels
            tabs.forEach(t => t.classList.remove("active-tab"));
            panels.forEach(panel => panel.classList.remove("active"));

            // Activate clicked tab and display its panel
            tab.classList.add("active-tab");
            const target = document.querySelector(tab.getAttribute("href"));
            target.classList.add("active");
        });
    });
});