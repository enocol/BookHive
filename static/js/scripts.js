addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar");
  const arrow = document.querySelector(".arrow");

  sidebar.addEventListener("mouseenter", function () {
    sidebar.classList.add("show");
    arrow.style.transform = "rotate(180deg)";
    arrow.style.transition = "transform 0.3s ease"; // smooth animation
  });
  sidebar.addEventListener("mouseleave", function () {
    sidebar.classList.remove("show");
    arrow.style.transform = "rotate(0deg)";
    arrow.style.transition = "transform 0.3s ease"; // smooth animation
  });
});

let lastScrollTop = 0;
const footer = document.getElementById("page-footer");
let scrollTimeout = null;

document.addEventListener(
  "scroll",
  function () {
    const currentScroll =
      document.pageYOffset || document.documentElement.scrollTop;

    // Always hide the footer on scroll
    footer.classList.add("footer-hidden");

    // Clear the previous timeout
    if (scrollTimeout !== null) {
      clearTimeout(scrollTimeout);
    }

    // Set timeout to show footer after 3 seconds of no scrolling
    scrollTimeout = setTimeout(() => {
      footer.classList.remove("footer-hidden");
    }, 2000);

    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
  },
  false
);
