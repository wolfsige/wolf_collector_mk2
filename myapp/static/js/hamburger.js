const toggleButton = document.getElementsByClassName('toggle-btn')[0]
const navbarLink = document.getElementsByClassName('navbar-links')[0]

toggleButton.addEventListener("click", () => {
  navbarLink.classList.toggle('active')
})