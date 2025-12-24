// Search filter
function filterProperties() {
  const value = document.getElementById("searchLocation").value.toLowerCase();
  document.querySelectorAll(".card").forEach(card => {
    card.style.display = card.innerText.toLowerCase().includes(value)
      ? "block"
      : "none";
  });
}

// Card animation
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => e.isIntersecting && e.target.classList.add("show"));
});

document.querySelectorAll(".card").forEach(card => observer.observe(card));

// Mobile menu
const menuToggle = document.getElementById("menuToggle");
const navLinks = document.getElementById("navLinks");

menuToggle.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});
