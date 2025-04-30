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

document.addEventListener(
  "scroll",
  function () {
    const currentScroll =
      document.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll > lastScrollTop) {
      // Scrolling down
      footer.classList.add("footer-hidden");
    } else {
      // Scrolling up
      footer.classList.remove("footer-hidden");
    }

    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // For Mobile or negative scrolling
  },
  false
);
