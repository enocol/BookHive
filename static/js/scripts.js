addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar");
  sidebar.addEventListener("mouseenter", function () {
    sidebar.classList.add("show");
  });
  sidebar.addEventListener("mouseleave", function () {
    sidebar.classList.remove("show");
  });
});
